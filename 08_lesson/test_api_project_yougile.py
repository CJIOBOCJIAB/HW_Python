import os
import pytest
from dotenv import load_dotenv


from YouGilePage import ProjectYouGile


load_dotenv()


@pytest.fixture(scope='session')
def api():
    url = "https://ru.yougile.com/api-v2"
    return ProjectYouGile(url)


@pytest.fixture
def id_project(api):
    title = 'Test Project'
    user_id = os.getenv("USER_ID")
    status_code, project = api.create_new_project(title, user_id)
    assert status_code == 201, "Не удалось создать проект для теста"
    yield project


def test_create_new_project(api):
    title = "тест реквест"
    user_id = os.getenv('USER_ID')
    status_code, response = api.create_new_project(title, user_id)
    assert status_code == 201
    assert response['id'] is not None


def test_create_new_project_negative(api):
    title = "тест реквест"
    user_id = os.getenv('MISS_USER_ID')
    status_code, response = api.create_new_project(title, user_id)

    assert status_code == 400
    assert (response['message'] ==
            'Сотрудники со следующими ID не найдены в компании:'
            ' 009ffd80-5bd4-4068-aa5e-af06a188af85')
    assert response['error'] == 'Bad Request'


def test_update_project(api, id_project):
    new_title = 'тест инвест'
    user_id = os.getenv("USER_ID")
    status, new_project = api.update_project(
        id_project['id'], new_title, user_id)
    assert status == 200
    assert new_project is not None


def test_update_project_negative(api):
    new_title = 'тест баг-тест'
    user_id = os.getenv("USER_ID")
    status, new_project = api.update_project(
        '12345', new_title, user_id)
    assert status == 404
    assert "Проект не найден" in new_project.get("message")


def test_get_project(api, id_project):
    status, project_data = api.get_project(id_project['id'])
    assert status == 200
    assert project_data['id'] == id_project['id']


def test_get_project_negative(api):
    status, project_id = api.get_project(api)
    assert status == 404
    assert 'Проект не найден' in project_id.get("message")

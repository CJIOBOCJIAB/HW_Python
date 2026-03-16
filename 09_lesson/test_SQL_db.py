import pytest

from QA_table import SubjectTable


@pytest.fixture
def db():
    db_connection = SubjectTable(
        "postgresql://postgres:sql@localhost:5432/QA")
    yield db_connection
    db_connection.close()

# @pytest.fixture
# def subject(db):
#     sid = db.insert("Base_Test_Subject")
#     yield sid
#     db.delete_by_id(sid)


def test_add_subject(db):
    subject_title = "Google"
    new_id = db.insert(subject_title)
    res = db.get_by_id(new_id)
    assert res["subject_title"] == subject_title
    print(res)
    db.delete_by_id(new_id)
    print("объект удалён")


def test_update_subject1(db):
    subject_title = "Boogle"
    new_id = db.insert(subject_title)
    res = db.get_by_id(new_id)
    test_id = res["subject_id"]
    print(res)

    new_title = "Google_Boogle"
    db.update(test_id, new_title)
    res = db.get_by_id(test_id)
    assert res["subject_title"] == new_title
    print(res)
    db.delete_by_id(test_id)
    print("объект удалён")


def test_delete_subject_by_id(db):
    new_id = db.insert("Delete_by_id")
    res = db.get_by_id(new_id)
    print(res)
    success = db.delete_by_id(new_id)
    assert success is True
    res = db.get_by_id(new_id)
    assert res is None
    print(res)


def test_delete_subject_by_title(db):
    subject_title = "Delete_by_title"
    new_id = db.insert(subject_title)
    created = db.get_by_id(new_id)
    assert created is not None
    print(created)

    db.delete_by_title(subject_title)
    res = db.get_by_id(new_id)
    assert res is None
    print(res)

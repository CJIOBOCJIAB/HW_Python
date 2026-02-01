import pytest
from string_utils import StringUtils

@pytest.fixture(scope="module")
def utils():
    return StringUtils()

# capitalize tests
@pytest.mark.positive
def test_capitalize_valid(utils):
    assert utils.capitalize("hello") == "Hello"
    assert utils.capitalize("world") == "World"
    assert utils.capitalize("a") == "A"

@pytest.mark.positive
def test_capitalize_empty(utils):
    assert utils.capitalize("") == ""

@pytest.mark.negative
def test_capitalize_none(utils):
    with pytest.raises(TypeError):
        utils.capitalize(None)

# trim tests
@pytest.mark.positive
def test_trim_valid(utils):
    assert utils.trim(" hello ") == "hello"
    assert utils.trim(" no_spaces_here ") == "no_spaces_here"

@pytest.mark.positive
def test_trim_empty(utils):
    assert utils.trim("") == ""

@pytest.mark.negative
def test_trim_none(utils):
    with pytest.raises(TypeError):
        utils.trim(None)

# contains tests
@pytest.mark.positive
def test_contains_valid(utils):
    assert utils.contains("Skypro", "S")
    assert not utils.contains("Skypro", "X")

@pytest.mark.negative
def test_contains_none(utils):
    with pytest.raises(TypeError):
        utils.contains(None, "S")

# delete_symbol tests
@pytest.mark.positive
def test_delete_symbol_valid(utils):
    assert utils.delete_symbol("Skypro", "p") == "Skyro"
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"

@pytest.mark.positive
def test_delete_symbol_empty(utils):
    assert utils.delete_symbol("", "S") == ''

@pytest.mark.negative
def test_delete_symbol_none(utils):
    with pytest.raises(TypeError):
        utils.delete_symbol(None, 'S')

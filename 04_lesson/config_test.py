def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "positive: Тесты, проверяющие корректное поведение функций"
    )
    config.addinivalue_line(
        "markers",
        "negative: Тесты, проверяющие некорректное поведение функций"
    )

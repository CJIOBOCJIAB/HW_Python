class StringUtils: # Класс с полезными утилитами для обработки и анализа строк
    def capitalize(self, s: str) -> str: # Принимает и возвращает текст, делает первую букву заглавной
        if isinstance(s, str):
            return s.capitalize()
        raise TypeError("Input must be a string.")

    def trim(self, s: str) -> str: # Принимает текст и удаляет пробелы в начале
        if isinstance(s, str):
            return s.strip()
        raise TypeError("Input must be a string.")

    def contains(self, s: str, char: str) -> bool: # Возвращает `True` или `False`, если строка содержит искомый символ
        if isinstance(s, str) and isinstance(char, str):
            return char in s
        raise TypeError("Both inputs must be strings.")

    def delete_symbol(self, s: str, char: str) -> str: # Удаляет из переданной строки указанные параметры
        if isinstance(s, str) and isinstance(char, str):
            return s.replace(char, '')
        raise TypeError("Both inputs must be strings.")

from sqlalchemy import create_engine, text


class SubjectTable:

    _scripts = {
        "get_max_subject_id": text(
            "SELECT MAX(subject_id) FROM subject"),
        "insert": text(
            "INSERT INTO subject ("
            "subject_id, subject_title) VALUES ("
            ":subject_id, :subject_title)"),
        "select_by_subject_id": text(
            "SELECT * FROM subject WHERE subject_id = :subject_id"),
        "update": text(
            "UPDATE subject SET subject_title = :"
            "new_title WHERE subject_id = :subject_id"),
        "delete_by_subject_id": text(
            "DELETE FROM subject WHERE subject_id = :subject_id"),
        "delete_by_subject_title": text(
            "DELETE FROM subject WHERE subject_title = :subject_title")
    }

    def __init__(self, connect_way):
        self.db = create_engine(connect_way)
        self.acc = None

    def _ensure_connection(self):
        # Гарантирует наличие активного соединения(частный случай)
        if self.acc is None or self.acc.closed:
            self.acc = self.db.connect()
        return self.acc

    def get_new_id(self):
        conn = self._ensure_connection()
        result = conn.execute(
            self._scripts["get_max_subject_id"]).scalar()
        return (result if result is not None else 0) + 1

    def insert(self, subject_title):
        next_id = self.get_new_id()
        conn = self._ensure_connection()
        try:
            conn.execute(
                self._scripts["insert"],
                {
                    "subject_id": next_id, "subject_title": subject_title}
            )
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        return next_id

    def get_by_id(self, subject_id):
        conn = self._ensure_connection()
        result = conn.execute(
            self._scripts["select_by_subject_id"],
            {"subject_id": subject_id}
        )
        row = result.mappings().first()
        return row

    def update(self, subject_id, new_title):
        conn = self._ensure_connection()
        existing = self.get_by_id(subject_id)
        if not existing:
            raise ValueError(
                f"Subject with ID {subject_id} not found")
        try:
            conn.execute(
                self._scripts["update"],
                {
                    "new_title": new_title, "subject_id": subject_id}
            )
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            raise e

    def delete_by_id(self, subject_id):
        conn = self._ensure_connection()
        existing = self.get_by_id(subject_id)
        if not existing:
            return False
        try:
            conn.execute(
                self._scripts["delete_by_subject_id"],
                {"subject_id": subject_id}
            )
            conn.commit()
            return True
        except Exception as e:
            if conn:
                conn.rollback()
            raise e

    def delete_by_title(self, subject_title):
        conn = self._ensure_connection()
        try:
            conn.execute(
                self._scripts["delete_by_subject_title"],
                {"subject_title": subject_title}
            )
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            raise e

    def close(self):
        if self.acc and not self.acc.closed:
            self.acc.close()
            self.acc = None

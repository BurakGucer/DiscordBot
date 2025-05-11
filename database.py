import sqlite3
from typing import List, Tuple, Optional

class Database:
    def __init__(self, db_name: str = "tasks.db"):
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    completed INTEGER NOT NULL DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def add_task(self, description: str) -> int:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (description) VALUES (?)",
                (description,)
            )
            conn.commit()
            return cursor.lastrowid

    def delete_task(self, task_id: int) -> bool:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            return cursor.rowcount > 0

    def complete_task(self, task_id: int) -> bool:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tasks SET completed = 1 WHERE id = ?",
                (task_id,)
            )
            conn.commit()
            return cursor.rowcount > 0

    def get_all_tasks(self) -> List[Tuple[int, str, bool]]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, description, completed FROM tasks ORDER BY id")
            return [(id, desc, bool(completed)) for id, desc, completed in cursor.fetchall()]

    def get_task(self, task_id: int) -> Optional[Tuple[int, str, bool]]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, description, completed FROM tasks WHERE id = ?",
                (task_id,)
            )
            result = cursor.fetchone()
            if result is None:
                return None
            return (result[0], result[1], bool(result[2])) 
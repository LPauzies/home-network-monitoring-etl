from typing import List


class SQLQueriesFactory:

    @staticmethod
    def generate_insert_query(table: str, columns: List[str], values: List[str]) -> str:
        query = f"INSERT INTO {table} "
        query += "(" + ", ".join(columns) + ") "
        query += "VALUES (" + ", ".join(values) + ")"
        return query
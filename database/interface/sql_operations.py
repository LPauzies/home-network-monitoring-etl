from interface.sql_connection_factory import SQLConnectionFactory

class SQLOperations:

    @staticmethod
    def execute_sql_query(sql_query: str) -> None:
        connection = SQLConnectionFactory.create_connection()
        connection.executescript(sql_query)
        connection.commit()
        connection.close()
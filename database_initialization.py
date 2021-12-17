""" Endpoint to create SQLite data model """
import os
from database.interface.sql_operations import SQLOperations

INIT_DATABASE_MODEL_SQL = os.path.join("database", "model", "nuke_and_create_data_model.sql")

def main() -> None:
    SQLOperations.execute_sql_script(INIT_DATABASE_MODEL_SQL)

if __name__ == "__main__":
    main()

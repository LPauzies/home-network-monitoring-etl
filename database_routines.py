""" Endpoint to create database routines """
import os
from database.interface.sql_operations import SQLOperations

# SQL scripts to be defined as routines
ROUTINE_SQL_SCRIPTS = [
    os.path.join("database", "routines", "routine_delete_last_values.sql")
]

def main() -> None:
    for script in ROUTINE_SQL_SCRIPTS:
        SQLOperations.execute_sql_script(script)

if __name__ == "__main__":
    main()
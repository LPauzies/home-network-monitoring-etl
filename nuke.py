""" Endpoint to create database routines """
import os
from database.interface.sql_operations import SQLOperations

# SQL scripts to be defined as routines
NUKE_SQL_SCRIPTS = [os.path.join("nuke", nuke) for nuke in os.listdir("nuke")]

def main() -> None:
    for script in NUKE_SQL_SCRIPTS:
        SQLOperations.execute_sql_script(script)

if __name__ == "__main__":
    main()
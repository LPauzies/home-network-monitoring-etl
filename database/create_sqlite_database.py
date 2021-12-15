import os
from interface.sql_operations import SQLOperations

INIT_DATABASE_MODEL_SQL = os.path.join("database", "model", "nuke_and_create_data_model.sql")

def main() -> None:
    with open(INIT_DATABASE_MODEL_SQL, "r") as sql_descriptor:
        sql_script = sql_descriptor.read()
        SQLOperations.execute_sql_query(sql_script)

if __name__ == "__main__":
    main()

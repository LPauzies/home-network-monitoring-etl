import sqlite3
import logging

# Create logger here
logger = logging.getLogger(__name__)

SQLITE_DATABASE_FILE = "database/sqlite/NetworkMonitoring.db"

class SQLConnectionFactory:

    def create_connection() -> sqlite3.Connection:
        try:
            return sqlite3.connect(SQLITE_DATABASE_FILE)
        except sqlite3.Error as error:
            logger.exception(error)
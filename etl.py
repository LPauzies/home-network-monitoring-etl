import os
from etl.configuration.parse_configuration import ConfigurationParser
from etl.process.network_monitor import NetworkMonitor
from database.interface.sql_queries import SQLQueriesFactory
from database.data_model.data_model import Ping

CONFIGURATION_FILE_PATH = os.path.join("etl-configuration.json")

def main() -> None:

    # Parse the configuration
    parser = ConfigurationParser(CONFIGURATION_FILE_PATH)
    configurations = parser.parse()

    # For each configuration, make a ping
    for configuration in configurations:
        ping = NetworkMonitor.ping(configuration)
        query = SQLQueriesFactory.generate_insert_query(
            Ping.TABLE,
            Ping.Columns.ALL,
            ping.to_list()
        )

if __name__ == "__main__":
    main()
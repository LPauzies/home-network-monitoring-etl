import os
from typing import List
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from database_routines import main as main_routines
from etl.configuration.parse_configuration import ConfigurationParser, Configuration
from etl.process.network_monitor import NetworkMonitor
from database.interface.sql_queries import SQLQueriesFactory
from database.interface.sql_operations import SQLOperations
from database.data_model.data_model import Ping

import warnings
warnings.filterwarnings("ignore")

CONFIGURATION_FILE_PATH = os.path.join("etl-configuration.json")

### JOBS

def monitor_pings(configurations: List[Configuration], verbose=False) -> None:
    # For each configuration, make a ping
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if verbose: print(f"Ping executed at {current_time}.")
    now = int(datetime.timestamp(datetime.now()))
    for configuration in configurations:
        ping = NetworkMonitor.ping(configuration, now)
        insertion_query = SQLQueriesFactory.generate_insert_query(
            Ping.TABLE,
            Ping.Columns.ALL,
            ping.to_inserted_values()
        )
        SQLOperations.execute_sql_query(insertion_query)

def launch_routines(verbose=False) -> None:
    # Launch routines for database
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if verbose: print(f"Routines executed at {current_time}.")
    main_routines()

### ENTRY POINTS

def main() -> None:

    # Parse the configuration
    parser = ConfigurationParser(CONFIGURATION_FILE_PATH)
    configuration = parser.parse()

    # Setup the scheduler
    scheduler = BlockingScheduler()
    # Add monitoring job
    scheduler.add_job(monitor_pings, trigger="cron", args=[configuration.entities, True], second=f"*/{configuration.monitoring_delay}")
    # Add routines job
    scheduler.add_job(launch_routines, trigger="interval", args=[True], seconds=configuration.routines_delay)

    # Said to user that he can easily get out the scheduler
    print('Press Ctrl+{0} to exit'.format('C' if os.name == 'nt' else 'Break'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == "__main__":
    main()
import os
from etl.configuration.parse_configuration import ConfigurationParser

CONFIGURATION_FILE_PATH = os.path.join("etl-configuration.json")

def main() -> None:

    # Parse the configuration
    parser = ConfigurationParser(CONFIGURATION_FILE_PATH)
    configurations = parser.parse()

if __name__ == "__main__":
    main()
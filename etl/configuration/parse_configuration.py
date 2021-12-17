import json
from dataclasses import dataclass
from typing import List

class ConfigurationModel:
    IP = "ip"
    DOMAIN = "domain"
    DESCRIPTION = "description"

@dataclass
class Configuration:
    ip: str
    domain: str
    description: str

class ConfigurationParser:

    def __init__(self, configuration_path: str) -> None:
        self.configuration_path = configuration_path

    def parse(self) -> List[Configuration]:
        parsed_configurations = []
        with open(self.configuration_path, "r") as configuration_descriptor:
            configurations = json.load(configuration_descriptor)
            for configuration in configurations:
                parsed_configuration = Configuration(
                    configuration[ConfigurationModel.IP], 
                    configuration[ConfigurationModel.DOMAIN], 
                    configuration[ConfigurationModel.DESCRIPTION]
                )
                parsed_configurations.append(parsed_configuration)
        return parsed_configurations
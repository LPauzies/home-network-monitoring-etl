import json
from dataclasses import dataclass
from typing import List

class EntityModel:
    IP = "ip"
    DOMAIN = "domain"
    DESCRIPTION = "description"

class ConfigurationModel:
    MONITORING_DELAY = "monitoring_delay"
    ROUTINES_DELAY = "routines_delay"
    ENTITIES = "entities"

@dataclass
class Entity:
    ip: str
    domain: str
    description: str

@dataclass
class Configuration:
    monitoring_delay: int
    routines_delay: int
    entities: List[Entity]

class ConfigurationParser:

    def __init__(self, configuration_path: str) -> None:
        self.configuration_path = configuration_path

    def parse(self) -> Configuration:
        parsed_entities = []
        with open(self.configuration_path, "r") as configuration_descriptor:
            configuration = json.load(configuration_descriptor)
            for entity in configuration[ConfigurationModel.ENTITIES]:
                parsed_configuration = Entity(
                    entity[EntityModel.IP],
                    entity[EntityModel.DOMAIN],
                    entity[EntityModel.DESCRIPTION]
                )
                parsed_entities.append(parsed_configuration)
            return Configuration(
                configuration[ConfigurationModel.MONITORING_DELAY],
                configuration[ConfigurationModel.ROUTINES_DELAY],
                parsed_entities
            )
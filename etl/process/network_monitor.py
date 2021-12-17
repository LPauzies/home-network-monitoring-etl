import math

from typing import List
from dataclasses import dataclass
from datetime import date, datetime
from pythonping import ping
from dataclasses import dataclass

from etl.configuration.parse_configuration import Configuration

@dataclass
class Ping:
    event_time: int
    ip: str
    domain: str
    ip_description: str
    response_time: float
    packet_loss: bool

    def to_list(self) -> List[str]:
        return list(map(str, [
            self.event_time,
            self.ip,
            self.domain,
            self.ip_description,
            self.response_time,
            self.packet_loss
        ]))


class NetworkMonitor:

    @staticmethod
    def ping(configuration: Configuration) -> Ping:
        response = ping(configuration.ip, count=1)
        return Ping(
            event_time = int(datetime.timestamp(datetime.now())),
            ip = configuration.ip,
            domain = configuration.domain,
            ip_description = configuration.description,
            response_time = math.ceil(response.rtt_avg * 100) / 100,
            packet_loss = int(response.packet_loss) != 0
        )
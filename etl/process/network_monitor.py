import math
from typing import List
from dataclasses import dataclass
from datetime import datetime
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

    def to_inserted_values(self) -> List[str]:
        return [
            str(self.event_time),
            f"'{self.ip}'",
            f"'{self.domain}'",
            f"'{self.ip_description}'",
            str(self.response_time),
            "1" if self.packet_loss else "0"
        ]


class NetworkMonitor:

    @staticmethod
    def ping(configuration: Configuration, now=int(datetime.timestamp(datetime.now()))) -> Ping:
        response = ping(configuration.ip, count=1)
        return Ping(
            event_time = now,
            ip = configuration.ip,
            domain = configuration.domain,
            ip_description = configuration.description,
            response_time = math.ceil(response.rtt_avg * 100) / 100,
            packet_loss = int(response.packet_loss) == 1
        )
from dataclasses import dataclass, field

import mythic_container
from mythic_container.deprecation import deprecated_property
from mythic_container.logging import logger
from mythic_container.MythicGoRPC.messages import SuccessMessage
import base64

MYTHIC_RPC_AGENTSTORAGE_SEARCH = "mythic_rpc_agentstorage_search"


class MythicRPCAgentStorageSearchMessage:
    def __init__(self,
                 SearchUniqueID: str,
                 **kwargs):
        self.SearchUniqueID = SearchUniqueID
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "unique_id": self.SearchUniqueID
        }


class MythicRPCAgentStorageSearchResult:
    def __init__(self,
                 unique_id: str = "",
                 data: str = "",
                 **kwargs):
        self.UniqueID = unique_id
        self.Data = base64.b64decode(data)
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")


@dataclass
class MythicRPCAgentStorageSearchMessageResponse(SuccessMessage):

    agentstorage_messages: list[MythicRPCAgentStorageSearchResult] = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self.agentstorage_messages, list):
            self.agentstorage_messages = [
                MythicRPCAgentStorageSearchResult(**msg) if isinstance(msg, dict) else msg
                for msg in self.agentstorage_messages
            ]

    @property
    def AgentStorageMessages(self)-> list[MythicRPCAgentStorageSearchResult]:
        deprecated_property("AgentStorageMessages", "agentstorage_messages")
        return self.agentstorage_messages


async def SendMythicRPCAgentStorageSearch(
        msg: MythicRPCAgentStorageSearchMessage) -> MythicRPCAgentStorageSearchMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_AGENTSTORAGE_SEARCH,
                                                                            body=msg.to_json())
    return MythicRPCAgentStorageSearchMessageResponse(**response)

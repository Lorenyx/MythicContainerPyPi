from dataclasses import dataclass

import mythic_container
from mythic_container.deprecation import deprecated_property
from mythic_container.logging import logger
from mythic_container.MythicGoRPC.messages import SuccessMessage

MYTHIC_RPC_APITOKEN_CREATE    = "mythic_rpc_apitoken_create"


class MythicRPCAPITokenCreateMessage:
    def __init__(self,
                 AgentTaskID: str = None,
                 AgentCallbackID: str = None,
                 PayloadUUID: str = None,
                 OperationID: int = None,
                 **kwargs):
        self.AgentTaskID = AgentTaskID
        self.AgentCallbackID = AgentCallbackID
        self.PayloadUUID = PayloadUUID
        self.OperationID = OperationID
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "agent_task_id": self.AgentTaskID,
            "agentCallback_id": self.AgentCallbackID,
            "payload_uuid": self.PayloadUUID,
            "operation_id": self.OperationID
        }


@dataclass
class MythicRPCAPITokenCreateMessageResponse(SuccessMessage):

    apitoken: str = ""

    @property
    def APIToken(self) -> str:
        deprecated_property("APIToken", "apitoken")
        return self.apitoken


async def SendMythicRPCAPITokenCreate(
        msg: MythicRPCAPITokenCreateMessage) -> MythicRPCAPITokenCreateMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_APITOKEN_CREATE,
                                                                            body=msg.to_json())
    return MythicRPCAPITokenCreateMessageResponse(**response)

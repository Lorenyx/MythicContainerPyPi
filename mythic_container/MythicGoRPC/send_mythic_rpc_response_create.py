import mythic_container
from mythic_container.logging import logger
from mythic_container.MythicGoRPC.messages import SuccessMessage
import base64

MYTHIC_RPC_RESPONSE_CREATE = "mythic_rpc_response_create"


class MythicRPCResponseCreateMessage:
    def __init__(self,
                 TaskID: int,
                 Response: bytes,
                 **kwargs):
        self.TaskID = TaskID
        self.Response = Response
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "task_id": self.TaskID,
            "response": base64.b64encode(self.Response.encode()).decode() if isinstance(self.Response, str) else base64.b64encode(self.Response).decode()
        }


class MythicRPCResponseCreateMessageResponse(SuccessMessage):
    ...


async def SendMythicRPCResponseCreate(
        msg: MythicRPCResponseCreateMessage) -> MythicRPCResponseCreateMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_RESPONSE_CREATE,
                                                                            body=msg.to_json())
    return MythicRPCResponseCreateMessageResponse(**response)

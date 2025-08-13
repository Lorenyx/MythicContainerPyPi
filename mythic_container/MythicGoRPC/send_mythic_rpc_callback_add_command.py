import mythic_container
from mythic_container.logging import logger
from mythic_container.MythicGoRPC.messages import SuccessMessage

MYTHIC_RPC_CALLBACK_ADD_COMMAND = "mythic_rpc_callback_add_command"


class MythicRPCCallbackAddCommandMessage:
    def __init__(self,
                 Commands: list[str],
                 TaskID: int = None,
                 CallbackAgentUUID: str = None,
                 PayloadType: str = None,
                 CallbackIDs: list[int] = [],
                 **kwargs):
        self.TaskID = TaskID
        self.CallbackAgentUUID = CallbackAgentUUID
        self.Commands = Commands
        self.PayloadType = PayloadType
        self.CallbackIDs = CallbackIDs
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "task_id": self.TaskID,
            "commands": self.Commands,
            "callback_agent_id": self.CallbackAgentUUID,
            "payload_type": self.PayloadType,
            "callback_ids": self.CallbackIDs
        }


class MythicRPCCallbackAddCommandMessageResponse(SuccessMessage):
    ...


async def SendMythicRPCCallbackAddCommand(
        msg: MythicRPCCallbackAddCommandMessage) -> MythicRPCCallbackAddCommandMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_CALLBACK_ADD_COMMAND,
                                                                            body=msg.to_json())
    return MythicRPCCallbackAddCommandMessageResponse(**response)

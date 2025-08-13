import mythic_container
from mythic_container.logging import logger
from mythic_container.MythicGoRPC.messages import SuccessMessage

MYTHIC_RPC_KEYLOG_CREATE = "mythic_rpc_keylog_create"

class MythicRPCKeylogData:
    def __init__(self,
                 WindowTitle: str = None,
                 User: bool = None,
                 Keystrokes: dict = None,
                 **kwargs):
        self.WindowTitle = WindowTitle
        self.User = User
        self.Keystrokes = Keystrokes
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "window_title": self.WindowTitle,
            "user": self.User,
            "keystrokes": self.Keystrokes,
        }


class MythicRPCKeylogCreateMessage:
    def __init__(self,
                 TaskID: int,
                 Keylogs: list[MythicRPCKeylogData],
                 **kwargs):
        self.TaskID = TaskID
        self.Keylogs = Keylogs
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "task_id": self.TaskID,
            "keylogs": [x.to_json() for x in self.Keylogs]
        }


class MythicRPCKeylogCreateMessageResponse(SuccessMessage):
    ...


async def SendMythicRPCKeylogCreate(
        msg: MythicRPCKeylogCreateMessage) -> MythicRPCKeylogCreateMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_KEYLOG_CREATE,
                                                                            body=msg.to_json())
    return MythicRPCKeylogCreateMessageResponse(**response)

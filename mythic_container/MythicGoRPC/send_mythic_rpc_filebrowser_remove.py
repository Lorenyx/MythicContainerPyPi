import mythic_container
from mythic_container.logging import logger
from mythic_container.MythicGoRPC.messages import SuccessMessage

MYTHIC_RPC_FILEBROWSER_REMOVE = "mythic_rpc_filebrowser_remove"

class MythicRPCRemoveFileData:
    def __init__(self,
                 Host: str = None,
                 Path: str = None,
                 **kwargs):
        self.Host = Host
        self.Path = Path
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "host": self.Host,
            "path": self.Path
        }


class MythicRPCFileBrowserRemoveMessage:
    def __init__(self,
                 TaskID: int,
                 RemovedFiles: list[MythicRPCRemoveFileData],
                 **kwargs):
        self.TaskID = TaskID
        self.RemovedFiles = RemovedFiles
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "task_id": self.TaskID,
            "removed_files": [x.to_json() for x in self.RemovedFiles]
        }


class MythicRPCFileBrowserRemoveMessageResponse(SuccessMessage):
    ...


async def SendMythicRPCFileBrowserRemove(
        msg: MythicRPCFileBrowserRemoveMessage) -> MythicRPCFileBrowserRemoveMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_FILEBROWSER_REMOVE,
                                                                            body=msg.to_json())
    return MythicRPCFileBrowserRemoveMessageResponse(**response)

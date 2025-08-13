import mythic_container
from mythic_container.logging import logger
from mythic_container.MythicGoRPC.messages import SuccessMessage

MYTHIC_RPC_CREDENTIAL_CREATE = "mythic_rpc_credential_create"


class MythicRPCCredentialData:
    def __init__(self,
                 CredentialType: str = None,
                 Realm: str = None,
                 Account: str = None,
                 Credential: str = None,
                 Comment: str = None,
                 ExtraData: str = None,
                 **kwargs):
        self.CredentialType = CredentialType
        self.Realm = Realm
        self.Account = Account
        self.Credential = Credential
        self.Comment = Comment
        self.ExtraData = ExtraData
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")
    def to_json(self):
        return {
            "credential_type": self.CredentialType,
            "realm": self.Realm,
            "account": self.Account,
            "credential": self.Credential,
            "comment": self.Comment,
            "metadata": self.ExtraData
        }

class MythicRPCCredentialCreateMessage:
    def __init__(self,
                 TaskID: int,
                 Credentials: list[MythicRPCCredentialData] = None,
                 **kwargs):
        self.TaskID = TaskID
        self.Credentials = Credentials
        for k, v in kwargs.items():
            logger.info(f"Unknown kwarg {k} - {v}")

    def to_json(self):
        return {
            "task_id": self.TaskID,
            "credentials": [x.to_json() for x in self.Credentials],
        }


class MythicRPCCredentialCreateMessageResponse(SuccessMessage):
    ...


async def SendMythicRPCCredentialCreate(
        msg: MythicRPCCredentialCreateMessage) -> MythicRPCCredentialCreateMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_CREDENTIAL_CREATE,
                                                                            body=msg.to_json())
    return MythicRPCCredentialCreateMessageResponse(**response)

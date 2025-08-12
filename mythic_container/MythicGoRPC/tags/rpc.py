MYTHIC_RPC_TAG_CREATE = "mythic_rpc_tag_create"
MYTHIC_RPC_TAG_SEARCH = "mythic_rpc_tag_search"


async def SendMythicRPCTagSearch(
        msg: MythicRPCTagSearchMessage) -> MythicRPCTagSearchMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_TAG_SEARCH,
                                                                            body=msg.to_json())
    return MythicRPCTagSearchMessageResponse(**response)


async def SendMythicRPCTagCreate(
        msg: MythicRPCTagCreateMessage) -> MythicRPCTagCreateMessageResponse:
    response = await mythic_container.RabbitmqConnection.SendRPCDictMessage(queue=MYTHIC_RPC_TAG_CREATE,
                                                                            body=msg.to_json())
    return MythicRPCTagCreateMessageResponse(**response)
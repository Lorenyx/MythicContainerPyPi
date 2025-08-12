from dataclasses import dataclass, field

from mythic_container.deprecation import deprecated_property


@dataclass
class MythicRPCTagTypeData:

    id: int = None
    name: str = ""
    description: str = ""
    color: str = ""
    operation_id: int = None

    @property
    def ID(self) -> int:
        deprecated_property("ID", "id")
        return self.id

    @property
    def Name(self) -> str:
        deprecated_property("Name", "name")
        return self.name

    @property
    def Description(self) -> str:
        deprecated_property("Description", "description")
        return self.description

    @property
    def Color(self) -> str:
        deprecated_property("Color", "color")
        return self.color

    @property
    def OperationID(self) -> int:
        deprecated_property("OperationID", "operation_id")
        return self.operation_id


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color,
            "operation_id": self.operation_id
        }


@dataclass
class _MythicRPCTag:

    tagtype_id: int = None
    tagtype: MythicRPCTagTypeData | None = None
    data: dict = field(default_factory=dict)
    url: str = ""
    source: str = ""
    task_id: int = None
    file_id: int = None
    credential_id: int = None
    mythic_tree_id: int = None

    def __post_init__(self):
        # Initialize "tagtype" to the proper object
        if isinstance(self.tagtype, dict):
            self.tagtype = MythicRPCTagTypeData(**self.tagtype)
        # Initialize "data" to an empty dict
        if self.data is None:
            self.data = {}

    @property
    def TagTypeID(self) -> int:
        deprecated_property("TagTypeID", "tagtype_id")
        return self.tagtype_id

    @property
    def TagType(self) -> MythicRPCTagTypeData | None:
        deprecated_property("TagType", "tagtype")
        return self.tagtype

    @property
    def Data(self) -> dict:
        deprecated_property("Data", "data")
        return self.data

    @property
    def URL(self) -> str:
        deprecated_property("URL", "url")
        return self.url

    @property
    def Source(self) -> str:
        deprecated_property("Source", "source")
        return self.source

    @property
    def TaskID(self) -> int:
        deprecated_property("TaskID", "task_id")
        return self.task_id

    @property
    def FileID(self) -> int:
        deprecated_property("FileID", "file_id")
        return self.file_id

    @property
    def CredentialID(self) -> int:
        deprecated_property("CredentialID", "credential_id")
        return self.credential_id

    @property
    def MythicTreeID(self) -> int:
        deprecated_property("MythicTreeID", "mythic_tree_id")
        return self.mythic_tree_id

    def to_json(self) -> dict:
        return {
            "tagtype_id": self.tagtype_id,
            "tagtype": self.tagtype.to_json() if self.tagtype is not None else None,
            "data": self.data,
            "url": self.url,
            "source": self.source,
            "task_id": self.task_id,
            "file_id": self.file_id,
            "credential_id": self.credential_id,
            "mythic_tree_id": self.mythic_tree_id
        }


@dataclass
class MythicRPCTagCreateMessage(_MythicRPCTag):
    ...


@dataclass
class MythicRPCTagData(_MythicRPCTag):

    id: int = None

    @property
    def ID(self) -> int:
        deprecated_property("ID", "id")
        return self.id
    
    def to_json(self) -> dict:
        data = super().to_json()
        data["id"] = self.id
        return data


@dataclass
class _MythicRPCTagMessageResponse:

    success: bool = False
    error: str = ""

    @property
    def Success(self) -> bool:
        deprecated_property("Success", "success")
        return self.success

    @property
    def Error(self) -> str:
        deprecated_property("Error", "error")
        return self.error

    @property
    def Tag(self) -> int:
        deprecated_property("Tag", "tag")
        return self.tag

    def to_json(self):
        return {
            "success": self.success,
            "error": self.error
        }


@dataclass
class MythicRPCTagCreateMessageResponse(_MythicRPCTagMessageResponse):

    tag: MythicRPCTagData | None = field(default_factory=dict)

    def __post_init__(self):
        if isinstance(self.tag, dict):
            self.tag = MythicRPCTagData(**self.tag)

    @property
    def Tag(self) -> int:
        deprecated_property("Tag", "tag")
        return self.tag

    def to_json(self):
        data = super().to_json()
        data["tag"] = self.tag.to_json() if self.tag is not None else None
        return data


@dataclass
class MythicRPCTagSearchMessageResponse(_MythicRPCTagMessageResponse):

    tags: list[MythicRPCTagData] | None = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self.tags, list):
            self.tags = [MythicRPCTagData(**tag) if isinstance(tag, dict) else tag for tag in self.tags]

    @property
    def Tags(self) -> int:
        deprecated_property("Tags", "tags")
        return self.tags

    def to_json(self):
        data = super().to_json()
        data["tags"] = [tag.to_json() for tag in self.tags] if self.tags is not None else []
        return data


@dataclass
class MythicRPCTagSearchMessage:

    task_id: int
    search_tag_id: int = None
    search_tag_task_id: int = None
    search_tag_file_id: int = None
    search_tag_credential_id: int = None
    search_tag_mythictree_id: int = None
    search_tag_source: str = None
    search_tag_data: str = None
    search_tag_url: str = None

    @property
    def TaskID(self) -> int:
        deprecated_property("TaskID", "task_id")
        return self.task_id

    @property
    def SearchTagID(self) -> int:
        deprecated_property("SearchTagID", "search_tag_id")
        return self.search_tag_id

    @property
    def SearchTagTaskID(self) -> int:
        deprecated_property("SearchTagTaskID", "search_tag_task_id")
        return self.search_tag_task_id

    @property
    def SearchTagFileID(self) -> int:
        deprecated_property("SearchTagFileID", "search_tag_file_id")
        return self.search_tag_file_id

    @property
    def SearchTagCredentialID(self) -> int:
        deprecated_property("SearchTagCredentialID", "search_tag_file_id")
        return self.search_tag_file_id

    @property
    def SearchTagMythicTreeID(self) -> str:
        deprecated_property("SearchTagMythicTreeID", "search_tag_mythictree_id")
        return self.search_tag_mythictree_id

    @property
    def SearchTagSource(self) -> str:
        deprecated_property("SearchTagSource", "search_tag_source")
        return self.search_tag_source

    @property
    def SearchTagData(self) -> str:
        deprecated_property("SearchTagData", "search_tag_data")
        return self.search_tag_data

    @property
    def SearchTagURL(self) -> str:
        deprecated_property("SearchTagURL", "search_tag_url")
        return self.search_tag_url

    def to_json(self):
        return {
            "task_id": self.task_id,
            "search_tag_id": self.search_tag_id,
            "search_tag_task_id": self.search_tag_task_id,
            "search_tag_file_id": self.search_tag_file_id,
            "search_tag_credential_id": self.search_tag_credential_id,
            "search_tag_mythictree_id": self.SearchTagMythicTreeID,
            "search_tag_source": self.search_tag_source,
            "search_tag_data": self.search_tag_data,
            "search_tag_url": self.search_tag_url
        }

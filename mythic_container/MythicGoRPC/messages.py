from dataclasses import dataclass

from mythic_container.deprecation import deprecated_property


@dataclass
class SuccessMessage:
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

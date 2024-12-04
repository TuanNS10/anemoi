from dataclasses import dataclass
from typing import Dict, Any

class File:
    def __init__(self, filename: Any):
        self.filename = filename

@dataclass(frozen=True)
class FileData:
    file: File
    file_name: str
    metadata: Dict[str, Any]

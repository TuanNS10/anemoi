from dataclasses import dataclass
from typing import Dict, Any
import io

@dataclass(frozen=True)
class FileResponseData:
    file_content: io.BytesIO 
    content_type: str
    metadata: Dict[str, str]
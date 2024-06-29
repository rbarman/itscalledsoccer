from pydantic import BaseModel, RootModel
from typing import List, Optional

class Manager(BaseModel):
    manager_id: str
    manager_name: Optional[str] = None
    nationality: Optional[str] = None

class Managers(RootModel):
    root: List[Manager]
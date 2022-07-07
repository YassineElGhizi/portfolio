from typing import Optional, List
from pydantic import BaseModel


class contact(BaseModel):
    name: str
    email: str
    subject: Optional[str]
    message: str

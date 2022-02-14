from typing import Optional

from pydantic import BaseModel


class BaseData(BaseModel):
    eTag: Optional[dict] = None

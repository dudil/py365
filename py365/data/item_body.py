from pydantic import BaseModel

from py365.enums import BodyType


class ItemBody(BaseModel):
    content: str = None
    contentType: BodyType = BodyType.HTML

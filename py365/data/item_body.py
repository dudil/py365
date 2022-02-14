from py365.enums import BodyType
from .base_data import BaseData


class ItemBody(BaseData):
    content: str = None
    contentType: BodyType = BodyType.HTML

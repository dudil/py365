import attr

from py365.enums import BodyType

from .base_data import BaseData


@attr.s(auto_attribs=True)
class ItemBody(BaseData):
    content: str = None
    contentType: BodyType = BodyType.HTML

from py365.enums import BodyType

from ._base_resource import BaseResource


class ItemBody(BaseResource):
    def __init__(self, content: str, contentType: BodyType = BodyType.HTML):
        self.content = content
        self.contentType = contentType
        BaseResource.__init__(self)


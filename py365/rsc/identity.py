# Resource documentation
# https://docs.microsoft.com/en-us/graph/api/resources/identity?view=graph-rest-1.0
from ._base_resource import BaseResource


class Identity(BaseResource):

    def __init__(self):
        self.displayName: str = None
        self.id = None
        BaseResource.__init__(self)

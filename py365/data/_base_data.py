import attr

from datetime import datetime
from enum import Enum

from py365.utils import datetimeFromStr, datetimeToStr


@attr.s
class BaseData:
    """
    Represent a base data on the OG
    Every OG data class should inherit from this class
    """

    @staticmethod
    def jsonVal(val: any) -> any:
        if val:
            if isinstance(val, BaseData):
                return val.json
            elif isinstance(val, Enum):
                return val.value
            elif isinstance(val, list):
                retList = []
                for i in val:
                    retItem = BaseData.jsonVal(i)
                    retList.append(retItem)
                return retList
            elif isinstance(val, datetime):
                return datetimeToStr(val)
            else:
                return val
        else:
            return val

    @property
    def json(self):
        """
        convert the resource into payload for the Open Graph365 API call
        """
        data = self.__dict__
        ret: dict = {}
        for key, val in data.items():
            if val:
                payloadVal = BaseData.jsonVal(val)
                ret.update({key: payloadVal})

        return ret

    def fromResponse(self, data: dict):
        attributes = attr.fields_dict(self.__class__)

        for attrName, attrAttributes in attributes.items():
            dataVal = data.get(attrName, None)
            val = dataVal
            if dataVal is None:
                continue
            elif isinstance(attrAttributes.type, BaseData):
                val.fromResponse(data=dataVal)
            elif isinstance(attrAttributes.type, datetime):
                val = datetimeFromStr(datetimeStr=dataVal)

            setattr(self, attrName, val)

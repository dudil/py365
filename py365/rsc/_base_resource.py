from enum import Enum


class BaseResource(object):
    """
    Represent a base resource on the OG
    Every OG resource class should inherit from this class
    """

    @staticmethod
    def payloadValue(val: any) -> any:
        if val is not None:
            if isinstance(val, BaseResource):
                return val.payload
            elif isinstance(val, Enum):
                return val.value
            elif isinstance(val, list):
                payloadList = []
                for i in val:
                    payloadItem = BaseResource.payloadValue(i)
                    payloadList.append(payloadItem)
                return payloadList
            else:
                return val
        else:
            return val

    @property
    def payload(self) -> dict:
        """
        convert the resource into payload for the Open Graph365 API call
        """
        data = vars(self)
        payload: dict = {}
        for key, val in data.items():
            if val is not None:
                payloadVal = BaseResource.payloadValue(val)
                payload.update({key: payloadVal})

        return payload


#utility function to add a new parameter to the payload only if it is already exist
def addPayloadParam(payload: dict, key: str, value: any):
        payload.update({key: value} if value else {})
        return payload

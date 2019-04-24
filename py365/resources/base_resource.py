class BaseResource(object):
    """
    Represent a base resource on the OG
    Every OG resource class should inherit from this class
    """

    def __init__( self ):
        pass

    def payload( self ) -> dict:
        """
        convert the resource into payload for the Open Graph
        """
        data = vars(self)
        payload: dict = {}
        for key, val in data.items():
            if val is not None:
                if isinstance(val, BaseResource):
                    payload.update({key: val.payload()})
                else:
                    payload.update({key: val})

        return payload

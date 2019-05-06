from datetime import datetime

_DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%SZ%Z"


def datetimeFromStr(datetimeStr: str) -> datetime:
    return datetime.strptime(datetimeStr
                             , _DATETIME_FORMAT)


def datetimeToStr(dateObj: datetime) -> str:
    return dateObj.strftime(_DATETIME_FORMAT)

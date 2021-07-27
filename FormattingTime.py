import time


def TimeStampToStandardFormat(TimeStamp):
    """

    :param TimeStamp: 时间戳
    :return: "%Y-%m-%d %H:%M:%S" 标准格式时间
    """
    TimeStamp = int(TimeStamp)
    timeArray = time.localtime(TimeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def StandardFormatToTimeStamp(dt):
    """

    :param dt: For example:dt = "2016-05-05 20:28:54"
    :return: timestamp
    """
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return timestamp

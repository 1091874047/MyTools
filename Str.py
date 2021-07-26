def StrGetLeft(text, findStr):
    """

    :param text: 文本
    :param findStr: 要查找的字符串
    :return: 返回findStr左边的字符串
    """
    text = text.replace('\r', "")
    text = text.replace('\n', "")
    text = text.replace('\t', "")

    try:
        n = str.index(text, findStr)
        return text[:n]
    except ValueError:
        return None


def StrGetRight(text, findStr):
    """

    :param text: 文本
    :param findStr: 要查找的字符串
    :return: 返回findStr右边的字符串
    """
    text = text.replace('\r', "")
    text = text.replace('\n', "")
    text = text.replace('\t', "")
    try:
        n = str.index(text, findStr) + len(findStr)
        return text[n:]
    except ValueError:
        return None


def StrGetSub(text, first, last):
    """

    :param text: 文本
    :param first: 要查找的字符串左边的字符
    :param last:    要查找的字符串右边的字符
    :return:    中间的字符
    """
    text = text.replace('\r', "")
    text = text.replace('\n', "")
    text = text.replace('\t', "")

    try:
        firstIndex = str.index(text, first)

        if firstIndex == -1:
            return None
        firstIndex = str.index(text, first) + len(first)
        lastIndex = str.index(text[firstIndex:], last) + firstIndex
        if firstIndex >= lastIndex:
            return None
        while True:
            if lastIndex <= firstIndex:
                text = text.replace(last, "", -1)
                firstIndex = str.index(text, first) + len(first)
                lastIndex = str.index(text, last)
            else:
                break
        return text[firstIndex:lastIndex]
    except ValueError:
        return None


def StrGetSubBatch(text, first, last):
    """
    循环遍历text,一直取到TypeError报错为止
    :param text:
    :param first:
    :param last:
    :return:
    """
    res = []
    while True:
        temp = StrGetSub(text, first, last)
        try:
            text = text.replace(first + temp + last, "", -1)
            if temp is None:
                return res
            else:
                res.append(temp)
        except TypeError:
            return res


def StrToHeadersDict(text):
    """

    :param text: Triple quoted string
    :return: headers struct
    """
    HeadersDict = {}
    StrList = text.split("\n")
    for single in StrList:
        res = single.split(": ")
        if res != ['']:
            HeadersDict[res[0]] = res[1]
    return HeadersDict


def CookieJarToStr(Cookiejar):
    """
    :param Cookiejar: CookieList
    :return: CookieStr
    """
    Cookie = ""
    for Cookies in Cookiejar:
        Cookie += Cookies['name'] + '=' + Cookies['value'] + '; '
    return Cookie

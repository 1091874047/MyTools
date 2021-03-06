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
    if text:
        HeadersDict = {}
        StrList = text.split("\n")
        for single in StrList:
            header = single.split(": ")
            if len(header) <= 1:
                continue
            if header[0] != [''] and "Content-Length" not in header[0] and "Cookie" not in header[0]:
                HeadersDict[header[0].strip()] = header[1]
        return HeadersDict
    return


def CookieJarToStr(Cookiejar):
    """
    :param Cookiejar: CookieList 程序响应后的 res.cookies options:List[Dict{name:str,value:str},Dict{name:str,value:str}]
    :return: CookieStr
    """
    Cookie = ""
    for Cookies in Cookiejar:
        Cookie += Cookies['name'] + '=' + Cookies['value'] + '; '
    return Cookie


def StrToDataDict(text):
    """
    将Fiddler复制的数据转化为 K,V 键值对
    For example: q=1&n=2
    return:  DataDict={'q':1,'n':2}
    text 数据来源 fiddler -> 会话详细 -> 数据（post类型）
    用法一：
            text = "j_username=abcdefg&j_password=B%40Tabd4ea2b4e7b242b6d48bf6ccec90751&kaptcha=scsd&isForceLogin=1"
            data = StrToData(text)
    用法二：
            n = 1245678
            text = f"j_username={n}&j_password=B%40Tabd4ea2b4e7b242b6d48bf6ccec90751&kaptcha=scsd&isForceLogin=1"
            data = StrToData(text)
    此方法数据转换后全部为str
    若要对数据进行更新：
    或者数据类型必须为指定类型:
                使用 DataDict.update({ K : n })即可
    """
    if text:
        DataDict = {}
        dataStrList = text.split("&")
        for data in dataStrList:
            res = data.split("=")
            if res:
                DataDict.update({res[0]: res[1]})
        return DataDict
    return


# 快速排序用法
def QuickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        QuickSort(arr, left, partitionIndex - 1)
        QuickSort(arr, partitionIndex + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def CookieTOCookieJar(cookie):
    if cookie != "":
        CookieJar = []
        Cookiestr = cookie.split(";")
        for i in Cookiestr:
            c={}
            CookieItem = i.split("=")
            c['name']=CookieItem[0]
            c['value']=CookieItem[1]
            CookieJar.append(c)
        return CookieJar

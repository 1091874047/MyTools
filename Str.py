html = """
今天，微软又放出了后续主题“Bing's Best 2”。虽然没有新的系统声音和屏幕保护，窗口颜色也只是简单的白色，但提供了多达21张壁纸，涵盖世界各地自然风情和一些动物，其中不乏精品，想要自己的电脑更个性化的话不妨下载看看……
"""

def StrGetLeft(text, findStr):
    """

    :param text: 文本
    :param findStr: 要查找的字符串
    :return: 返回findStr左边的字符串
    """
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
                text = text.replace(last, "", 1)
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
            text = text.replace(first + temp + last, "", 1)
            if temp is None:
                break
            else:
                res.append(temp)
        except TypeError:
            return res

# r = StrGetSubBatch(html3, '<a target="_top" title="', '" ')
# print(r)

html = """
今天，微软又放出了后续主题“Bing's Best 2”。虽然没有新的系统声音和屏幕保护，窗口颜色也只是简单的白色，但提供了多达21张壁纸，涵盖世界各地自然风情和一些动物，其中不乏精品，想要自己的电脑更个性化的话不妨下载看看……
"""

html2 = """
1234567 1238567
"""
html3 = """
<div class="design" id="leftcolumn">
						<a target="_top" title="Python 基础教程" href="/python/python-tutorial.html">
			Python 基础教程			</a>
						<a target="_top" title="Python 简介" href="/python/python-intro.html">
			Python 简介			</a>
						<a target="_top" title="Python 环境搭建" href="/python/python-install.html">
			Python 环境搭建			</a>
			<a target="_top" title="Python 中文编码" href="python-chinese-encoding.html"> Python 中文编码 </a>			<a target="_top" title="Python 基础语法" href="/python/python-basic-syntax.html">
			Python 基础语法			</a>
						<a target="_top" title="Python 变量类型" href="/python/python-variable-types.html">
			Python 变量类型			</a>
						<a target="_top" title="Python 运算符" href="/python/python-operators.html">
			Python 运算符			</a>
						<a target="_top" title="Python 条件语句" href="/python/python-if-statement.html">
			Python 条件语句			</a>
						<a target="_top" title="Python 循环语句" href="/python/python-loops.html">
			Python 循环语句			</a>
						<a target="_top" title="Python While 循环语句" href="/python/python-while-loop.html">
			Python While 循环语句			</a>
						<a target="_top" title="Python for 循环语句" href="/python/python-for-loop.html">
			Python for 循环语句			</a>
						<a target="_top" title="Python 循环嵌套" href="/python/python-nested-loops.html">
			Python 循环嵌套			</a>
						<a target="_top" title="Python break 语句" href="/python/python-break-statement.html">
			Python break 语句			</a>
						<a target="_top" title="Python continue  语句" href="/python/python-continue-statement.html">
			Python continue  语句			</a>
						<a target="_top" title="Python pass 语句" href="/python/python-pass-statement.html">
			Python pass 语句			</a>
						<a target="_top" title="Python Number(数字)" href="/python/python-numbers.html">
			Python Number(数字)			</a>
						<a target="_top" title="Python 字符串" href="/python/python-strings.html" style="background-color: rgb(150, 185, 125); font-weight: bold; color: rgb(255, 255, 255);">
			Python 字符串			</a>
						<a target="_top" title="Python 列表(List)" href="/python/python-lists.html">
			Python 列表(List)			</a>
						<a target="_top" title="Python 元组" href="/python/python-tuples.html">
			Python 元组			</a>
						<a target="_top" title="Python 字典(Dictionary)" href="/python/python-dictionary.html">
			Python 字典(Dictionary)			</a>
						<a target="_top" title="Python 日期和时间" href="/python/python-date-time.html">
			Python 日期和时间			</a>
						<a target="_top" title="Python 函数" href="/python/python-functions.html">
			Python 函数			</a>
						<a target="_top" title="Python 模块" href="/python/python-modules.html">
			Python 模块			</a>
						<a target="_top" title="Python 文件I/O" href="/python/python-files-io.html">
			Python 文件I/O			</a>
			<a target="_top" title="Python File 方法" href="file-methods.html">Python File 方法</a>			<a target="_top" title="Python 异常处理" href="/python/python-exceptions.html">
			Python 异常处理			</a>
			<a target="_top" title="Python OS 文件/目录方法" href="os-file-methods.html">Python OS 文件/目录方法</a>
<a target="_top" title="Python 内置函数" href="python-built-in-functions.html">Python 内置函数</a>
<br><h2 class="left"><span class="left_h2">Python</span> 高级教程</h2>			<a target="_top" title="Python 面向对象" href="/python/python-object.html">
			Python 面向对象			</a>
						<a target="_top" title="Python 正则表达式" href="/python/python-reg-expressions.html">
			Python 正则表达式			</a>
						<a target="_top" title="Python CGI 编程" href="/python/python-cgi.html">
			Python CGI 编程			</a>
						<a target="_top" title="Python 操作 MySQL 数据库" href="/python/python-mysql.html">
			Python MySQL			</a>
			<a target="_top" title="Python 网络编程" href="python-socket.html"> Python 网络编程 </a>			<a target="_top" title="Python SMTP发送邮件" href="/python/python-email.html">
			Python SMTP			</a>
						<a target="_top" title="Python 多线程" href="/python/python-multithreading.html">
			Python 多线程			</a>
						<a target="_top" title="Python XML 解析" href="/python/python-xml.html">
			Python XML 解析			</a>
						<a target="_top" title="Python GUI 编程(Tkinter)" href="/python/python-gui-tkinter.html">
			Python GUI 编程(Tkinter)			</a>
						<a target="_top" title="Python2.x 与 3​​.x 版本区别" href="/python/python-2x-3x.html">
			Python2.x 与 3​​.x 版本区别			</a>
						<a target="_top" title="Python IDE" href="/python/python-ide.html">
			Python IDE			</a>
						<a target="_top" title="Python JSON" href="/python/python-json.html">
			Python JSON			</a>
						<a target="_top" title="Python 100例" href="/python/python-100-examples.html">
			Python 100例			</a>
			<a target="_blank" title="Python 测验" href="/quiz/python-quiz.html"> Python 测验 </a>	
		</div>"""


def StrGetLeft(text, findStr):
    """

    :param text: 文本
    :param findStr: 要查找的字符串
    :return: 返回findStr左边的字符串
    """
    n = str.index(text, findStr)
    if n == -1:
        return None
    return text[:n]


# r = StrGetLeft(html, "保护")
# print(r)

def StrGetRight(text, findStr):
    """

    :param text: 文本
    :param findStr: 要查找的字符串
    :return: 返回findStr右边的字符串
    """
    n = str.index(text, findStr) + len(findStr)
    if n == -1:
        return None
    return text[n:]


# r=StrGetRight(html,"保护")
# print(r)

def StrGetSub(text, first, last):
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


#
# r = StrGetSub(html, "新的", "保护")
# print(r)
def StrGetSubBatch(text, first, last):
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


r = StrGetSubBatch(html3, '<a target="_top" title="', '" ')
print(r)

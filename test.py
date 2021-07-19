import http.client


class BuildRequest:
    def __init__(self, url=None, Mode=None, DataStr=None, Headers=None):
        self.param = {}
        self.Url: str = url
        self.Mode: str = Mode
        self.DataStr: str = DataStr
        self.Headers: str = Headers
        self.RetHeaders = http.client.HTTPResponse.headers

    def add_param(self):
        pass

    def HttpSend(self):
        pass

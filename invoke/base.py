import re
from urllib.parse import urlparse

import requests
from requests import RequestException

from invoke.exceptions import PrefixError, FormatError, RequestError

URL_RE = re.compile(
    r'^(?:[a-z0-9\.\-]*)://'  # scheme is validated separately
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}(?<!-)\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

PREFIX_RE = re.compile("^[A-Z]_[A-Z]{1,20}_")


class ServiceInvoke(object):
    """
    _prefix = "F_EMAIL_"
    """
    _prefix = None

    """
        关于地址分开的写法，觉得有点麻烦，所以这里重新改写成一个参数
    """

    _addr = None

    _version = "0.0.1"  # 关于版本现在不用

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    @property
    def prefix(self):
        return self._prefix

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, url):
        """
        格式: http[s]://ip:port[/]

        不做地址和端口号的验证
        :param url:
        :return:
        """
        parse_rs = urlparse(url)
        scheme = parse_rs.scheme
        netloc = parse_rs.netloc
        self._addr = "{}://{}".format(scheme, netloc)
        # 这进行统一判断，减少判断流程
        if not URL_RE.match(self._addr):
            raise FormatError

    def init_app(self, app):
        """
        传入app对象
        :param app:
        :return:

        F_EMAIL_ADDR = ..


        """
        if self._prefix is None:
            raise PrefixError
        cfg = app.config
        for _cfg in cfg:
            if PREFIX_RE.match(_cfg):
                self.addr = cfg[_cfg]
                break

    def update_from_finder(self, finder):
        """

        :param finder:
        :return:

        获得地址: http://...:80[/]
        self.host =
        self.port =
        """
        addr = finder.get(self.prefix).get('message')
        if addr:
            self.addr = addr

    def send_request(self, method, url, retry=3, **kwargs):
        """
            发送三次重试请求，限制超时时间3s.
        """
        url = self.addr + url
        try:
            return requests.request(method=method, url=url, timeout=3, **kwargs).json()
        except RequestException:
            retry -= 1
            if retry == 0:
                return RequestError().to_dict()
            self.send_request(method, url, retry=retry, **kwargs)

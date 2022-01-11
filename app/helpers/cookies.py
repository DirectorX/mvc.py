# Author: DirectorX

from app.config import web
from app.helpers import Helper
from app.helpers import HelperException


class CookieManager(Helper):
    _COOKIE_MAX_AGE = 0xffffff

    @staticmethod
    def load_cookie(cookie_name):
        cookies = CookieManager.web.cookies()
        try:
            return cookies[cookie_name]
        except Exception as e:
            raise CookieManagerException(e)

    @staticmethod
    def set_cookie(cookie_name, data, age=None):
        if not age:
            age = CookieManager._COOKIE_MAX_AGE
        try:
            CookieManager.web.setcookie(cookie_name, data, age)
        except Exception as e:
            raise CookieManagerException(e)

    @staticmethod
    def delete_cookie(spec_cookie='user'):
        try:
            CookieManager.web.setcookie(spec_cookie, None, 0x0)
        except Exception as e:
            raise CookieManagerException(e)


class CookieManagerException(HelperException):
    pass

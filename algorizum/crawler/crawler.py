# -*- coding: utf8 -*-

import time
import requests

from parser import Parser
from rules import *


class AlgorizumCrawler(object):
    def __init__(self, parsing_rules, _url='', delay=3):
        """
            매너 있게 delay를 지켜주자 (단위는 seconds)

            :param parsing_rules: dictionary
            :param _url : string
            :param delay : integer
        """

        self.__url = _url
        self.__user = ''

        self.delay = delay
        self.parser = Parser(rules=parsing_rules)

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, _url):
        if not isinstance(_url, str):
            raise TypeError("main_url must be str type not %s" % type(_url))

        self.__url = _url

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, _user):
        if not isinstance(_user, (str, list)):
            raise TypeError("main_url must be str type not %s" % type(_user))

        self.__user = [_user] if isinstance(_user, str) else _user

    def _download_url(self):

        total_user_count = len(self.__user)

        # key: user_id, value: html
        result_dict = dict()

        for idx, user_id in enumerate(self.__user, 1):
            down_url = Urls.normalize_user_url(self.__url, user_id=user_id)
            response = requests.get(down_url)
            result_dict[user_id] = response.content

            if idx == total_user_count:
                break
            time.sleep(self.delay)

        return result_dict

    def crawl(self):

        result_dict = dict()
        html_dict = self._download_url()

        for user_id, html in html_dict.items():
            user_result = dict()
            parsing_result = self.parser.parse(html)
            user_result[AlgorizumRules.recent_published_date] = DateTimeText.normalize_datetime(
                parsing_result[AlgorizumRules.recent_published_date])
            result_dict[user_id] = user_result

        return result_dict

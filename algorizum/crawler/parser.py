# -*- coding:utf8 -*-

import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from rules import DateTimeText


class Parser(object):
    def __init__(self, rules):
        """

        :param rules: dictionary
        """

        # rules exampled
        # {'div': {'my_key': 'value'}}
        #

        self.rules = rules

    @staticmethod
    def parse_datetime(text):
        """

        :param text: string
        :return: datetime
        """

        today = datetime.today()

        for match, val in DateTimeText.match_text.items():
            result = re.match(match, text)
            if result is not None:
                delta = int(result.group(1)) * val
                break
        else:
            raise ValueError("Unknown pattern text %s" % text)

        return today + timedelta(seconds=delta)

    def parse(self, html):
        result_dict = {}

        soup = BeautifulSoup(html, "html.parser")
        for rule in self.rules:
            if rule == 'class':
                for key, val in self.rules[rule].items():
                    count = 0
                    if "[" in val and "]" in val:
                        val, count = val.split("[")
                        count = int(count.strip("[]"))
                    result = soup.find_all(class_=val)
                    for idx, res in enumerate(result):
                        if idx == count:
                            result_dict[key] = res.contents[0].text.encode('utf-8')
                            break
        return result_dict

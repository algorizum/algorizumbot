# -*- coding:utf8 -*-

from bs4 import BeautifulSoup


class Parser(object):
    def __init__(self, rules):
        """

        :param rules: dictionary
        """

        # rules exampled
        # {'div': {'my_key': 'value'}}
        #

        self.rules = rules

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

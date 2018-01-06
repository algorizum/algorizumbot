# -*- coding: utf8 -*-

# rules for this crawler
# 1. parentheses(or brackets) do not use on parameters

import re
from datetime import datetime, timedelta


class AlgorizumRules(object):
    recent_published_date = 'recent_published_date'


class Urls(object):
    def __init__(self):
        pass

    @staticmethod
    def normalize_user_url(url, user_id):
        return url.replace("(USER_ID)", user_id)


class DateTimeText(object):
    match_text = {r'(\d{0,})일 전': -1, r'(\d{0,})달 전': -30}

    @classmethod
    def normalize_datetime(cls, text):
        """

        :param text: string
        :return: datetime
        """

        today = datetime.today()
        delta = 0

        for match, val in cls.match_text.items():
            result = re.match(match, text)
            if result is not None:
                delta = int(result.group(1)) * val
                break

        return today + timedelta(delta)

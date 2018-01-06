# -*- coding: utf8 -*-

# rules for this crawler
# 1. parentheses(or brackets) do not use on parameters

import re
from datetime import datetime, timedelta

from config import Date


class AlgorizumRules(object):
    recent_published_date = 'recent_published_date'


class Urls(object):
    def __init__(self):
        pass

    @staticmethod
    def normalize_user_url(url, user_id):
        return url.replace("(USER_ID)", user_id)


class DateTimeText(object):
    # value seconds
    match_text = {r'(\d{0,})초 전': -Date.SECOND,
                  r'(\d{0,})분 전': -Date.MINUTE,
                  r'(\d{0,})시간 전': -Date.HOUR,
                  r'(\d{0,})일 전': -Date.DAY,
                  r'(\d{0,})달 전': -Date.MONTH,
                  r'(\d{0,})년 전': -Date.YEAR}

    @classmethod
    def normalize_datetime(cls, text):
        """

        :param text: string
        :return: datetime
        """

        today = datetime.today()

        for match, val in cls.match_text.items():
            result = re.match(match, text)
            if result is not None:
                delta = int(result.group(1)) * val
                break
        else:
            raise ValueError("Unknown pattern text %s" % text)

        return today + timedelta(seconds=delta)

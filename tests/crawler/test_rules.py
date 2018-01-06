# -*- coding: utf8 -*-

import unittest
from datetime import datetime, timedelta

from config import Date
from crawler.rules import DateTimeText


class TestDateTimeText(unittest.TestCase):
    def test_normalize_datetime(self):
        today = datetime.today()

        self.assertEqual((today - timedelta(seconds=Date.DAY)).strftime("%Y%m%d"),
                         DateTimeText.normalize_datetime("1일 전").strftime("%Y%m%d"))
        self.assertEqual((today - timedelta(seconds=Date.MINUTE)).strftime("%Y%m%d"),
                         DateTimeText.normalize_datetime("1분 전").strftime("%Y%m%d"))
        self.assertEqual((today - 32 * timedelta(seconds=Date.MINUTE)).strftime("%Y%m%d"),
                         DateTimeText.normalize_datetime("32분 전").strftime("%Y%m%d"))
        self.assertEqual((today - timedelta(seconds=Date.HOUR)).strftime("%Y%m%d"),
                         DateTimeText.normalize_datetime("1시간 전").strftime("%Y%m%d"))
        self.assertEqual((today - 5 * timedelta(seconds=Date.YEAR)).strftime("%Y%m%d"),
                         DateTimeText.normalize_datetime("5년 전").strftime("%Y%m%d"))

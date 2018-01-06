# -*- coding: utf8 -*-

import unittest
from datetime import datetime, timedelta

from crawler.rules import DateTimeText


class TestDateTimeText(unittest.TestCase):
    def test_normalize_datetime(self):
        yesterday = datetime.today() - timedelta(1)
        self.assertEqual(yesterday, DateTimeText.normalize_datetime("1일 전"))

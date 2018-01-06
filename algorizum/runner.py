# -*- coding: utf8 -*-

from datetime import datetime

from crawler.crawler import AlgorizumCrawler
from crawler.rules import AlgorizumRules


def test():
    algospot_user = ["홍시"]
    algospot_rules = {'class': {AlgorizumRules.recent_published_date: 'submitted_on[1]'}}

    algospot_crawler = AlgorizumCrawler(parsing_rules=algospot_rules)
    algospot_crawler.url = 'https://algospot.com/judge/submission/recent/?user=(USER_ID)'
    algospot_crawler.user = algospot_user

    result = algospot_crawler.crawl()
    today = datetime.today()

    for user in algospot_user:
        user_recent_published_date = result[user][AlgorizumRules.recent_published_date]
        if today != user_recent_published_date:
            print "no result", user, 'recent published', user_recent_published_date.strftime("%Y년 %m월 %d일 %H시 %M분")


if __name__ == "__main__":
    test()

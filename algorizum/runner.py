# -*- coding: utf8 -*-

from crawler.crawler import AlgorizumCrawler
from crawler.rules import AlgorizumRules


def test():
    algospot_rules = {'class': {AlgorizumRules.recent_published_date: 'submitted_on[1]'}}

    algospot_crawler = AlgorizumCrawler(parsing_rules=algospot_rules)
    algospot_crawler.url = 'https://algospot.com/judge/submission/recent/?user=(USER_ID)'
    algospot_crawler.user = '홍시'

    result = algospot_crawler.crawl()
    print result['홍시']


if __name__ == "__main__":
    test()

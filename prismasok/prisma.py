from datetime import datetime
from decimal import Decimal

import requests
from bs4 import BeautifulSoup


class Prisma:
    DOMAIN = 'http://www.sok-ru.tx.fi'
    ENCODING = 'cp1251'

    LOGIN_URI = '/service.cntum?pageId=158302&Pid=logIn'

    ITEMS_TABLE_CLASS = 'ostotapahtuma'

    PURCHASES_URI = '/service.cntum?pageId=158306'
    PURCHASES_DATE_FORMAT = '%d.%m.%Y'

    TOTAL_URI = '/ajax2?Pid=expand&summary&date={startDate}&date2={endDate}'
    TOTAL_DATE_FORMAT = '%Y%m%d'

    def __init__(self, cardNum, password):
        self.s = requests.Session()

        r = self.s.post(self.DOMAIN + self.LOGIN_URI,
                        data={'CardNum': cardNum, 'Password': password}, timeout=5)
        if r.url == self.DOMAIN + self.LOGIN_URI:
            raise ValueError('Failed to authenticate')

    def purchases(self, startDate, endDate=None):
        if endDate is None:
            endDate = startDate

        r = self.s.post(self.DOMAIN + self.PURCHASES_URI,
                        data={'startDate': startDate.strftime(self.PURCHASES_DATE_FORMAT), 'endDate': endDate.strftime(self.PURCHASES_DATE_FORMAT)}, timeout=5)
        soup = BeautifulSoup(r.text, from_encoding=self.ENCODING)

        tables = soup('table', self.ITEMS_TABLE_CLASS)
        rows = [r for t in tables for r in t('tr')[1:]]
        return [Purchase.from_row(self, row) for row in rows[:-1]]

    def total_items(self, startDate, endDate):
        return Items(self, self.TOTAL_URI.format(startDate=startDate.strftime(self.TOTAL_DATE_FORMAT), endDate=endDate.strftime(self.TOTAL_DATE_FORMAT)))


class Purchase:
    def __init__(self, prisma, items_uri, date, total):
        self._prisma = prisma
        self._items_uri = items_uri
        self._date = date
        self._total = total

        self._items = None  # cache

    @classmethod
    def from_row(cls, prisma, row):
        u, d, t, _ = row('td')
        return cls(prisma, u.a['href'], datetime.strptime(d.text, prisma.PURCHASES_DATE_FORMAT).date(), Decimal(t.text.replace(',', '')))

    def __repr__(self):
        return '<Purchase date={}, total={}>'.format(self.date, self.total)

    @property
    def date(self):
        return self._date

    @property
    def total(self):
        return self._total

    @property
    def items(self):
        if self._items is None:
            self._items = Items(self._prisma, self._items_uri)
        return self._items


class Items:
    def __init__(self, prisma, uri):
        self._prisma = prisma

        r = prisma.s.get(prisma.DOMAIN + uri, timeout=5)
        soup = BeautifulSoup(r.text, from_encoding=prisma.ENCODING)

        rows = soup('tr')
        items = [(n.text.strip(), Decimal(v.text.replace(',', ''))) for n, _, v, _ in [r('td') for r in rows]]
        self._data = items

    @property
    def data(self):
        return self._data

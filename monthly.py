#!/usr/bin/env python3

from datetime import date, timedelta
import calendar

from notifier import init
from notifier.providers import EmailNotify
from prismasok import prisma
from prismasok.util import load_credentials, sorted_items, print_items, total


today = date.today()
last_month = date(today.year, today.month, 1) - timedelta(days=1)
month, year = last_month.month, last_month.year
last_day = calendar.monthrange(year, month)[1]

cardno, password = load_credentials()
p = prisma.Prisma(cardno, password)

items = sorted_items(p.total_items(date(year, month, 1), date(year, month, last_day)).data)

n = init(email=EmailNotify('Prisma'))
with n:
    t = total(items)
    n.subject = 'Prisma: {} rub spent in {}'.format(t, calendar.month_name[month])
    print_items(items)
    print('Total: {}'.format(t))
n.notify()

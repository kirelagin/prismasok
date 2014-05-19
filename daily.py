#!/usr/bin/env python3

from datetime import date, timedelta

from notifier import init, plural
from notifier.providers import EmailNotify
from prismasok import prisma
from prismasok.util import load_credentials, sorted_items, print_items, total


cardno, password = load_credentials()
p = prisma.Prisma(cardno, password)
ps = p.purchases(date.today() - timedelta(days=1))

if len(ps) > 0:
    n = init(email=EmailNotify('Prisma'))
    with n:
        n.subject = 'Prisma: {} purchase{s} yesterday'.format(len(ps), s=plural(len(ps)))
        for i, p in enumerate(ps, 1):
            data = sorted_items(p.items.data)
            print('Purchase #{}:'.format(i))
            print_items(data)
            print('Total: {}'.format(p.total))
            real_total = total(data)
            if (real_total != p.total):
                print('Real total: {}'.format(real_total))
            print()
    n.notify()

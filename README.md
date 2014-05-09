Prisma Python API
==================

This library lets you grab your purchases information from [Prisma][prisma], a Russian-Finnish retailer.

It uses [Russian Prisma club][club] website, but it might work in other countries if they run
the same CMS.


API
----

API documentation TBD.

But you can check shipped scripts and sources. Everything is pretty straightforward.


Shipped scripts
----------------

### `daily.py`

`daily.py` gathers information about purchases during the day.

~~~~~~~~ShellSession
% ./daily.py  
[Prisma: 1 purchase today]

Purchase #1:
-----------------------------------
масло, маргарин, соусы       199.90
молоко и сливки               97.80
туалетная бумага              89.10
корнеплоды                    68.85
кисломолочные продукты        45.20
десертные молочные продукты   34.90
===================================
Total: 535.75
~~~~~~~~~

`./daily.py email` will send you an email and is designed to be run by cron in the evening.

### `monthly.py`

`monthly.py` summarises all the purchases during the _previous_ month.

`./monthly.py email` will send you an email and is designed to be run by cron on the first night of every month.


Requirements
-------------

### API:

* [Requests](http://python-requests.org/) for HTTP
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) for HTML parsing

### Shipped scripts:

* [pyxdg](https://freedesktop.org/www/Software/pyxdg/) for configuration
* [pynotifier](https://github.com/kirelagin/pynotifier) for output


 [prisma]:  http://prismamarket.ru/
 [club]:    http://www.sok-ru.tx.fi/

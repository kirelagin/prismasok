#!/usr/bin/env python3

from distutils.core import setup


setup(name='prismasok',
      version='0.1',

      description='Prisma Python API',
      long_description='''
          This library lets you grab your purchases information from Prisma_,
          a Russian-Finnish retailer.

          See README_ for more details.

          .. _Prisma: http://prismamarket.ru/
          .. _README: https://github.com/kirelagin/prismasok/blob/master/README.md
          ''',


      author='Kirill Elagin',
      author_email='kirelagin@gmail.com',

      url='https://github.com/kirelagin/prismasok',

      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'Intended Audience :: End Users/Desktop',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: Unix',
                     'Programming Language :: Python :: 3',
                     'Topic :: Office/Business :: Financial :: Accounting',
                     'Topic :: Software Development :: Libraries',
                    ],
      keywords = ['Prisma', 'Sok', 'API', 'purchases'],

      packages=['prismasok'],
      scripts=['daily.py', 'monthly.py'],

      requires=['requests', 'BeautifulSoup', 'pyxdg', 'notifier'],
     )

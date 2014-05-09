import xdg.BaseDirectory as xdgb


def load_credentials():
    p = xdgb.load_first_config('prisma', 'credentials')
    if p is None:
        exit('Please save your card number and password (each on its own line) in {}/credentials'
              .format(xdgb.save_config_path('prisma')))
    with open(p, 'r') as f:
        t = f.read().split()
        return (t[0], t[1])


def sorted_items(items, reverse=False):
    return sorted(items, key=lambda x: x[1], reverse=not reverse)

def print_items(items):
    space = 2
    width0 = max([len(i[0]) for i in items])
    width1 = max([len(str(i[1])) for i in items])
    t = width0 + space + width1
    print('-' * t)
    for item in items:
        print('{:<{width0}}{space}{:>{width1}}'.format(item[0], item[1], width0=width0, width1=width1, space=' ' * space))
    print('=' * t)

def total(items):
    return sum([i[1] for i in items])

class SimpleStrategy:
    def __init__(self, items):
        self.items = items

    def reorder(self):
        self.items = sorted(self.items, key=lambda x: (x['otc'], x['wkc'], x['hrs'], x['id']))

    def nxt(self):
        self.reorder()
        return self.items[0:2]

    def __str__(self):
        self.reorder()
        s = 'Items:\n'
        s += '\n'.join([f'\t{m}' for m in self.items])
        return s

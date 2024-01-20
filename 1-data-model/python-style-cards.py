import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
#元组，赋予其属性 tuple表示无法修改，固定属性。
class FrenchCard:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __getitem__(self, position):
        return self._cards[position]

    def __len__(self): #choice 需要定义长度
        return len(self._cards)

from random import choice

#deck = [Card(rank, suit) for suit in ['spade', 'diamond', 'clubs', 'hearts']
 #                         for rank in [str(i) for i in range(2,11)] + list("JQKA")] #每个suit都在rank中进行了循环。
deck = FrenchCard()
print(choice(deck)) #choice需要定义长度 于是__len__ 同时需要是可迭代对象
print(deck.__getitem__(0)) #你以为__getitem__只能这样获得？
# 直接实例化对象 变为可迭代对象 可通过 for xx in deck迭代 ，同时支持reversed(deck)进行反向迭代。
# for card in deck:
#     print(card)

print(Card(rank='7', suit='spade2') in deck)
#红桃(红心)、黑桃、方块(方片)及梅花(草花)分别用英语hearts、spades、diamonds及clubs表示
#红桃：hearts    黑桃 spades    方块 diamonds   梅花 clubs
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

print(spades_high(deck.__getitem__(21)))

for card in sorted(deck, key=spades_high): #key = lambda x: spades_high(x)
    print(card)

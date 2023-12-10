import sys
import collections

def hand_type(hand):
    cnt = collections.Counter(hand)
    cnt1 = collections.Counter(cnt.values())
    if cnt1 == {5: 1}:
        return 6 # five of a kind
    elif cnt1 == {4: 1, 1: 1}:
        return 5 # four of a kind
    elif cnt1 == {2: 1, 3: 1}:
        return 4 # full house
    elif cnt1 == {3: 1, 1: 2}:
        return 3 # three of a kind
    elif cnt1 == {2: 2, 1: 1}:
        return 2 # two pair
    elif cnt1 == {2: 1, 1: 3}:
        return 1 # one pair
    elif cnt1 == {1: 5}:
        return 0 # high card

t = {
    'T': 'a',
    'J': 'b',
    'Q': 'c',
    'K': 'd',
    'A': 'e',
}

def card_key(hand):
    return [t.get(c, c) for c in hand]

def hand_key(hand):
    return hand_type(hand), card_key(hand)

data = []
with open(sys.argv[1]) as f:
    for line in f:
        hand, bid = line.split()
        bid = int(bid)
        data.append((hand, bid))

data.sort(key=lambda x: hand_key(x[0]))
s = 0
for i, (hand, bid) in enumerate(data, start=1):
    s += i * bid
print(s)

# part 2

t['J'] = '1'

def hand_type2(hand):
    return max(hand_type(hand.replace('J', c)) for c in set(hand))

def hand_key2(hand):
    return hand_type2(hand), card_key(hand)

data.sort(key=lambda x: hand_key2(x[0]))
s = 0
for i, (hand, bid) in enumerate(data, start=1):
    s += i * bid
print(s)

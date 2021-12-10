import sys

with open(sys.argv[1]) as f:
    s = f.read()

parts = s.split('\n\n')
nums = parts[0].split(',')
nums = [int(n) for n in nums]

class Card:

    def __init__(self, nums):
        self.nums = set(nums)
        self.combos = []
        for i in range(5):
            self.combos.append(set(nums[i*5:i*5+5]))
            self.combos.append({nums[i+5*z] for z in range(5)})

    def check(self, play):
        for combo in self.combos:
            if combo.issubset(play):
                return True
        return False

    def score(self, play, last):
        unmarked = self.nums - play
        return sum(unmarked) * last

cards = []
for part in parts[1:]:
    cards.append(Card([int(n) for n in part.split()]))

play = set()
first = True
for n in nums:
    play.add(n)
    cards_left = []
    for card in cards:
        if card.check(play):
            if first:
                first = False
                print(card.score(play, n))
            else:
                last = card.score(play, n)
        else:
            cards_left.append(card)
    cards = cards_left
print(last)

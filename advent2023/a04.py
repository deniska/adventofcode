import sys

scratch_cards = []

s = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        card_name, card_data = line.split(': ')
        winning_numbers, card_numbers = card_data.split('|')
        winning_numbers = set(int(n) for n in winning_numbers.split())
        card_numbers = [int(n) for n in card_numbers.split()]
        pts = 0
        matches = 0
        for number in card_numbers:
            if number in winning_numbers:
                matches += 1
                if pts == 0:
                    pts = 1
                else: 
                    pts *= 2
        s += pts
        scratch_cards.append(matches)
print(s)

copies = [1] * len(scratch_cards)
for i, matches in enumerate(scratch_cards):
    for j in range(i+1, i+matches+1):
        copies[j] += copies[i]

print(sum(copies))

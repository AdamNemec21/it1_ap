from random import randint
cards = []
for i in range(1,10):
    cards.append(randint(1,50))
print(cards)

print(cards)

min_index = i
for j in range (i, len(cards)):
    min_index = i
    if cards[j] < cards[i]:
        min_index = j
cards[i], cards[min_index] = cards[min_index], cards[i]
print(cards)

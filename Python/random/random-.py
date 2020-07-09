import random

# returns a random int between 1 and 10
rangeval = random.randint(1, 10)
print(rangeval)

# returns one random string from the list
possibleteams = ['HSV', 'Bremen', 'Dortmund', 'Bayern']
randteam = random.choice(possibleteams)
print(randteam)

# returns 10 strings from the list in random order
possiblecolors = ['Red', 'Green', 'Blue']
randcolor = random.choices(possiblecolors, k=10)
print(randcolor)

# shuffles the list
cards = list(range(1, 33))
random.shuffle(cards)
print(cards)

# returns 7 random cards from the list
cardsonhand = random.sample(cards, k=7)
print(cardsonhand)
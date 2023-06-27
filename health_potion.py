import random
health=50
difficulty=1
#our task is to increase the integer number defined to difficulty as the difficulty level of user increases
#in the game. Easy=1, Medium=2, Hard=3.
potionHealth=random.randint(25,50)//difficulty
#potionHealth=int(random.randint(25,50))
health=health+potionHealth
print(health)


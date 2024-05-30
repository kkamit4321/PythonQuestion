# import random as rd

import operator
import random
print("---------menu----------")
print("press 1 for play game:\npress 2 for play later:")
choice=int(input("enter choice:"))
if choice==1:
    ch=0
    def play_game():
        operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
        for _ in range(10):
            number1 = random.randint(1, 20)
            number2 = random.randint(1, 20)
            operator = random.choice(operators)
            result = play_game(number1, number2)
            print(f"{number1} {operator} {number2} = {result}")
    play_game()

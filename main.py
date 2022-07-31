
import random
top = input('type a number ')
if top.isdigit():
    top = int(top)
    if top < 0:
        print("please enter a number more than zero ")
    else:
        quit()
else:
    print("plese enter a number")
    quit()

r_number = random.randrange(11)
print(r_number)


 
num=18

count=10

while(count>=1):
    guess=int(input("Guess The Number:"))
    if num<guess:
        print("Decrease!!")


    elif num>guess:
        print("Increase!!")

    else:
        print("Correct!")

    print("The no of guesses he took",count)
    count = count-1

if count == 0:
    print("Game Over!!")


    

import random, playsound


# def winning_music():
#     """
#     Plays the winning music.
#     """
#     win_music = ["anime wow.mp3", "bruhh.mp3"]
#     try:
#         playsound.playsound(random.choice(win_music))
#     except Exception as e:
#         print(e)
#
#
# def losing_music():
#     """
#     Plays the losing music.
#     """
#     lose_music = ["Nope.mp3", "Fart.mp3"]
#     try:
#         playsound.playsound(random.choice(lose_music))
#     except Exception as e:
#         print(e)
#
#
# def tie_music():
#     """
#     Plays the tie music.
#     """
#     try:
#         playsound.playsound(random.choice("Awkward Cricket.mp3"))
#     except Exception as e:
#         print(e)


if __name__ == "__main__":
    print("Welcome to the stone paper scissor Game !\n\n")

    attempts = 1
    your_point = 0
    computer_point = 0
    a = str(input('Enter the name of player : '))

    while (attempts <= 10):

        lst = ["stone", "paper", "scissor"]
        ran = random.choice(lst)

        inp = input("Enter your choice (stone/paper/scissor): ")
        inp = inp.lower()

        if inp == ran:
            print("Tie")
            print(f"{a} chose {inp} and computer guess is {ran}")
            print("No body gets point\n")


        elif inp == "stone" and ran == "paper":
            your_point = your_point + 1
            print(f"{a} choosed {inp} and computer guess is {ran}")
            print(f"{a} : 1 point\n")


        elif inp == "paper" and ran == "stone":
            computer_point = computer_point + 1
            print(f"{a} choosed {inp} and computer guess is {ran}")
            print("Computer : 1 point\n")


        elif inp == "scissor" and ran == "paper":
            print(f"{a} chose {inp} and computer guess is {ran}")
            your_point = your_point + 1
            print(f"{a} : 1 point\n")


        elif inp == "paper" and ran == "scissor":
            print(f"{a} choosed {inp} and computer guess is {ran}")
            computer_point = computer_point + 1
            print("computer : 1 point\n")


        elif inp == "stone" and ran == "scissor":
            print(f"{a} choosed {inp} and computer guess is {ran}")
            your_point = your_point + 1
            print("You : 1 point\n")

        elif inp == "stone" and ran == "scissor":
            print(f"{a} choosed {inp} and computer guess is {ran}")
            computer_point = computer_point + 1
            print("computer : 1 point\n")

        else:
            print("Invalid input!\n")
            continue

        print("No. of guesses left: {}".format(10 - attempts))
        attempts = attempts + 1

        if attempts > 10:
            print("Game over!")

    print(f"{a} score: {your_point} \nComputer's score: {computer_point}")

    if computer_point > your_point:
        print(f"Computer won and {a} lost!")

    elif computer_point < your_point:
        print(f"{a} won and computer lost!")

    else:

        print("It was a tie!")
        print("invalid")

    print(10 - attempts, "no. of guesses left")
    attempts = attempts + 1

    if attempts > 10:
        print("game over")

if computer_point > your_point:
    print(f"Computer wins and {a} loose")

if computer_point < your_point:
    print(f"{a} win and the computer looses")

print(f"{a} points is {your_point} and computer points is {computer_point}")



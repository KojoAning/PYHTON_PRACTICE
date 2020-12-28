n = 16
number_of_guesses=1
print('welcom to number guess game :)')
print('You have only 9 guesses')

while (number_of_guesses<= 9) :
    a = int(input('Enter your guess:'))
    if a < n :
        print('Enterd number is small')
    elif a > n:
        print('Entered number is BIG.')
    else:
        print('Correct guess.')
        print ('Game Over')
        print(number_of_guesses, "no.of guesses he took to finish.")
        break

    print(9-number_of_guesses,"number of guess left.")
    number_of_guesses=number_of_guesses+1

if number_of_guesses>9:
    print('You loose')
    print('Game Over')



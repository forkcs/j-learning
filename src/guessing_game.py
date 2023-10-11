import random


def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def get_user_guess():
    return int(input('Guess the number: '))


def game_loop(max_attempts, guessed_number):
    attempts = 0

    while attempts < max_attempts:
        user_input = get_user_guess()
        if user_input == guessed_number:
            print('You guessed the number!')
            break
        if user_input > guessed_number:
            print('The number is smaller than your guess')
        else:
            print('The number is bigger than your guess')
        attempts += 1
    else:
        print(f'You did not guess the number, it was {guessed_number}')


def main():
    max_attempts = 5
    min_value = 1
    max_value = 30

    print('Welcome to the guessing game!')
    print(
        f'You have {max_attempts} attempts to guess a number between {min_value} and {max_value}'
    )

    guessed_number = generate_random_number(min_value, max_value)
    game_loop(max_attempts, guessed_number)


if __name__ == '__main__':
    main()

from msvcrt import getch
import os

username = ""
user_info = {}
score = (0, 0)
moves = []

screen = 'main_menu'
menu_item = 0
main_menu_items = ['Play', 'High Scores', 'Difficulty', 'Quit']
difficulty_items = ['Easy', 'Medium', 'Hard']
difficulty = 'Easy'


class Key:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    RETURN = 4
    ESC = 5
    ROCK = 6
    PAPER = 7
    SCISSORS = 8
    UNDEF = 9


def get_move():
    return 'R'


def get_pressed_key():
    first_part = getch()
    if first_part == b'\xe0':
        second_part = getch()
        return {'H': Key.UP, 'P': Key.DOWN, 'K': Key.LEFT, 'M': Key.RIGHT}[second_part.decode()]
    elif first_part == b'\r':
        return Key.RETURN
    elif first_part == b'\x1b':
        return Key.ESC
    elif first_part == b'r':
        return Key.ROCK
    elif first_part == b'p':
        return Key.PAPER
    elif first_part == b's':
        return Key.SCISSORS
    else:
        return Key.UNDEF


def draw_interface():
    os.system("cls")
    print("Playing as: {} | Difficulty: {}\n\n".format(username, difficulty))

    if screen == 'main_menu':
        for item in main_menu_items:
            index = main_menu_items.index(item)
            print('{} {}'.format(item, "<<" if index == menu_item else ""))
    elif screen == 'difficulty':
        for item in difficulty_items:
            index = difficulty_items.index(item)
            print('{} {}'.format(item, "<<" if index == menu_item else ""))

    elif screen == 'game_over':
        formatted_moves = map(lambda mv: '{}\t{}'.format(mv[0], mv[1]), moves)
        print('Game over.\nRounds played: {}\n\n'.format(score[0]+score[1]))
        print('You\tComputer\n------------\n')
        for move in formatted_moves:
            print('{}'.format(move))
        print('\n------------\n')
        print('{}\t{}'.format(score[0], score[1]))

    elif screen == 'game':
        formatted_moves = map(lambda mv: '{}\t{}'.format(mv[0], mv[1]), moves)
        print("Pick your move... (r -> Rock, p -> Paper, s -> Scissors\n")
        print('Rounds played: {}\n\n'.format(score[0] + score[1]))
        print('You\tComputer\n------------\n')
        for move in formatted_moves:
            print('{}'.format(move))
        print('\n------------\n')
        print('{}\t{}'.format(score[0], score[1]))


def process_key(key):
    global screen
    global menu_item
    global difficulty
    if screen == 'game':
        handle_game(key)
    elif key == Key.ESC and (screen == 'high_scores' or screen == 'game_over'):
        screen = 'main_menu'
        menu_item = 0
    elif key == Key.UP:
        if screen == 'main_menu':
            menu_item -= 1
            if menu_item < 0:
                menu_item = len(main_menu_items) - 1
        elif screen == 'difficulty':
            menu_item -= 1
            if menu_item < 0:
                menu_item = len(difficulty_items) - 1
    elif key == Key.DOWN:
        if screen == 'main_menu':
            menu_item += 1
            if menu_item >= len(main_menu_items):
                menu_item = 0
        elif screen == 'difficulty':
            menu_item += 1
            if menu_item >= len(difficulty_items):
                menu_item = 0
    elif key == Key.RETURN:
        if screen == 'main_menu':
            if main_menu_items[menu_item] == 'Play':
                start_game()
            elif main_menu_items[menu_item] == 'High Scores':
                screen = 'high_scores'
            elif main_menu_items[menu_item] == 'Difficulty':
                screen = 'difficulty'
                menu_item = 0
            else:
                exit(0)
        elif screen == 'difficulty':
            difficulty = difficulty_items[menu_item]
            screen = 'main_menu'
            menu_item = 0


def start_game():
    global screen
    global score
    global moves
    screen = 'game'
    score = (0, 0)
    moves = []


def end_game():
    # save stats
    global screen
    screen = 'game_over'


# return 0 if equal, 1 if user wins, -1 if computer wins
def get_outcome(user_move, computer_move):
    # paper > rock, rock > scissors, scissors > paper
    if user_move == computer_move:
        return 0
    if (user_move, computer_move) in [('P', 'R'), ('R', 'S'), ('S', 'P')]:
        return 1
    else:
        return -1


def handle_game(key):
    global score
    global moves
    if key == Key.ESC or score[0] + score[1] >= 14:
        end_game()

    computer_move = get_move()
    user_move = ''
    if key == Key.ROCK:
        user_move = 'R'
    elif key == Key.PAPER:
        user_move = 'P'
    elif key == Key.SCISSORS:
        user_move = 'S'
    else:
        return

    outcome = get_outcome(user_move, computer_move)
    if outcome == -1:
        score = (score[0], score[1] + 1)
    elif outcome == 1:
        score = (score[0] + 1, score[1])
    
    moves.append((user_move, computer_move, outcome))


if __name__ == "__main__":
    username = input("Enter your name\n\t")

    while True:
        draw_interface()
        process_key(get_pressed_key())

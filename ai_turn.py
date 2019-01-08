# 0 - foarfeca
# 1 - hartie
# 2 - piatra
import random

def get_random():
    r = random.randint(0,2)
    if r ==0:
        return 'F'
    elif r == 1:
        return 'H'
    else:
        return 'P'

def easy_mode():
    get_random()



def medium_mode(prob_dict,pattern_dict):
    # 50% random , 50% anticipare
    sum_of_patterns = 0
    for elem in pattern_dict:
        sum_of_patterns = sum_of_patterns + pattern_dict[elem]

    if sum_of_patterns<3:
        get_random()


    random_move = random.randint(0,2)
    if random_move == 0:
        random_move = 'F'
    elif random_move == 1:
        random_move = 'H'
    else:
        random_move = 'P'
    
    max_prob = 0
    pattern = None
    
    for elem in pattern_dict:
        if pattern_dict[elem] > max_prob and elem[0] == random_move:
            max_prob = pattern_dict[elem]
            pattern = elem
    if pattern == None:
        get_random()
    return pattern[1]
                
                
def hard_mode(prob_dict,pattern_dict):
    
    sum_of_patterns = 0
    for elem in pattern_dict:
        sum_of_patterns = sum_of_patterns + pattern_dict[elem]

    if sum_of_patterns<3:
        get_random()
    
    maxim = 0
    pattern = None

    max_prob = 0
    tip = 0
    for elem in prob_dict:
        
        if prob_dict[elem]> max_prob:
            max_prob = prob_dict[elem]
            tip = elem


    for elem in pattern_dict:
        if pattern_dict[elem] > maxim and  (elem[0]) == (tip):
            
            maxim = pattern_dict[elem]
            pattern = elem
    if pattern == None:
        get_random()
    return pattern[1]

def strategy(prob_dict,pattern_dict,game_mode):


    if game_mode == 0:
        return easy_mode()
    elif game_mode == 1:
        return medium_mode(prob_dict,pattern_dict)
    else:
        return hard_mode(prob_dict,pattern_dict)



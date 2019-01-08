import random

def get_random():
    r = random.randint(0,2)
    if r ==0:
        return 'S'
    elif r == 1:
        return 'P'
    else:
        return 'R'

def get_result(pattern):
    if pattern[1] ==  'S':
        return 'R'
    if pattern[1] == 'R':
        return 'P'
    if pattern[1] == 'P':
        return 'S'

def easy_mode(prob_dict,pattern_dict):
    
    sum_of_patterns = 0
    for elem in pattern_dict:
        sum_of_patterns = sum_of_patterns + pattern_dict[elem]

    if sum_of_patterns<3:
        return get_random()
    
    maxim = 0
    pattern = None

    max_prob = 0
    tip = 0
    for elem in prob_dict:
        
        if prob_dict[elem]> max_prob:
            max_prob = prob_dict[elem]
            tip = elem


    for elem in pattern_dict:
        if pattern_dict[elem] > maxim and  elem[0] == tip:
            
            maxim = pattern_dict[elem]
            pattern = elem
    if pattern == None:
        return get_random()
    return get_result(pattern)

def medium_mode(prob_dict,pattern_dict):
    sum_of_patterns = 0
    for elem in pattern_dict:
        sum_of_patterns = sum_of_patterns + pattern_dict[elem]

    if sum_of_patterns<3:
        return get_random()


    random_move = random.randint(0,2)
    if random_move == 0:
        random_move = 'S'
    elif random_move == 1:
        random_move = 'P'
    else:
        random_move = 'R'
    
    max_prob = 0
    pattern = None
    
    for elem in pattern_dict:
        if pattern_dict[elem] > max_prob and elem[0] == random_move:
            max_prob = pattern_dict[elem]
            pattern = elem
    if pattern == None:
        return get_random()
    return get_result(pattern)
    



def hard_mode(prob_dict,pattern_dict,last_move):

    hard_mode_way = random.randint(1,10)
    if hard_mode_way <=5:
        max_value = 0
        pattern = None
        if last_move == 'U':
            last_move = get_random()
        for elem in pattern_dict:
            if  elem[0] == last_move and pattern_dict[elem]>max_value:
                max_value = pattern_dict[elem]
                pattern = elem

        if pattern == None:
            return get_random()
        return get_result(pattern)
    else:
        medium_mode(prob_dict,pattern_dict)
                
                


def strategy(prob_dict,pattern_dict,last_move,game_mode):


    if game_mode == 0:
        return easy_mode(prob_dict,pattern_dict)
    elif game_mode == 1:
        return medium_mode(prob_dict,pattern_dict)
    else:
        return hard_mode(prob_dict,pattern_dict,last_move)



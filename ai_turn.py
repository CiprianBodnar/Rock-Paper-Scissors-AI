# 0 - easy , foarfeca
# 1 - medium, hartie
# 2 - hard, piatra
import random
def easy_mode():
    return random.randint(0,2)


def medium_mode(user_details):
    # 50% random , 50% anticipare
    if user_details == False:
        return random.randint(0,2)

    else:
        random_move = random.randint(0,2)
        pattern_for_user = user_details['bodnar_ciprian']['pattern']
        max_prob = 0
        pattern = None
        
        for elem in pattern_for_user:
            if pattern_for_user[elem] > max_prob and int ( elem[0] ) == random_move:
                max_prob = pattern_for_user[elem]
                pattern = elem
        if pattern == None:
            return random.randint(0,2)
        return pattern[1]
                
                
def hard_mode(user_details):
    
    if user_details == False:
        return random.randint(0,2)
    else:
        pattern_for_user = user_details['bodnar_ciprian']['pattern']
        maxim = 0
        pattern = None

        prob_for_user = user_details['bodnar_ciprian']['prob']
        max_prob = 0
        tip = 0
        for elem in prob_for_user:
            
            if prob_for_user[elem]> max_prob:
                max_prob = prob_for_user[elem]
                tip = (elem)


        for elem in pattern_for_user:
            if pattern_for_user[elem] > maxim and int (elem[0]) == int(tip):
               
                maxim = pattern_for_user[elem]
                pattern = elem
        if pattern == None:
            return random.randint(0,2)
        return pattern[1]

def strategy():

    user_details = {"bodnar_ciprian": 
                    {   "prob":{"0":5,"1":5,"2":6},
                        "pattern":{"02":3,"01":4,"21":7,"20":5,"10":2,"12":8,"00":5,"22":4,"11":6}
                    }
                    }
    blank = {}
    game_mode = 2

    if game_mode == 0:
        return easy_mode()
    elif game_mode == 1:
        return medium_mode(user_details)
    else:
        
        return hard_mode(user_details)


print(strategy())
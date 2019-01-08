import os
import json


stats_filename = 'stats.json'


def get_user_stats(username):
    # default stats for current user
    user_stats = {
        'choices': {
            'R': 0, 'P': 0, 'S': 0
        },
        'patterns': {
            'RR': 0, 'RP': 0, 'RS': 0,
            'PP': 0, 'PR': 0, 'PS': 0,
            'SS': 0, 'SR': 0, 'SP': 0
        },
        'wins': 0
    }

    if os.path.isfile(stats_filename):
        file_pointer = open(stats_filename, 'r')
        stats = json.load(file_pointer)
        if username in stats:
            user_stats = stats[username]
        file_pointer.close()

    return user_stats


def get_high_scores(top):
    if os.path.isfile(stats_filename):
        file_pointer = open(stats_filename, 'r')
        stats:dict = json.load(file_pointer)
        file_pointer.close()
        return sorted(list(map(lambda x: (x, stats[x]['wins']), stats.keys())), key=lambda x: stats[x[0]]['wins'], reverse=True)[:top]

def save_user_stats(username, user_stats):
    stats = {}
    if os.path.isfile(stats_filename):
        file_pointer = open(stats_filename, 'r')
        stats = json.load(file_pointer)
        file_pointer.close()

    stats[username] = user_stats
    file_pointer = open(stats_filename, 'w')
    json.dump(stats, file_pointer, indent=4)
    file_pointer.close()

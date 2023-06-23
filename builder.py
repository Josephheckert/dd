import races


class Character:

    def __init__(self, race, name, race_subcategory, scores_increase, age, size, speed, languages, abilities, proficiencies, stats):
        self.race = race
        self.race_subcategory = race_subcategory
        self.name = name
        self.scores_increase = scores_increase
        self.age = age
        self.size = size
        self.speed = speed
        self.languages = languages
        self.abilities = abilities
        self.proficiencies = proficiencies
        self.stats = stats


def add_players():
    player_count = 0
    player_count_input = input(f'''How many characters would you like to create?    
Input must be a whole number:    ''')
    try:
        player_count_input = int(player_count_input)
    except ValueError:
        player_count_input = input('Entry must be a whole number. Please try again:    ')
    else:
        player_count = int(player_count_input)
        for i in range(player_count):
            sublist_name = f'player_{i+1}'
            players[sublist_name] = [{"Player Name" : None}]
        print(players)
        print(f"Great! We're going to build {len(players)} characters. Let's get started.")
        player_num = 1
        for player in players:
            player_name = input(f'Player #{player_num}, what is your name?    ')
            players[player][0]["Player Name"] = player_name
            player_num += 1


def select_race():
    race_number = 1
    for player in players:
        print(f'''Great! Now, {player_name}, here are the races you can choose from:
''')
        for i in range(len(races.race_data)):
            print(str(race_number) + ". " + races.race_data[i][0]["Race Name"])
            race_number += 1


players = {}

add_players()

print(players)

from copy import deepcopy
from constants import TEAMS, PLAYERS

players = deepcopy(PLAYERS)
teams = deepcopy(TEAMS)

def clean_data(players):

    cleaned_players = []

    for player in players:
        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians'].split(' and ')
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(player['height'].split(' ')[0])
        cleaned_players.append(fixed)                           

        
    return cleaned_players

def balanced_team(players, teams):

    balanced = {team: [] for team in teams}

    for index, player in enumerate(players):
        team = teams[index % len(teams)]
        balanced[team].append(player)
    return balanced

balanced = balanced_team(clean_data(players), teams)
for team, team_players in balanced.items():
    print('\n' + team)
    print('-' * len(team))
    for player in team_players:
        print(player['name'])
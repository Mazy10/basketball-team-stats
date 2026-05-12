from copy import deepcopy
from constants import TEAMS, PLAYERS

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

def balance_teams(players, teams):

    balanced = {team: [] for team in teams}

    for index, player in enumerate(players):
        team = teams[index % len(teams)]
        balanced[team].append(player)
    return balanced

def display_team_stats(team_name, team_players):
    total_players = len(team_players)

    experienced_players = 0
    inexperienced_players = 0

    total_height = 0

    player_names = []
    guardians = []

    for player in team_players:
        player_names.append(player['name'])
        guardians.extend(player['guardians'])
        total_height += player['height']
        if player['experience']:
            experienced_players += 1
        else:
            inexperienced_players += 1
    
    average_height = total_height / total_players

    print(f'\nTeam: {team_name} Stats')
    print('-' * 20)

    print(f'Total players: {total_players}')
    print(f'Total experienced: {experienced_players}')
    print(f'Total inexperienced: {inexperienced_players}')
    print(f'Average height: {average_height:.1f}')

    print('\nPlayers on Team:')
    print(', '.join(player_names))

    print('\nGuardians:')
    print(', '.join(guardians))

    input('\nPress ENTER to continue...')
    
def menu():
    print('\nBASKETBALL TEAM STATS TOOL')
    print('\n----MENU----')
    print('\nHere are your choicesL:')
    print('A) Display Team Stats')
    print('B) Quit')

def choose_team(balanced_team):
    print('\nA) Panthers')
    print('B) Bandits')
    print('C) Warriors')

    choice = input('\nEnter an option:    ').upper()

    if choice == 'A':
        display_team_stats('Panthers', balanced_team['Panthers'])
    elif choice == 'B':
        display_team_stats('Bandits', balanced_team['Bandits'])
    elif choice == 'C':
        display_team_stats('Warriors', balanced_team['Warriors'])
    else:
        print('\nInvalid option')

if __name__ == "__main__":

    players = deepcopy(PLAYERS)
    teams = deepcopy(TEAMS)
    cleaned_players = clean_data(players)
    balanced_team = balance_teams(cleaned_players, teams)
    
    while True:
        menu()

        option = input('\nEnter an option:    ').upper()
        if option == 'A':
            choose_team(balanced_team)
        elif option == 'B':
            print('\nGoodbye!')  
            break  
        else:
            print('\nInvalid option. Please try again')    
            continue      
from constants import TEAMS, PLAYERS

def clean_data(PLAYERS):

    cleaned = []

    for player in PLAYERS:
        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians'].split(' and ')
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(player['height'].split(' ')[0])
        cleaned.append(fixed)                           

        
    return cleaned

print(clean_data(PLAYERS))

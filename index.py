class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_team.append(player)
            
        print(new_team)


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "a", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

player_kevin = Player(players[0]["name"],players[0]["age"], players[0]["position"], players[0]["team"])
player_Jason = Player(players[1]["name"], players[1]["age"], players[1]["position"], players[1]["team"])
player_Kyrie = Player(players[2]["name"], players[2]["age"], players[2]["position"], players[2]["team"])
player_Damian = Player(players[3]["name"], players[3]["age"], players[3]["position"], players[3]["team"])
player_Joel = Player(players[4]["name"], players[4]["age"], players[4]["position"], players[4]["team"])
player_a = Player(players[5]["name"], players[5]["age"], players[5]["position"], players[5]["team"])


# ... (class definition and large list of players here)
def populateTeam():
    new_team = []
    # Write your for loop here to populate the new_team variable with Player objects.
    for player in players:
        new_team.append(player)
    return new_team
    
#print(populateTeam)


# populateTeam()
Player.get_team(players)



class Pair():

    def __init__(self):
   
        onechoice  = "a"
        twochoice  = "a"
        mikechoice = "a"
        leochoice  = "b"
        self.match(onechoice, twochoice, mikechoice, leochoice)

    def match(self, onechoice, twochoice, mikechoice, leochoice):
        team_1 = ["a", onechoice]
        team_2 = ["b", twochoice]
        self.mike = ["a", mikechoice]
        self.leo  = ["b", leochoice]
        self.teams   = {"a": "Team 1", "b": "Team 2"}
        self.workers = {"a": "Mike", "b": "Leo"}
    
        if   team_1[1] == self.mike[1] or self.leo[1]:
            self.choiceprocess(team_1, team_2)
        elif team_2[1] == self.mike[1] or self.leo[1]:
            self.choiceprocess(team_2, team_1)
        else:
            print('No match.')

    def choiceprocess(self, match, rake):
        teamchoice = []
        leftover   = ["a", "b"]
        teamchoice.append(match[1])
        leftover.remove(match[1])
    
        winner = self.workers[teamchoice[0]]
        loser  = self.workers[leftover[0]]
            
        finlist = [f"{self.teams[match[0]]} : {winner}", 
                   f"{self.teams[rake[0]]} : {loser}", 
                   f"{winner} : {self.teams[match[0]]}", 
                   f"{loser} : {self.teams[rake[0]]}"]
        for i in finlist:
            print(i)

Pair() 
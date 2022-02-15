import views
import models
import datetime
import itertools

class Tournament:
    """
    """
    def __init__(self):
        """
        """
        self.uid = ''
        self.number_of_players = 0
        # self.Players = []
        self.date_stamp = str(datetime.datetime.now())
        self.end_date = ''
        self.status = 'en cours'
        # self.number_of_players = 0
        self.number_of_players = self.set_number_of_players()
        # print(type(self.number_of_players))
        # self.Players = views.select_players(self.number_of_players)
        self.Players = self.select_players()
        print('les joueurs selected : ' + str(self.Players))
        self.rounds = self.create_rounds()
        self.push_tournament_into_DB()

    
    def set_number_of_players(self):
        """
        """
        number_of_players = views.new_tournament_get_number_of_players()
        return number_of_players

    def select_players(self):
        """
        """
        list_of_players = views.select_players(self.number_of_players)
        return list_of_players
        # print(list_of_players)
    
    def create_rounds(self):
        """
        a partir du moment ou nous avons le nombre de joueur on peut determner le nombre
        de rounds et ainsi se faire recontrer les joueurs
        """
        round = Rounds()
        print('creation des rounds ' + str(self.Players))
        first_matchs = round.create_first_matchs(self.Players)
        print('create rounds : players list : ')
        print(self.Players)
        round.create_next_matchs(first_matchs, self.Players)

    def push_tournament_into_DB(self):
        """
        """
        models.insert_tournament(self)

class Rounds:
    """
    """
    def __init__(self):
        """
        """
        self.uid = ''
        self.matchs = []
        self.uids = []
        self.startDate = str(datetime.datetime.now())
        print('Rounds creation_')

    def create_first_matchs(self, list_of_players):
        """
        """
        print('first matchs creation algo suisse')
        list_of_players_to_fight = list_of_players.copy()
        # print(list_of_players)
        # print(list_of_players_to_fight)
        number_of_players = len(list_of_players_to_fight)
        middle_index = int((len(list_of_players_to_fight)/2))
        list_of_matchs = []
        i = 0
        while True :
            # print(list_of_players_to_fight)
            print('middle ' + str(middle_index) + ' interation : ' + str(i))
            if number_of_players > 2 :
                list_of_matchs.append([list_of_players_to_fight.pop(), list_of_players_to_fight.pop(middle_index)])
                number_of_players = len(list_of_players_to_fight)
                middle_index = int((len(list_of_players_to_fight)/2))
            elif number_of_players > 1 :
                print('fin de liste pair')
                list_of_matchs.append([list_of_players_to_fight.pop(), list_of_players_to_fight.pop()])
                break
            elif number_of_players < 2 :
                print(number_of_players)
                print('joueur tout seul')
                list_of_matchs.append([list_of_players_to_fight[0], ''])
                break
            i += 1
            # print(len(list_of_players_to_fight)/2)
        print(list_of_matchs)
        return list_of_matchs
    
    def create_next_matchs(self, list_of_matchs, list_of_players):
        """
        """
        print('next matchs creation')
        rounds = []
        first_round = list_of_matchs[0]
        # print('list of matchs : ')
        # print(list_of_matchs)
        # print('list of players : ')
        # print(list_of_players)
        if (len(list_of_players) % 2) != 0 :
            list_of_players.append('')
        combinaisons = itertools.combinations(list_of_players, 2)
        for combinaison in combinaisons:
            print(combinaison)
            player1 = combinaison[0]
            player2 = combinaison[1]
            # si un couple de joueurs est deja dans le premier round alors on ajoute pas ce round
            if player1 != first_round[0] and player2 != first_round[1] or player1 != first_round[1] and player2 != first_round[0]:
                rounds.append([player1, player2])
        rounds.insert(0, first_round)
        print('rounds : ')
        print(rounds)
        return rounds


        

class Matchs:
    """
    """
    def _init__(self, player1, player2):
        """
        """
        self.uid = ''
        self.player1 = player1
        self.player2 = player2
        self.winner = ''
        self.creationDate = str(datetime.datetime.now())

    def set_winner(self, player):
        """
        """
        self.winner = player
    
    def pushIntoDB(self):
        """
        """
        models.insertMatch(self)



# tournament = Tournament()
# tournament.set_number_of_players()
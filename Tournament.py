import views
import models
import datetime
import itertools
import controllers


class Tournament:
    """
    class Tournament
    """

    def __init__(self):
        """ """
        self.uid = 0
        self.number_of_players = 0
        self.Players = [] # TODO supp de la
        self.date_stamp = str(datetime.datetime.now())
        self.creationDate = str(datetime.datetime.now())
        self.endDate = ""
        self.status = "en cours"
        self.number_of_players = 0
        self.rounds = [] # TODO supp de la
        ## self.number_of_players = self.set_number_of_players() # TODO to controllers
        ## self.Players = self.select_players() # TODO to controllers
        ## print("les joueurs selected : " + str(self.Players)) # TODO to controllers
        # self.rawRounds = []
        ## self.uid = self.push_tournament_into_DB() # TODO to controllers
        ## self.create_rounds() # TODO to controllers
        ## controllers.launchTournament() # TODO to controllers

    def set_number_of_players(self):
        """ """
        number_of_players = views.new_tournament_get_number_of_players()
        return number_of_players

    def select_players(self):
        """ """
        list_of_players = views.select_players(self.number_of_players)
        for player in list_of_players:
            player["localScore"] = 0
        return list_of_players

    def create_rounds(self):
        """
        a partir du moment ou nous avons le nombre de joueur on peut determner
        le nombre de rounds et ainsi se faire recontrer les joueurs
        """
        tournamentUID = self.uid
        firstRound = Round(tournamentUID)
        self.rounds.append(firstRound)
        print("creation des rounds " + str(self.Players))
        first_matchs = firstRound.create_round(self.Players, "score")
        print('create_rounds : first_matchs' + str(first_matchs))
        # firstRound.matchs.append(first_matchs)
        # print("tournament : create rounds : first_matchs : " + str(first_matchs))
        # self.round.matchs = first_matchs

        # firstRound.matchs.append(firstRound.createMatchs())
        firstRound.matchs = first_matchs
        firstRound.createMatchs() # TODO move to controllers
        print('create_rounds : firstRound.matchs : ' + str(firstRound.matchs))

        # print("self.round.matchs : " + str(self.round.matchs))

    def push_tournament_into_DB(self):
        """ """
        print("create tournament in DB ")
        return models.insert_tournament(self)

    def launchTournament(self): # mettre dans controller
        """
        Lancement du tournoi
        """
        # Recuperation des parties dans la base
        models
        # Lancement des rounds
        for round in rounds:
            model.getMatchs(roundID)  # une liste de matchs
            views.displayMatchs()


class Round:
    """ """

    def __init__(self, tournamentUID):
        """ """
        self.uid = ""
        self.tournamentUID = tournamentUID
        self.matchs = [] # TODO supp de la
        self.matchsUIDs = [] # TODO supp de la
        self.uid = [] # TODO supp de la
        self.creationDate = str(datetime.datetime.now())
        print("Rounds creation_")

    def create_round(self, list_of_players, arrangement):
        """ """
        print("first matchs creation algo suisse")
        list_of_players_to_fight = list_of_players.copy()
        list_of_players_to_fight = sorted(
            list_of_players_to_fight, key=lambda i: i[arrangement]
        )
        number_of_players = len(list_of_players_to_fight)
        middle_index = int((len(list_of_players_to_fight) / 2))
        # TODO order list of players
        list_of_matchs = []
        i = 0
        while True:
            print("middle " + str(middle_index) + " iteration : " + str(i))
            if number_of_players > 2:
                list_of_matchs.append(
                    [
                        list_of_players_to_fight.pop(),
                        list_of_players_to_fight.pop(middle_index),
                    ]
                )
                number_of_players = len(list_of_players_to_fight)
                middle_index = int((len(list_of_players_to_fight) / 2))
            elif number_of_players > 1:
                print("fin de liste pair")
                list_of_matchs.append(
                    [list_of_players_to_fight.pop(), list_of_players_to_fight.pop()]
                )
                break
            elif number_of_players < 2:
                print(number_of_players)
                print("joueur tout seul")
                list_of_matchs.append([list_of_players_to_fight[0], ""])
                break
            i += 1
        print("rounds : create round : list_of_matchs" + str(list_of_matchs))
        self.uid = self.pushRoundIntoDB()
        return list_of_matchs

    def create_next_rounds(self, list_of_matchs, list_of_players):
        """ """
        print("next matchs creation")
        rounds = []
        first_round = list_of_matchs[0]
        # print('lis_of_players)
        if (len(list_of_players) % 2) != 0:
            list_of_players.append("")
        combinaisons = itertools.combinations(list_of_players, 2)
        for combinaison in combinaisons:
            print("combinaison :")
            print(combinaison)
            player1 = combinaison[0]
            player2 = combinaison[1]
            # si un couple de joueurs est deja dans le premier round alors on ajoute pas ce round
            if (
                player1 != first_round[0]
                and player2 != first_round[1]
                or player1 != first_round[1]
                and player2 != first_round[0]
            ):
                rounds.append([player1, player2])
        rounds.insert(0, first_round)
        print("rounds : ")
        print(rounds)
        return rounds

    def pushRoundIntoDB(self):
        """ """
        print("push rounds into db" + str(self))
        roundUID = models.insertRound(self)
        return roundUID
    
    def createMatchs(self):
        """"""
        print("match creation !!!")
        theMatch = Match()
        roundUID = self.uid
        print("match du round : " + str(self.matchs))
        for match in self.matchs:
            print("match : " + str(match))
            if match[0] != "" and match[1] != "":
                theMatch.player1 = match[0]["uid"]
                theMatch.player2 = match[1]["uid"]
            elif match[0] == "" and match[1] != "":
                theMatch.player2 = match[1]["uid"]
                Match.player1 = 0
            else:
                theMatch.player1 = match[0]["uid"]
                theMatch.player2 = 0
            print("match into DB")
            theMatch.UID = theMatch.pushMatchIntoDB(roundUID)

class Match:
    """ """

    def __init__(self):
        """ """
        self.player1 = "player1"
        self.player2 = "player2"
        self.winner = ""
        self.creationDate = str(datetime.datetime.now())
        self.roundUID = 0
        self.UID = 0

    def set_winner(self, player):
        """ """
        self.winner = player
        # views.update_winner

    def pushMatchIntoDB(self, roundUID):
        """ """
        print("push match into DB")
        print("players playing : ", self.player1, self.player2)
        return models.insertMatch(self, roundUID)


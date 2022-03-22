import views
import models
import datetime
import itertools


class Tournament:
    """
    class Tournament
    """

    def __init__(self):
        """ """
        self.number_of_players = 0
        # self.Players = []
        self.date_stamp = str(datetime.datetime.now())
        self.creationDate = str(datetime.datetime.now())
        self.endDate = ""
        self.status = "en cours"
        # self.number_of_players = 0
        self.number_of_players = self.set_number_of_players()
        # print(type(self.number_of_players))
        # self.Players = views.select_players(self.number_of_players)
        self.Players = self.select_players()
        print("les joueurs selected : " + str(self.Players))
        self.rawRounds = []
        self.uid = self.push_tournament_into_DB()
        self.create_rounds()
        # self.roundsUIDs = []
        # print(self.roundUIDs)

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
        self.round = Round()
        print("creation des rounds " + str(self.Players))
        first_matchs = self.round.create_round(self.Players, "score")
        print("tournament : create rounds : first_matchs : " + str(first_matchs))
        self.round.matchs = first_matchs
        self.round.createMatchs()
        print("self.round.matchs : " + str(self.round.matchs))
        # first_matchs
        # print("create rounds : players list : ")
        # print(self.Players)
        # return first_matchs
        # print("vars round : " + str(vars(self.round)))
        # print("test dic : " + str(self.round.matchs))
        # self.rawRounds.append(self.round)
        # return self.rounds.create_next_rounds(first_matchs, self.Players)

    def push_tournament_into_DB(self):
        """ """
        # print("nombre de rounds : " + str(len(self.rawRounds[0].matchs)))
        print("create tournament in DB ")
        # roundLocalId = 0
        # for round in self.rawRounds:
        #     print("round " + str(round))
        #     roundIUD = self.round.pushRoundIntoDB()
        #     self.roundsUIDs.append(roundIUD)
        # # print(self.rawRounds.matchsUIDs)
        # # roundIUD = self.round.pushRoundIntoDB(self.rawRounds, self.rawRounds)
        return models.insert_tournament(self)

    def launchTournament(self):
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

    def __init__(self):
        """ """
        self.uid = ""
        self.matchs = []
        self.matchsUIDs = []
        self.tournamentUID = 0
        self.uid = []
        self.creationDate = str(datetime.datetime.now())
        print("Rounds creation_")

    def create_round(self, list_of_players, arrangement):
        """ """
        print("first matchs creation algo suisse")
        list_of_players_to_fight = list_of_players.copy()
        list_of_players_to_fight = sorted(
            list_of_players_to_fight, key=lambda i: i[arrangement]
        )
        # print(list_of_players)
        # print(list_of_players_to_fight)
        number_of_players = len(list_of_players_to_fight)
        middle_index = int((len(list_of_players_to_fight) / 2))
        # TODO order list of players
        list_of_matchs = []
        i = 0
        while True:
            # print(list_of_players_to_fight)
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
            # print(len(list_of_players_to_fight)/2)
        print("rounds : create round : list_of_matchs" + str(list_of_matchs))
        self.uid = self.pushRoundIntoDB()
        # self.createMatchs()
        return list_of_matchs

    def create_next_rounds(self, list_of_matchs, list_of_players):
        """ """
        print("next matchs creation")
        rounds = []
        first_round = list_of_matchs[0]
        # print('list of matchs : ')
        # print(list_of_matchs)
        # print('list of players : ')
        # print(list_of_players)
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
        # theMatch = Match()
        # print("round : " + str(self.matchsUIDs))
        roundUID = models.insertRound(self)
        # theMatch = Match()
        # for match in self.matchs:
        #     print("match : " + str(match))
        #     if match[0] != "" and match[1] != "":
        #         theMatch.player1 = match[0]["uid"]
        #         theMatch.player2 = match[1]["uid"]
        #     elif match[0] == "" and match[1] != "":
        #         theMatch.player2 = match[1]["uid"]
        #         Match.player1 = 0
        #     else:
        #         theMatch.player1 = match[0]["uid"]
        #         theMatch.player2 = 0
        #     print("match into DB")
        #     theMatch.UID = theMatch.pushMatchIntoDB()
        #     self.matchsUIDs.append(theMatch.UID)  # boucle infinie !!!
        # return True
        # roundsUIDs = []
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
        self.UID = 0
        # self.uid = self.pushIntoDB(self)

    def set_winner(self, player):
        """ """
        self.winner = player
        # views.update_winner

    def pushMatchIntoDB(self, roundUID):
        """ """
        print("push match into DB")
        print("players playing : ", self.player1, self.player2)
        return models.insertMatch(self, roundUID)


# tournament = Tournament()
# tournament.set_number_of_players()

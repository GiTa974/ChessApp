import views
import models
import Players
import Tournament

# MENU PRINCIPAL
def menu_principal():
    """ """
    reponse_consistance = False
    while not reponse_consistance:
        reponse = views.menu_principal()
        print(reponse)
        try:
            int_reponse = int(reponse["choix"])
            if int_reponse > -1 and int_reponse <= reponse["longueur"]:
                reponse_consistance = True
                # break
            else:
                views.bad_choice(reponse["longueur"])
        except:
            views.bad_choice(reponse["longueur"])
    if reponse["choix"] == "0":
        get_last_tournament()
    elif reponse["choix"] == "1":
        menu_tournois()
    elif reponse["choix"] == "2":
        menu_players()
    elif reponse["choix"] == "3":
        quit()

    # print(reponse)


# MENU TOURNOIS
def menu_tournois():
    """ """
    reponse_consistance = False
    while not reponse_consistance:
        reponse = views.menu_tournois()
        print(reponse)
        try:
            int_reponse = int(reponse["choix"])
            if int_reponse > -1 and int_reponse <= reponse["longueur"]:
                reponse_consistance = True
                # break
            else:
                views.bad_choice(reponse["longueur"])
                # reponse_consistance = True)
        except:
            views.bad_choice(reponse["longueur"])
    if reponse["choix"] == "0":
        get_last_tournament()
    elif reponse["choix"] == "1":
        get_tournaments_by_date_desc()
    elif reponse["choix"] == "2":
        currentTournament = Tournament.Tournament()
        currentTournament.number_of_players = currentTournament.set_number_of_players()
        currentTournament.Players = currentTournament.select_players()
        currentTournament.uid = currentTournament.push_tournament_into_DB()
        models.pushTournamentPlayersIntoDB(currentTournament.uid, currentTournament.Players)
        currentTournament.create_rounds()
        # launchTournament()
    elif reponse["choix"] == "3":
        # views.back()
        menu_principal()
    elif reponse["choix"] == "4":
        quit()


def get_last_tournament():
    """ """
    print("get last tournament()")


def create_tournament():
    """ """
    print("create tournament()")
    number_of_players = views.new_tournament_get_number_of_players()
    print("nombre de joueur : " + str(number_of_players))
    # set_of_players = views.affect_players(number_of_players)


def get_tournaments_by_date_desc():
    """ """
    print("get tournaments by date desc()")

# MENU PLAYERS
def menu_players():
    """ """
    reponse_consistance = False
    while not reponse_consistance:
        reponse = views.menu_joueurs()
        print(reponse)
        try:
            int_reponse = int(reponse["choix"])
            if int_reponse > -1 and int_reponse <= reponse["longueur"]:
                reponse_consistance = True
                # break
            else:
                views.bad_choice(reponse["longueur"])
        except:
            views.bad_choice(reponse["longueur"])
    if reponse["choix"] == "0":
        get_players_by_date_desc()
    elif reponse["choix"] == "1":
        # create_player()
        new_player = Players.Player()
        new_player.create_player()
    elif reponse["choix"] == "2":
        menu_principal()
    elif reponse["choix"] == "3":
        quit()


def get_players_by_date_desc():
    """ """
    # print('get players by date desc()')
    list_players = models.get_players_by_uid_asc()
    # print(list_players)
    views.print_list_of_players(list_players)


def create_player():
    print("create player()")

    reponse = views.create_player()
    print(reponse)

def quit():
    """ """
    models.DBClose()

def launchTournament():
    """
    appelle le tournois actuel
    """
    

# menu_principal()

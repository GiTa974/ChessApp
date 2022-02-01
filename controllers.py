import views

# MENU PRINCIPAL
def menu_principal():
    """
    """
    reponse_consistance = False
    while not reponse_consistance:
        reponse = views.menu_principal()
        print(reponse)
        try :
            int_reponse = int(reponse['choix'])
            if int_reponse > -1 and int_reponse <= reponse['longueur']:
                reponse_consistance = True
                # break
            else:
                views.bad_choice(reponse['longueur'])
        except :
            views.bad_choice()
    if reponse['choix'] == '0':
        get_last_tournament()
    elif reponse['choix'] == '1':
        menu_tournois()
    elif reponse['choix'] == '2':
        menu_players()
    elif reponse['choix'] == '3':
        views.quit()

    # print(reponse)

# MENU TOURNOIS
def menu_tournois():
    """
    """
    reponse_consistance = False
    while not reponse_consistance:
        reponse = views.menu_tournois()
        print(reponse)
        try :
            int_reponse = int(reponse['choix'])
            if int_reponse > -1 and int_reponse <= reponse['longueur']:
                reponse_consistance = True
                # break
            else:
                views.bad_choice(reponse['longueur'])
                # reponse_consistance = True)
        except :
            views.bad_choice()
    if reponse['choix'] == '0':
        get_last_tournament()
    elif reponse['choix'] == '1':
        get_tournaments_by_date_desc()
    elif reponse['choix'] == '2':
        create_tournament()
    elif reponse['choix'] == '3':
        # views.back()
        menu_principal()
    elif reponse['choix'] == '4':
        views.quit()

def get_last_tournament():
    """
    """
    print('get last tournament()')

def create_tournament():
    """
    """
    print('create tournament()')
    # views.create_tournament()

def get_tournaments_by_date_desc():
    """
    """
    print('get tournaments by date desc()')

# MENU PLAYERS
def menu_players():
    """
    """
    reponse_consistance = False
    while not reponse_consistance:
        reponse = views.menu_joueurs()
        print(reponse)
        try :
            int_reponse = int(reponse['choix'])
            if int_reponse > -1 and int_reponse <= reponse['longueur']:
                reponse_consistance = True
                # break
            else:
                views.bad_choice(reponse['longueur'])
        except :
            views.bad_choice()
    if reponse['choix'] == '0':
        get_players_by_date_desc()
    elif reponse['choix'] == '1':
        create_player()
    elif reponse['choix'] == '2':
        menu_principal()
    elif reponse['choix'] == '3':
        views.quit()

def get_players_by_date_desc():
    """
    """
    print('get players by date desc()')

def create_player():
    print('create player()')
    reponse = views.create_player()
    print(reponse)

# menu_principal()

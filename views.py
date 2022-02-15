import controllers
import models

def menu_principal():
    """
    """
    print('\nMENU PRINCIPAL\n')
    i = 0
    print(str(i) + ' - Retourner au tournoi en cours')
    i+=1
    print(str(i) + ' - Menu tournois')
    i+=1
    print(str(i) + ' - Menu joureurs')
    i+=1
    print(str(i) + ' - Quitter')
    reponse = input('faites votre choix et appuyez sur entree\n')
    # tester si la reponse est ok
    return {'choix' : reponse, 'longueur' : i}

# TOURNOIS
def menu_tournois():
    """
    """
    print('\nMENU TOURNOIS\n')
    i = 0
    print(str(i) + ' - Retourner au tournoi en cours')
    i+=1
    print(str(i) + ' - Consulter les tournois')
    i+=1
    print(str(i) + ' - Creer un tournoi')
    i+=1
    print(str(i) + ' - Retour au menu precedent')
    i+=1
    print(str(i) + ' - Quitter')
    reponse = input('faites votre choix et appuyez sur entree\n')
    # tester si la reponse est ok
    return {'choix' : reponse, 'longueur' : i}

def new_tournament_get_number_of_players():
    """
    """
    print('CREATION DU TOURNOI')
    number_of_players = input('Entrez le nombre de joueurs : ')
    return int(number_of_players)

def affect_players(number_of_players):
    """
    """
    list_of_players = []
    i = 0
    while i < number_of_players:
        print(i)
        list_of_players.append(choose_player())
        i+=1
    return list_of_players

def choose_player():
    """
    """
    list_of_players = models.get_players_by_uid_asc()
    return 1

def select_players(number_of_players):
    """
    """
    all_players = models.get_players_by_uid_asc()
    # print('player selected')
    number_of_selected_players = 0
    list_of_selected_players = []
    # print(type(all_players))
    while number_of_selected_players < number_of_players :
        indice = 0
        for player in all_players :
            print(str(indice) + ' - ' + player['LastName'] + ' ' + player['FirstName'] + ' ne(e) le : ' + player['BirthDate'])
            indice += 1
        print('Selectionner le joueur competiteur : (restant ' + str(number_of_players - number_of_selected_players) + '/' + str(number_of_players) + ')')
        try :
            selection = int(input())
            if selection > len(all_players) - 1 :
                print('\nJe n ai pas compriS votre réponse\nSelectionner un nombre entre 0 et ' + str(len(all_players)-1))
            elif all_players[selection] in list_of_selected_players :
                print('\nJoueur deja selectionne, choisissez un autre :')
            else :
                list_of_selected_players.append(all_players[selection])
                number_of_selected_players += 1
        except :
            print('\nJe n ai pas compris votre réponse\nSelectionner un nombre entre 0 et ' + str(len(all_players)-1))
    return list_of_selected_players

# JOUEURS
def menu_joueurs():
    """
    """
    print('\nMENU JOUEURS\n')
    i = 0
    print(str(i) + ' - Consulter les joueurs')
    i+=1
    print(str(i) + ' - Creer un joueur')
    i+=1
    print(str(i) + ' - Retour au menu precedent')
    i+=1
    print(str(i) + ' - Quitter')
    reponse = input('faites votre choix et appuyez sur entree\n')
    # tester si la reponse est ok
    return {'choix' : reponse, 'longueur' : i}

def create_player():
    """
    """
    print('\nCREATION D UN JOUEUR')
    last_name = ''
    while last_name == '' :
        last_name = input('Entrez le nom : ')
    first_name = ''
    while first_name == '' :
        first_name = input('Entrez le prenom : ')
    birth = False
    while not birth:
        birth_date = input('Entrez la date de naissance (JJ/MM/AAAA) : ')
        try :
            numbers = birth_date.split('/')
            if len(numbers) == 3 and int(numbers[0]) < 31 and int(numbers[1]) < 13 and int(numbers[2]) > 1900 and int(numbers[2]) < 2050:
                birth = True
            else:
                print('Date de naissance mal renseignee 0')
        except :
            print('Date de naissance mal renseignee')
    # pseudo = input('Entrez le pseudo')
    print('vous avez entre le joueur : ' + last_name + ', ' + first_name + ' ne(e) le : ' + birth_date)
    confirmed = input('Vous confirmez ? (oui ou non)\n')
    if confirmed == 'oui':
        print('push_new_player_to_DB')
        return last_name, first_name, birth_date
    else :
        print('Abandon ! Retour au menu precedent.')
    controllers.menu_players()

def print_list_of_players(list_players):
    """
    """
    i = 0
    for player in list_players:
        print(str(i) + ' - ' + player['LastName'] + ', ' + player['FirstName'] + ' ne(e) le ' + player['BirthDate'])
        i+=1

# GENERIQUES
def bad_choice(max):
    """
    """
    print('\nje n ai pas compris votre reponse, resaississez la svp\n' + 
    '(Une reponse sous forme de nombre est atendu entre 0 et ' + str(max) + ')')

def quit():
    """
    """
    print('au revoir !!!')

# def create_tournament():
#     """
#     """
#     print('\nCREATION DU TOURNOI\n')
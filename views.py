import controllers

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
    last_name = input('Entrez le nom : ')
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

def create_tournament():
    """
    """
    print('\nCREATION DU TOURNOI\n')
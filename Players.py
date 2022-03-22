import models
import views

class Player:
    """
    """
    def __init__(self):
        """
        """
        print('init')
        self.lastname =''
        self.firstname = ''
        self.birthdate = ''
        self.score = ''
        self.uid = ''
    
    def create_player(self):
        """
        """
        print('create player')
        infos_new_player = views.create_player()
        self.uid = models.get_last_record_id_player() + 1
        self.score = 0
        print('new id = ' + str(self.uid))
        # reponse = views.create_player()
        print(infos_new_player)
        self.lastname = infos_new_player[0].lower()
        self.firstname = infos_new_player[1].lower()
        self.birthdate = infos_new_player[2].lower()
        models.insert_new_player(self)
        # back to player menu
        views.menu_joueurs()


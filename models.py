import tinydb
import datetime

db = tinydb.TinyDB("db.json")


def get_players_by_uid_asc():
    """ """
    table = db.table("joueurs")
    return table.all()


def insert_new_player(player):
    """ """
    table = db.table("joueurs")
    # serialized ?
    print("player : " + player.lastname)
    creation_date = datetime.datetime.now()
    table.insert(
        {
            "FirstName": player.firstname,
            "LastName": player.lastname,
            "BirthDate": player.birthdate,
            "uid": player.uid,
            "score": player.score,
            "DateStamp": str(creation_date),
        }
    )  # voir la serialisation
    db.close()


def get_last_record_id_player():
    """
    permet de recuperer le dernier id pour la creation d un nouveau joueur
    """
    table = db.table("joueurs")
    table_length = len(table.all())
    try:
        last_id_player = int(table.all()[table_length - 1]["uid"])
    except:
        print("table joueur non existante last id = 0")
        last_id_player = 0
    return int(last_id_player)


def insert_tournament(tournament):
    """ """
    # print("players : " + str(tournament.Players))
    # print("model tournament insertion : " + str(tournament.roundsUIDs))
    tableTournaments = db.table("tournaments")
    # try car la table est suceptible de ne pas exister
    try:
        TournamentUID = tableTournaments.all()[-1]["uid"] + 1
    except:
        print("La table tournaments est vide uid = 1")
        TournamentUID = 1
    tableTournaments.insert(
        {
            "uid": TournamentUID,
            "CreationDate": str(tournament.creationDate),
            "EndDate": str(tournament.endDate),
            "Status": tournament.status
        }
    )  # voir la serialisation
    # "RoundsUID": tournament.roundsUIDs,
    return TournamentUID


def insertRound(round):
    """ """
    print(round)
    tableRounds = db.table("rounds")
    # try car la table est suceptible de ne pas exister
    try:
        roundUID = tableRounds.all()[-1]["uid"] + 1
    except:
        print("La table matchs est vide uid = 1")
        roundUID = 1
    tableRounds.insert(
        {
            "uid": roundUID,
            "CreationDate": str(round.creationDate),
        }
    # "MatchsUID": round.matchsUIDs,
    )  # voir la serialisation
    return roundUID


def insertMatch(match, roundUID):
    """ """
    print(match)
    tableMatchs = db.table("matchs")
    # try car la table est suceptible de ne pas exister
    try:
        matchUID = tableMatchs.all()[-1]["uid"] + 1
    except:
        print("La table matchs est vide uid = 1")
        matchUID = 1
    tableMatchs.insert(
        {
            "uid": matchUID,
            "roundUID": roundUID,
            "CreationDate": str(match.creationDate),
            "Player1": match.player1,
            "Player1 result": "",
            "Player2": match.player2,
            "Player2 result": "",
        }
    )  # voir la serialisation
    # db.close()
    return matchUID


def getMatchs(roundID):
    """ """
    tableRounds = db.table("rounds")
    Rounds = tinydb.Query()
    matchsIDs = tableRounds.search(Rounds.uid == roundID)
    print(matchsIDs)
    return matchsIDs

import firebase_admin
from firebase import firebase
from firebase_admin import db, credentials
import json
import random
firebase = firebase.FirebaseApplication("https://wso-projekt-default-rtdb.firebaseio.com/%22", None)

cred_obj = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://wso-projekt-default-rtdb.firebaseio.com/%22"
	})

#DZIALA TYLKO NA JEDNYM OSTATNIM REKORDZIE
def down_from_db():
    ref = db.reference("/wso-projekt-default-rtdb/Ruchy/")
    #ostatni rekord z bazy danych
    last_record = ref.order_by_key().limit_to_last(1).get()
    #zamiana OrderDict na zwykly dict
    to_dict = json.loads(json.dumps(last_record))
    #zapisanie nazwy klucza do zmiennej
    key_to_str = "".join(to_dict.keys())
    #pobranie samych ruchow z dict
    moves = to_dict[key_to_str]["Ruchy"]
    # print(moves)
    return moves


def generate_random_loc():
    x = str(random.randrange(0, 5))
    y = str(random.randrange(0, 5))
    location = x+y
    return location

def rabbit_loc(x = '0', y = '0'):
    location = x+y
    return location


def iterating_comparison(moves, location):
    steps = 0
    while moves[steps] != location:
        steps += 1
    return steps


def message(steps):
    print(f"Wykonano {steps} ruchow!")

def json_message(steps):
    return int(steps)

def send_message_to_db(data):
    return firebase.post('/wso-projekt-default-rtdb/Cel', json_message(data))

#baza danych z liczba prob i iloscia potrzebnych ruchow do osiagniecia celu
def save_result_to_db(steps):
    pass

#fajna funkcja co nie
message(iterating_comparison(down_from_db(), rabbit_loc()))
send_message_to_db(iterating_comparison(down_from_db(), rabbit_loc()))
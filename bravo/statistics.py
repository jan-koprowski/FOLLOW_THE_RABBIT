import plotly.graph_objects as go
import numpy as np
from firebase import firebase
from firebase_admin import db, credentials
import firebase_admin
import json

firebase = firebase.FirebaseApplication("https://wso-projekt-default-rtdb.firebaseio.com/%22", None)

cred_obj = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://wso-projekt-default-rtdb.firebaseio.com/%22"
	})



def download_data():
    ref = db.reference("/wso-projekt-default-rtdb/Cel/")
    get_record = ref.order_by_key().get()
    dict_values = json.loads(json.dumps(get_record)).values()
    return list(dict_values)

def print_diagram(*data):
    x = np.linspace(0, len(data), num = len(data))

    fig = go.Figure()
    fig.add_trace(go.Scatter(
                x = x,
                y = data,
                mode="lines",
                name = "Liczba kroków = f(próby)"
                ))

    fig.update_layout(
    title="Po ilu krokach złapano króliczka?",
    xaxis_title="Próba",
    yaxis_title="Liczba kroków",
    legend_title="Liczba kroków = f(próby)"
    )

    fig.show()

print_diagram(*download_data())
# print(download_data())
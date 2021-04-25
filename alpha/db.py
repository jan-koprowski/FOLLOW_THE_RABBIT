from firebase import firebase

firebase = firebase.FirebaseApplication("https://wso-projekt-default-rtdb.firebaseio.com/",None)

def my_data(date, values):
    return {
        'Data': date,
        'Ruchy': values}

def add_to_db(date, values):
    result = firebase.post('/wso-projekt-default-rtdb/Ruchy', my_data(date, values))
    print(result)

# add_to_db('2020-04-15', [1,2,3,4,5,6,7,8,8,8], 5)
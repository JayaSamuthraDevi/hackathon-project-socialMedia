import requests
import json
import random
import string

api_url = 'http://localhost:8080/api/v1/userdetails/newUser'

def generate_email():
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    return f"{username}@{domain}.com"

interests = list(range(1, 38))
accountChoice = list(range(0,2))

genderChoice = list(range(0,2))

accounttype = ['public','private']
gendertype=['Male','Female']


def generate_phone():
    ph_no = [] 
    num=''
  
    ph_no.append(random.randint(6, 9)) 
  
    for i in range(1, 10): 
        ph_no.append(random.randint(0, 9)) 
  
    for i in ph_no: 
        num+=str(i)

    return num



for _ in range(100):
    user_interests = random.sample(interests, 10)

    user_email = generate_email()
    user_firstname = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    user_lastname = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    user_phno = generate_phone()
    user_password = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))



    temp1=random.sample(accountChoice,1)[0]
    temp2=random.sample(genderChoice,1)[0]
    interest_arr=[]


    for interest in user_interests:
        interest_arr.append({"interestId":interest})

    user_data = {
        "userName": f"User{_+1}",
        "firstName": user_firstname,
        "lastName": user_lastname,
        "userProfile": "user.png",
        "email": user_email,
        "phNo": user_phno,
        "gender": gendertype[temp2],
        "dateOfBirth": "2000-01-01",
        "password": user_password,
        "accountType": accounttype[temp1],
        "interests": interest_arr
    }

    json_data = json.dumps(user_data)

    print(json_data)

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(api_url, data=json_data, headers=headers)

        if response.status_code == 200:
            print(f"User {_+1} inserted successfully.")
        else:
            print(f"Failed to insert user {_+1}. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while inserting user {_+1}: {e}")

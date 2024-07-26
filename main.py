import requests
import random, os
import schedule
from time import sleep
from datetime import date

messages = [
    "I was unable to complete my leetcode problems today",
    "I didn't do my leetcode problem :("
]

consequences = [
    'chipotle',
    '5 dollars',
    'a drink'
]

# get customizable user data
username = input("What leetcode username would you like to track? ")
while True:
    sleep(1)
    os.system('clear')
    try:
        questions = int(input("How many LeetCode problems do you need to complete per day? (At least 1.) "))
        if questions < 1:
            print("Number of questions should be more or equal to one")
        else:
            sleep(0.2)
            os.system('clear')
            print(f"Tracking {questions} questions a day")
            break
    except ValueError:
        print("Please enter an integer.")

def fetch_leetcode(user, num_questions):
    os.system('clear')
    print("fetching...")
    url = f'https://leetcode-stats-api.herokuapp.com/{user}'

    response = requests.get(url)

    # check if user exists
    if response.status_code == 200:
        leetcode_data = response.json()
        problems_done = leetcode_data.get('totalSolved')

        today = date.today()
        if leetcode_data[today] > (num_questions - 1):
            result(True)
        else:
            result(False)
        
    else:
        print(f"Unable to fetch data for user {user}. Status code {response.status_code}")
    
def result(status):
    os.system('clear') # signal end of fetching with screen clear

    # failed to complete problem
    if status == False:
        # assign specific punishment
        message = random.choice(messages)
        consequence = random.choice(consequences)
        
        print(f"{message}. I owe you {consequence}")
    
    else:
        print("Great success!")
        pass

# run logic at 12 AM
schedule.every().day.at("00:00").do(fetch_leetcode, username, questions)

run = True
while run:
    schedule.run_pending()
    sleep(5)

#!/usr/bin/python3
""" Export api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user_id
    user_res = requests.get(url_user)

    user_data = user_res.json()
    username = user_data.get('username')

    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    todos_response = requests.get(url_todos)
    todos = todos_response.json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            completed = task.get('completed')
            title_task = task.get('title')
            csvwriter.writerow([user_id, username, completed, title_task])

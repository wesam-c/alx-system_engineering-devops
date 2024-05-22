#!/usr/bin/python3
'''
Gather data from an API
'''

import requests
import sys


def get_user_name(user_id):
    """Get the list of users"""
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "users"
    """Format the url"""
    url_to_call = f"{url}/{endpoint}/{user_id}"
    """Get the response"""
    response = requests.get(url_to_call)
    json_response = response.json()
    return json_response


def get_user_todos(user_id):
    """Get the list of todos"""
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "todos"
    """Format the url"""
    url_to_call = f"{url}/users/{user_id}/{endpoint}"
    """Get the response"""
    response = requests.get(url_to_call)
    json_response = response.json()
    return json_response


def export_csv(todos, user_id, name):
    """Export to CSV"""
    with open(f"{user_id}.csv", "w") as file:
        for todo in todos:
            file.write(f'"{user_id}","{name}",'
                       f'"{todo.get("completed")}","{todo.get("title")}"\n')


if __name__ == "__main__":
    """Get User TODOS"""
    user_id = sys.argv[1]
    user_todos = get_user_todos(user_id)
    user = get_user_name(user_id)
    export_csv(user_todos, user_id, user.get("username"))


#!/usr/bin/python3
"""Gather data from an API"""
import json
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


def export_json(todos, user_id, name):
    """Export to Json"""
    data = {
        f"{user_id}": [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": name,
            }
            for todo in todos
        ]
    }
    with open(f"{user_id}.json", "w") as file:
        json.dump(data, file)


def get_all_users():
    """Get all users"""
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "users"
    """Format the url"""
    url_to_call = f"{url}/{endpoint}"
    """Get the response"""
    response = requests.get(url_to_call)
    json_response = response.json()
    return json_response


def get_all_todos():
    """Get all todos"""
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "todos"
    """Format the url"""
    url_to_call = f"{url}/{endpoint}"
    """Get the response"""
    response = requests.get(url_to_call)
    json_response = response.json()
    return json_response


if __name__ == "__main__":
    """Get User TODOS"""
    all_users = get_all_users()
    all_todos = get_all_todos()
    all_data = {}
    for user in all_users:
        user_id = user.get("id")
        user_todos = [todo for todo in all_todos
                      if todo.get("userId") == user_id]
        user_name = user.get("username")
        all_data[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_name,
            }
            for todo in user_todos
        ]
    with open("todo_all_employees.json", "w") as file:
        json.dump(all_data, file)


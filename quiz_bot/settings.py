import json

with open('token.txt', 'r') as tk:
    token = tk.read()

with open('users.json', 'r') as user:
    users_dict = json.load(user)

def add_new_user(id, result):
    users_dict[str(id)] = result
    with open('users.json', 'w') as user:
        json.dump(users_dict, user)


def get_rating(user_id):
    results = []
    for k, v in users_dict.items():
        results.append((v, k))
    sorted_results = sorted(results, reverse=True)
    for index_user in sorted_results:
        if str(user_id) in index_user:
            return sorted_results.index(index_user) + 1

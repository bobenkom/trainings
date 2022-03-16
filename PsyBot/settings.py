import os.path

with open('token.txt', 'r') as tk:
    token = tk.read()

new_users_dict = {}

if not os.path.isfile('users.txt'):
    raise Exception('Missing users.txt')
elif not os.path.isfile('psychologists.txt'):
    raise Exception('Missing psychologists.txt')
else:
    with open('users.txt', 'r') as user:
        users_dict = {}
        for line in user:
            a = line.find('@')
            users_dict[line[:a]] = line[a + 1:]
    with open('psychologists.txt', 'r') as psy:
        psychol_dict = {}
        for line in psy:
            a = line.find('@')
            psychol_dict[line[:a]] = line[a + 1:]
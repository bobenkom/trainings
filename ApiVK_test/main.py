# VK API DOCS:
# https://vk.com/dev/methods

# How to get auth code:
# https://oauth.vk.com/authorize?client_id=<YOUR CLIENT ID>&redirect_uri=https://vk.com

# How to get token:
# https://oauth.vk.com/access_token?client_id=<YOUR CLIENT ID>&client_secret=<YOUR CLIENT SECRET>&redirect_uri=https://vk.com&code=<YOUR AUTH CODE>

# "access_token":"64c63267392def797fe511a31cd9f715c19198b7270ced26d0828a16e81c944837e7121e7672da0d3ebfc"

import requests
import queries
import json
import time


class VkApi:
    api_url = 'https://api.vk.com/method/'
    api_version = "5.131"

    def __init__(self, api_token):
        self.token = api_token


    def get_user_info(self, user_id):
        r = requests.get(self.api_url + "users.get", params={
            "access_token": self.token,
            "v": self.api_version,
            'user_ids': user_id
        })
        if not r.ok:
            print(f"Error! Got status code: {r.status_code}")
        else:
            return r.json()["response"]

    def search_words(self, query, latitude, longitude):
        posts = []
        start_from = 0
        while len(posts) < 1000:
            r = requests.get(self.api_url + "newsfeed.search", params={
                "access_token": self.token,
                "v": self.api_version,
                'q': query,
                "count": 200,
                "latitude": latitude,
                "longitude": longitude,
                "start from": start_from,
                # "start_time": start_time,
                # "end_time": end_time

            })
            if not r.ok:
                print(f"Error! Got status code: {r.status_code}")

            elif "next_from" in r.json()["response"].keys():
                start_from = r.json()["response"]["next_from"]

            batch = r.json()["response"]["items"]
            posts += batch
            time.sleep(1)
            with open('tags_data.json', 'a') as tags_file:
                json.dump(batch, tags_file)
                tags_file.write('\n')


    def wall_search(self, url, query):
        r = requests.get(self.api_url + "wall.search", params={
            "access_token": self.token,
            "v": self.api_version,
            "domain": url,
            'query': query,
            "count": 100,
        })
        if not r.ok:
            print(f"Error! Got status code: {r.status_code}")
        else:
            with open('wall.json', 'w') as wall:
                json.dump(r.json()["response"], wall)

    def get_members(self, id, query, count):
        r = requests.get(self.api_url + "wall.search", params={
            "access_token": self.token,
            "v": self.api_version,
            "group_id": id,
            'query': query,
            "count": count,
            'offset': 0,
            'fields': 'bdate, city, coutry, education, sex, universities'
        })
        if not r.ok:
            print(f"Error! Got status code: {r.status_code}")
        else:
            with open('members.json', 'w') as members:
                json.dump(r.json()["response"], members)


api = VkApi("")


if __name__ == '__main__':
    n = 1
    for name in queries.tags:
        api.search_words(name, "55.7558", "37.6173") # Москва
        print(f'сформирован {n} запрос из {len(queries.tags)}')
        n += 1


    # api.wall_search()
    # api.get_members()




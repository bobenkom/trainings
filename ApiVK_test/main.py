import requests
import queries
import json
import time
from datetime import datetime

TOKEN = 'Enter your token here'
RIA_NEWS_PAGE_ID = -15755094

class VkApi:
    api_url = "https://api.vk.com/method/"
    api_version = "5.131"
    NEWSFEED_SEARCH_MAX_POSTS = 1000
    NEWSFEED_SEARCH_MAX_COUNT = 200
    WALL_SEARCH_MAX_POSTS = 5000
    WALL_SEARCH_MAX_COUNT = 100

    def __init__(self, api_token):
        self.token = api_token

    def get_user_info(self, user_id: str) -> dict:
        """"""
        r = requests.get(self.api_url + "users.get", params={
            "access_token": self.token,
            "v": self.api_version,
            "user_ids": user_id
        })
        if not r.ok:
            raise Exception(f"Error! Got status code: {r.status_code}")
        else:
            return r.json()["response"]

    def get_group_info(self, group_ids: str) -> int:
        r = requests.get(self.api_url + "groups.getById", params={
            "access_token": self.token,
            "v": self.api_version,
            "group_ids": group_ids,
            "fields": "members_count"
        })
        if not r.ok:
            raise Exception(f"Error! Got status code: {r.status_code}")
        else:
            return r.json()["response"][0]["members_count"]

    # start_time и end_time принимаются в формате "дд-мм-гггг"
    def search_key_words(self, query: str, latitude: str, longitude: str, start_time: str, end_time: str) -> json:
        posts = ''
        start_from = 0
        start_time = int(datetime.strptime(start_time, '%d-%m-%Y').timestamp())
        end_time = int(datetime.strptime(end_time, '%d-%m-%Y').timestamp())
        while len(posts) < self.NEWSFEED_SEARCH_MAX_POSTS:
            r = requests.get(self.api_url + "newsfeed.search", params={
                "access_token": self.token,
                "v": self.api_version,
                'q': query,
                "count": self.NEWSFEED_SEARCH_MAX_COUNT,
                "latitude": latitude,
                "longitude": longitude,
                "start from": start_from,
                "start_time": start_time,
                "end_time": end_time
            })
            if not r.ok:
                raise Exception(f"Error! Got status code: {r.status_code}")

            elif "next_from" in r.json()["response"].keys():
                start_from = r.json()["response"]["next_from"]

            batch = r.json()["response"]["items"]
            posts += json.dumps(batch) + '\n'
            time.sleep(1)
        with open('key_words_data.json', 'w') as tags_file:
            tags_file.write(posts)

    def wall_search(self, owner_id: int):
        publications = []
        offset = 0
        while len(publications) < self.WALL_SEARCH_MAX_POSTS:
            r = requests.get(self.api_url + "wall.get", params={
                "access_token": self.token,
                "v": self.api_version,
                "owner_id": owner_id,
                "count": self.WALL_SEARCH_MAX_COUNT,
                "offset": offset
            })
            if not r.ok:
                raise Exception(f"Error! Got status code: {r.status_code}")
            else:
                items = r.json()['response']['items']
                publications += items
                offset += len(items)
                time.sleep(0.5)
        with open('wall.json', 'w') as wall:
            json.dump(publications, wall)

    def get_members(self, group_id: str, members_count: int):
        members = []
        offset = 0
        while len(members) < members_count:
            r = requests.get(self.api_url + "groups.getMembers", params={
                "access_token": self.token,
                "v": self.api_version,
                "group_id": group_id,
                "count": 1000,
                "offset": offset,
                "fields": "bdate, city, country, education, sex, universities"
            })
            if not r.ok:
                raise Exception(f"Error! Got status code: {r.status_code}")
            else:
                items = r.json()['response']['items']
                members += items
                offset += len(items)
                time.sleep(0.5)
                print(f"{len(members)} из {members_count}")
        with open("members.json", "w") as members_file:
            json.dump(members, members_file)


api = VkApi(TOKEN)

if __name__ == '__main__':
    for name in queries.tags:
        api.search_key_words(name, "55.7558", "37.6173", "24-02-2022", "03-03-2022")    # Москва
        print(f'сформирован {queries.tags.index(name) + 1} запрос из {len(queries.tags)}')

    api.wall_search(RIA_NEWS_PAGE_ID)

    api.get_members("rt_international", api.get_group_info("rt_international"))     # Страница RT

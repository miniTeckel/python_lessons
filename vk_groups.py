#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import argparse
import requests
import time
import json


class VK_API:
    VK_URL = "https://api.vk.com/method/"
    VK_API_VER = "5.52"
    MAX_REQ_PER_SEC = 3

    def __init__(self, access_token):
        self.access_token = access_token
        self.request_count = 0
        self.request_start = 0

    def get_all_friends(self, user_id):
        params = {}
        if not user_id is None:
            params["user_id"] = user_id

        response = self._call_vk_api("friends.get", params)
        if response:
            return response["items"]
        return []

    def _check_limits(self):
        now = time.perf_counter()
        if now - self.request_start > 1.0:
            self.request_start = now
            self.request_count = 1
        elif self.request_count == self.MAX_REQ_PER_SEC:
            time.sleep(1.3 - (now - self.request_start))
            self.request_start = time.perf_counter()
            self.request_count = 1
        else:
            self.request_count += 1

    def _call_vk_api(self, method, params):
        self._check_limits()
        params["access_token"] = self.access_token
        params["v"] = self.VK_API_VER
        response = requests.get("%s%s" % (self.VK_URL, method), params=params)
        json_ = response.json()
        if "response" in json_:
            return json_['response']
        else:
            raise LookupError(json_["error"]["error_msg"])

    def get_id(self, user_name):
        params = {}
        if not user_name is None:
            params["user_ids"] = user_name

        response = self._call_vk_api("users.get", params)
        if response:
            return response[0]["id"]
        return None

    def get_groups(self, user_id):
        params = {"user_id": user_id}
        response = self._call_vk_api("groups.get", params)
        if response:
            return response["items"]
        return []

    def get_group_info(self, group_ids):
        params = {"group_ids": ",".join(str(x) for x in group_ids),
                  "fields": "members_count"}
        response = self._call_vk_api("groups.getById", params)
        if response:
            return response
        return []


def format_result(groups):
    results = []
    for g in groups:
        results.append({"name": g["name"],
                        "gid": g["id"],
                        "members_count": g["members_count"]})
    return results

def output_result(file, result):
    with open(file, 'wt') as f:
        f.write(json.dumps(result, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id', help='user ID')
    group.add_argument('--username', help='user name')
    parser.add_argument('--file', default='groups.json', help='resulting file')
    parser.add_argument('--token', help='access token', required=True)
    args = parser.parse_args()

    vk_api = VK_API(args.token)
    if args.username:
        args.id = vk_api.get_id(args.username)

    friends_id = vk_api.get_all_friends(args.id)
    groups = set(vk_api.get_groups(args.id))
    count = 0.0
    percents = 0
    for friend_id in friends_id:
        try:
            friend_groups = set(vk_api.get_groups(friend_id))
            groups = groups-friend_groups
            count += 1

            new_percents = int(100.0 * count / len(friends_id))
            if new_percents > percents:
                percents = new_percents
                print ("%d%% groups=%d"%(percents, len(groups)))
            else:
                print(".")
        except LookupError as error:
            print ("User: %d error: %s"%(friend_id, error))
    res = format_result(vk_api.get_group_info(groups))
    if args.file:
        output_result(args.file, res)
    else:
        print (json.dumps(res, indent=4))

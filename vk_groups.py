#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import argparse
import requests
import time

class VK_API:
    VK_URL = "https://api.vk.com/method/"
    VK_API_VER = "5.52"
    MAX_REQ_PER_SEC = 3
    MAX_REQ = 100
    
    
    def __init__(self, access_token):
        self.access_token = access_token

    def get_all_friends(self, user_id):   
        params = {
            'access_token': self.access_token,
            'v': self.VK_API_VER,    
        }


        response = requests.get("%s%s" %(self.VK_URL, "friends.get"), params=params)
        json_ = response.json()
        if "response" in json_:
            return json_['response']['items']
        print(json_)
        return []
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id', help='user ID')
    group.add_argument('--username', help='user name')
    parser.add_argument('--file', default='groups.json', help='resulting file')
    parser.add_argument('--token', help='access token', required=True)
    args = parser.parse_args()

    #print (args) 
    vk_api = VK_API(args.token)
    friends_id = vk_api.get_all_friends(args.id)
    print (friends_id)
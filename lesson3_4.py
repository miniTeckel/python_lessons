import requests
import time

VK_URL = "https://api.vk.com/method/"
VK_API_VER = "5.52"
MAX_REQ_PER_SEC = 3
MAX_REQ = 100


def get_access_token(path="./vk_access_token.txt"):
    with open(path, "rt") as source:
        return source.read()


def get_all_friends(token, user_id=None):   
    params = {
        'access_token': token,
        'v': VK_API_VER,    
    }
    if not user_id is None:
        params["user_id"] = user_id 


    response = requests.get("%s%s" %(VK_URL, "friends.get"), params=params)
    json_ = response.json()
    if "response" in json_:
        return json_['response']['items']
    print(json_)
    return []


def check_limits(req_count):
    if req_count % MAX_REQ_PER_SEC == 0:
        time.sleep(1)
    return req_count < MAX_REQ


if __name__ == "__main__":
    access_token = get_access_token()
    my_friends = get_all_friends(access_token)
    common_friends = set(my_friends)
    req_count = 1
    for id in my_friends:
        if not check_limits(req_count):
            break
        his_friends = get_all_friends(access_token, id)
        req_count += 1
        if his_friends:
            common_friends = set(his_friends) & common_friends
    print(common_friends)
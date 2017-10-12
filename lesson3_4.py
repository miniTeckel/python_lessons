import requests

VK_URL = "https://api.vk.com/method/"
VK_API_VER = "5.52"


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


    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

if __name__ == "__main__":
    get_all_friends(get_access_token())
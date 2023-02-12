import requests


response_users = requests.get('https://reqres.in/api/users').json()
response_unknown = requests.get('https://reqres.in/api/unknown').json()
data_users_list = []


def parser() -> list:
    for user in response_users['data']:
        for add_info in response_unknown['data']:
            additional_info = {}
            if user['id'] == add_info['id']:
                additional_info['name'] = add_info.get('name')
                additional_info['year'] = add_info.get('year')
                additional_info['color'] = add_info.get('color')
                additional_info['pantone_value'] = add_info.get('pantone_value')
                user['add_info'] = additional_info
                data_users_list.append(user)
    return data_users_list


def data_writing(data_users_list):
    for data_user in data_users_list:
        data_user.pop('id')
        file = open(f'users/{data_user.get("first_name")}_{data_user.get("last_name")}.txt', "w")
        file.write(str(data_user))
        file.close()


data_users = parser()
data_writing(data_users)



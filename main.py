import requests
import os


def parser(data_users_list, response_users, response_unknown) -> list:
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


def data_writing(data_user, file_path):
    with open(file_path, "w") as file:
        data_user.pop('id')
        file.write(str(data_user))


def check_users_file(data_users_list):
    for data_user in data_users_list:
        file_path = f'users/{data_user.get("first_name")}_{data_user.get("last_name")}.txt'
        if os.access(file_path, os.F_OK) == True:
            data_writing(data_user, file_path=f'users/{data_user.get("first_name")}_{data_user.get("last_name")}_{data_user.get("id")}.txt')
        else:
            data_writing(data_user, file_path)

def main():
    data_users_list = parser(data_users_list=[], response_users=requests.get('https://reqres.in/api/users').json(),
           response_unknown=requests.get('https://reqres.in/api/unknown').json())
    check_users_file(data_users_list)


if __name__ == "__main__":
    main()




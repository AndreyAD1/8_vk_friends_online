import vk
import getpass


APP_ID = 6454800


def get_user_login():
    user_login = input('Enter VK login: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass('Enter VK password: ')
    return user_password


def get_online_friends(login, password, api_version):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    vk_api = vk.API(session, v=api_version)
    friends_online_id = vk_api.friends.getOnline()
    friends_online_name_id = vk_api.users.get(user_ids=friends_online_id)
    return friends_online_name_id


def print_friend_names_to_console(online_friends):
    online_friends_message = 'Your online friends:\n'
    for friend in online_friends:
        friend_name = friend['first_name']
        friend_surname = friend['last_name']
        online_friends_message = '{}{} {}\n'.format(
            online_friends_message,
            friend_name,
            friend_surname
        )
    print(online_friends_message)


if __name__ == '__main__':
    api_version = 5.52
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password, api_version)
    except vk.exceptions.VkAuthError:
        exit('The wrong login and/or password.')
    print_friend_names_to_console(friends_online)

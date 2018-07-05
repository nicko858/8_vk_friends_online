import vk
import getpass
from vk.exceptions import VkAuthError
import logging


def get_user_login():
    login = input("Enter your vk login: ")
    return login


def disable_vk_log(mode):
    logger = logging.getLogger("vk")
    logger.disabled = mode


def get_user_password():
    password = getpass.getpass(
        prompt="Enter your vk password: ")
    return password


def get_online_friends(login,
                       password,
                       app_id,
                       api_version=5.80):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session, v=api_version)
    friends_online_id = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_online_id)
    return friends_online


def output_friends_to_console(friends_online):
    if not friends_online:
        print("There are no friends online!")
    else:
        delimiter = "*" * 23
        print(delimiter)
        print("* Your friends online *")
        print(delimiter)
        for friend in friends_online:
            print("{first_name} {last_name}".format(**friend))


if __name__ == "__main__":
    disable_vk_log(True)
    app_id = 6623784
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password, app_id)
        output_friends_to_console(friends_online)
    except VkAuthError:
        exit("Incorrect login or password!")
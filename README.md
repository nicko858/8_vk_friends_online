# Watcher of Friends Online

# Quickstart

The program is represented by the module ```vk_friends_online.py```.
Module ```vk_friends_online.py``` contains the following functions:

- ```get_online_friends()```
- ```get_user_login()```
- ```get_user_password()```
- ```output_friends_to_console()```
- ```disable_vk_log()```


The program uses these standart and third-party libraries:

```python
vk
getpass
logging
```

How in works:
- The program suggests user to input [vk](https://vk.com/) login and password 
- Autorization in [vk](https://vk.com/)
- Prints online friends list


# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.


# How to run
- Activate virtualenv
``` bash
source <path_to_virtualenv>/bin/activate
```
- Run script with virtualenv-interpreter
```bash
<path_to_virtualenv>/bin/python3.5 vk_friends_online.py
```
If everything is fine, you'll see such output:

```text
***********************
* Your friends online *
***********************
Сергей Сергеев
Иван Иванов
Константин Константинов
Кирилл Кириллов
```
In case of wrong username or password, you'll see this message:
```text
Incorrect login or password!
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

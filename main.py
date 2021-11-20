# Imports
import os
import json
import time
from colorama import Fore, Back, Style

# JSON 
with open("./Utils/config.json", "r", encoding = "utf8") as file:
    js = json.load(file)

# Start 
try:
# IF member not have IP/SSH
    if js["SSH"] == "":
        print("Добро пожаловать в SMART-HOST!")
        time.sleep(2)

        print("Похоже вас нет в моей базе данных, давайте это исправим!")
        time.sleep(2)

        print("\nДля начала укажите ваш SSH/Домен для подключения!")
        values  = input("SSH/Домен: ")

        print("\nХорошо, теперь давайте я запишу ваш никнейм")
        name    = input("Ваш ник: ")

        type = f"ssh root@{values}"
        os.system("\n" + type)

# Add value in JSON
        try:
            js["SSH"]   += f"ssh root@{values}"
            js["name"]  += f"{name}"

            with open("./Utils/config.json", "w", encoding = "utf8") as file:
                js = json.dump(js, file, indent = 2)

        except Exception as e:
            print("Произошла ошибка при внесении даных!")
            print(e)

# IF have IP/SSH
    elif js["SSH"] != "":
        type = js["SSH"]
        name = js["name"]
        names = name or "Юзер"

        print("Добро пожаловать в SMART-HOST!")
        time.sleep(2)

        print(f"Привет {names}, Рад видить тебя снова!")
        time.sleep(2)
        # value = input("\nЖелаете изменить ваши данные? [y/n]: ")
        # try:
        #     if value == "n":
        os.system(type)   

        # except Exception as e:
        #     print(e)


except Exception as e:
    print(e)
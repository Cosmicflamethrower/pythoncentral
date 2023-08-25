import json
import random
import re

with open('commands.json') as file:
    cmd_mping = json.load(file)


def command_processing(cmd, cnt, attr, athr, id, chnnl, gld):
    global command, content, attributes, author, user_id, channel, guild
    command = cmd
    content = cnt
    attributes = attr
    author = athr
    user_id = id
    channel = chnnl
    guild = gld

    if cmd in cmd_mping:
        cmd_info = cmd_mping[cmd]
        func = cmd_info['function']
        args = cmd_info['args']
        func_to_call = globals().get(func)

        if func_to_call:
            prepared_args = [globals().get(arg) if arg == "attributes" else arg for arg in args]
            return func_to_call(*prepared_args)
        else:
            error_msg = f'Function not found for command: {cmd}'
            print(error_msg)
            return error_msg
    else:
        error_msg = f'Command not found: {cmd}'
        print(error_msg)
        return error_msg


def help():
    return '''`Hello, this is the DeathMetal64 bot.
Commands:
Help: Displays this command. Usage: "help"
Roll: Rolls a dice. Usage: "roll num1 num2".
Level: Shows the level of a user. Usage: "level @User(optional)".
Secretroll: I forgot what this is for lol. Usage: "secretroll". `'''


def level(args):
    ID = re.search(r'\d+', args[0]).group()
    if ID:
        folder_path = "E:\\Data\\DeathMetal64\\user_data"
        file_path = folder_path + '\\' + str(ID) + '.json'
        with open(file_path, 'rt') as file:
            data = json.load(file)
            lvl = int(data["level"])
            exp = int(data["experience"])
            return f'Their level is {lvl}. {exp} required for next level'
    else:
        return 'Invalid user or'



def roll(args):
    num1 = int(args[0])
    num2 = int(args[1])
    num = random.randint(num1, num2)
    return f'You rolled a {num}'

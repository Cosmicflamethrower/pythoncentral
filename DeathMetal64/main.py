import bot

if __name__ == '__main__':
    with open("E:\\Source_Code\\DeathMetal64\\token", 'rt') as file:
        token = file.read()
    bot.run_bot(token)

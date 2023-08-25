import discord
import json
import os
import command_handler
import level_handler
import archive_handler
import pythoncentral.common as common


# Load the responses from the JSON file
def run_bot(token):
    # Initialize the Discord bot client
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}", flush=True)
        common.test()

    @client.event
    async def on_message(message):
        if message.author.bot:
            return

        prefix = 'poledance'
        author = message.author
        ID = author.id
        guild_ID = author.guild.id
        guild_name = message.author.guild.name
        guild = message.guild
        channel_name = message.channel
        channel_ID = message.channel.id
        cnt = message.content
        archive_handler.archive_handler(cnt, author, channel_name, channel_ID, guild_name, guild_ID)
        # Make user data if missing
        data_level_path = "E:\\Data\\DeathMetal64\\user_data"
        if os.path.exists(data_level_path + '\\' + str(ID) + '.json'):
            print('Exists', flush=True)
        elif not os.path.exists(data_level_path + '\\' + str(ID)):
            with open(data_level_path + '\\' + str(ID) + '.json', 'xt') as file_level:
                data = {
                    "level": 1,
                    "experience": 0
                }
                dta = json.dumps(data)
                file_level.write(dta)
            with open(data_level_path + '\\' + str(ID) + '.json', 'r') as file_level:
                print(file_level.read(), flush=True)
        # Get the content of the message (the text sent by the user)
        content = message.content.lower()
        level_handler.expgain(content, ID)
        print("Content: " + content, flush=True)

        # Check if the message is a valid prompt in the JSON data

        result = common.cmd_aysis(message, prefix)
        if result:
            cmd, args = result
            response = command_handler.command_processing(cmd, content, args, author, ID, channel_name, guild)
            print("Command: {}".format(content[len(prefix)]), flush=True)
            await message.channel.send(response)
        else:
            print('False')

    client.run(token)

    # Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token

def archive_handler(message, author, channel_name, channel_ID, guild_name, guild_ID):
    f_path = "E:\\Source_Code\\DeathMetal64\\Archive.txt"

    with open(f_path, 'a', encoding='utf-8') as f:
        archive_message = '{} wrote "{}" in channel {} <{}> in {} <{}>\n'.format(author, message, channel_name, channel_ID, guild_name, guild_ID)
        print(archive_message, flush=True)
        f.write(archive_message)
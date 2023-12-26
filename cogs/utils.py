import io
import random
import os
import discord
import datetime
import pyshorteners
import spotipy
from discord.ext import commands
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError
from ext import notifications


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.notifier = notifications.Notifications()
        client_id = os.environ.get('SPOTIFY_CLID')
        client_secret = os.environ.get('SPOTIFY_SECRET')
        self.spotify_active = False

        if client_id and client_secret:
            self.spotify_active = True
            self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    @staticmethod
    def split_lines(text, max_chars):
        lines = text.split('\n')
        result = []
        current_line = ''
        for line in lines:
            if len(current_line + line) <= max_chars:
                current_line += line + '\n'
            else:
                result.append(current_line.strip())
                current_line = line + '\n'
        if current_line:
            result.append(current_line.strip())
        return result

    @commands.command(name='guildinfo', help='Shows debug info about the guild')
    async def guildinfo(self, ctx, guild: discord.Guild = None):
        if guild is None:
            await ctx.reply('Please specify a guild')
            return

        message = f""">>> **Guild Debug**
        **Guild Name:** {guild.name}
        **Guild ID:** {guild.id}
        **Guild Owner:** {guild.owner}
        **Guild Owner ID:** {guild.owner_id}
        **Guild Created At:** {guild.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Guild Member Count:** {guild.member_count}
        **Guild Emoji Count:** {len(guild.emojis)}
        **Guild Role Count:** {len(guild.roles)}
        **Guild Channel Count:** {len(guild.channels)}
        **Guild Text Channel Count:** {len(guild.text_channels)}
        **Guild Voice Channel Count:** {len(guild.voice_channels)}
        **Guild Category Count:** {len(guild.categories)}
        **Guild Boost Tier:** {guild.premium_tier}
        **Guild Boost Count:** {guild.premium_subscription_count}"""

        await ctx.reply(message)

    @commands.command(name='userinfo', help='Shows debug info about the user')
    async def userinfo(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.reply('Please specify a user')
            return

        message = f""">>> **User Debug**
        **User Name:** {user.name}
        **User ID:** {user.id}
        **User Created At:** {user.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **User Bot:** {user.bot}
        **User Avatar:** {user.avatar.url if user.avatar else user.default_avatar.url}
        **User Discriminator:** {user.discriminator if user.discriminator else 'None'}
        **User Flags:** {user.public_flags}
        **User System:** {user.system}
        **User Mention:** {user.mention}"""

        await ctx.reply(message)

    @commands.command(name='channelinfo', help='Shows debug info about the channel')
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            await ctx.reply('Please specify a channel')
            return

        message = f""">>> **Channel Debug**
        **Channel Name:** {channel.name}
        **Channel ID:** {channel.id}
        **Channel Created At:** {channel.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Channel Category:** {channel.category}
        **Channel Position:** {channel.position}
        **Channel NSFW:** {channel.is_nsfw()}
        **Channel Slowmode Delay:** {channel.slowmode_delay}
        **Channel Topic:** {channel.topic}
        **Channel Mention:** {channel.mention}"""

        await ctx.reply(message)

    @commands.command(name='roleinfo', help='Shows debug info about the role')
    async def roleinfo(self, ctx, role: discord.Role = None):
        if role is None:
            await ctx.reply('Please specify a role')
            return

        message = f""">>> **Role Debug**
        **Role Name:** {role.name}
        **Role ID:** {role.id}
        **Role Created At:** {role.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Role Position:** {role.position}
        **Role Color:** {role.color}
        **Role Permissions:** {role.permissions}
        **Role Mention:** {role.mention}"""

        await ctx.reply(message)

    @commands.command(name='emojiinfo', help='Shows debug info about the emoji')
    async def emojiinfo(self, ctx, emoji: discord.Emoji = None):
        if emoji is None:
            await ctx.reply('Please specify an emoji')
            return

        message = f""">>> **Emoji Debug**
        **Emoji Name:** {emoji.name}
        **Emoji ID:** {emoji.id}
        **Emoji Created At:** {emoji.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Emoji URL:** {emoji.url}
        **Emoji Animated:** {emoji.animated}
        **Emoji Managed:** {emoji.managed}
        **Emoji Require Colons:** {emoji.require_colons}
        **Emoji Available:** {emoji.available}"""

        await ctx.reply(message)

    @commands.command(name='ping', help='Pong!')
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name='shorten', help='Shortens a URL')
    async def shorten(self, ctx, url):
        s = pyshorteners.Shortener()
        await ctx.reply(s.tinyurl.short(url))

    @commands.command(name='help', help='Shows this message')
    async def help(self, ctx):
        max_name_length = max(len(command.name) for command in self.bot.commands if not command.hidden)
        max_desc_length = max(len(command.help) for command in self.bot.commands if not command.hidden)

        header = "Command" + " " * (max_name_length - 7) + "Description" + " " * (
                max_desc_length - 11) + "Usage    Aliases\n"
        messages = []
        current_message = header
        for command in self.bot.commands:
            if command.hidden:
                continue
            help_msg = f"{self.bot.command_prefix}{command.name} "
            if command.params:
                for param in command.params:
                    if param == 'self' or param == 'ctx':
                        continue
                    help_msg += f"<{param}> "
            aliases = ', '.join(command.aliases) if command.aliases else 'None'
            command_message = f"{command.name:<{max_name_length}} {command.help:<{max_desc_length}} {help_msg:<20} {aliases}\n"
            # Check if adding this command would exceed the Discord character limit
            if len(current_message + command_message) > 1994:
                # If it would, add the current message to the list and start a new one
                messages.append(current_message)
                current_message = header + command_message
            else:
                # If not, add the command to the current message
                current_message += command_message
        # Add the last message to the list
        messages.append(current_message)

        for msg in messages:
            await ctx.reply(f"```{msg}```")

    @commands.command(name='uptime', help='Shows the bot\'s uptime')
    async def uptime(self, ctx):
        uptime = datetime.datetime.now() - self.bot.boot_time
        uptime = str(uptime).split('.')[0]
        boot_time = self.bot.boot_time.strftime('%d/%m/%Y %H:%M:%S')
        await ctx.reply(f'Uptime: {uptime} ({boot_time})')

    @commands.command(name='download', help='Links to the github repo')
    async def download(self, ctx):
        await ctx.reply('https://github.com/LapisPhoenix/KeiretsuV2')

    @commands.command(name='watch', help='Whitelists a channel for logging')
    async def watch(self, ctx, channel: discord.TextChannel = None):
        # await ctx.message.delete()
        # if channel is None:
        #     self.notifier.show('Keiretsu V2', 'Please specify a channel')
        #     return

        # with open("whitelist.txt", "a") as f:
        #     channels = f.read().splitlines()
        #     if channel.id in channels:
        #         self.notifier.show('Keiretsu V2', 'Channel is already whitelisted')
        #         return

        #     f.write(f"{channel.id}\n")
        #     self.notifier.show('Keiretsu V2', f"Whitelisted {channel.mention}")
        await ctx.reply('This command is currently disabled')

    @commands.command(name='unwatch', help='Unwhitelists a channel for logging')
    async def unwatch(self, ctx, channel: discord.TextChannel = None):
        # await ctx.message.delete()
        # if channel is None:
        #     self.notifier.show('Keiretsu V2', 'Please specify a channel')
        #     return

        # with open("whitelist.txt", "r") as f:
        #     channels = f.read().splitlines()
        #     if channel.id not in channels:
        #         self.notifier.show('Keiretsu V2', 'Channel is not whitelisted')
        #         return

        # with open("whitelist.txt", "w") as f:
        #     for line in channels:
        #         if line != channel.id:
        #             f.write(f"{line}\n")

        # self.notifier.show('Keiretsu V2', f"Unwhitelisted {channel.mention}")
        await ctx.reply('This command is currently disabled')

    @commands.group(name='spotify', help='Shows information about a spotify track', invoke_without_command=True)
    async def spotify(self, ctx):
        await ctx.reply(f'Use `{ctx.prefix}help` for a list of commands')

    @spotify.command(name='play', help='Plays a spotify track')
    async def spotify_play(self, ctx, *, track):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=track, type='track')
        if results['tracks']['total'] == 0:
            await ctx.reply('No results found')
            return

        track = results['tracks']['items'][0]
        await ctx.reply(f'Playing {track["name"]} by {track["artists"][0]["name"]}')
        self.spotify.start_playback(uris=[track['uri']])

    @spotify.command(name='pause', help='Pauses the current spotify track')
    async def spotify_pause(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        self.spotify.pause_playback()
        await ctx.reply('Paused playback')

    @spotify.command(name='resume', help='Resumes the current spotify track')
    async def spotify_resume(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        self.spotify.start_playback()
        await ctx.reply('Resumed playback')

    @spotify.command(name='next', help='Plays the next spotify track')
    async def spotify_next(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        self.spotify.next_track()
        await ctx.reply('Playing next track')

    @spotify.command(name='previous', help='Plays the previous spotify track')
    async def spotify_previous(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        self.spotify.previous_track()
        await ctx.reply('Playing previous track')

    @spotify.command(name='track', help='Shows information about a spotify track')
    async def spotify_track(self, ctx, *, track):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=track, type='track')
        if results['tracks']['total'] == 0:
            await ctx.reply('No results found')
            return

        track = results['tracks']['items'][0]
        message = f""">>> **{track['name']}**
        **Artist:** {track['artists'][0]['name']}
        **Album:** {track['album']['name']}
        **Release Date:** {track['album']['release_date']}
        **Duration:** {datetime.timedelta(milliseconds=track['duration_ms'])}
        **Popularity:** {track['popularity']}
        **Explicit:** {track['explicit']}
        **URL:** {track['external_urls']['spotify']}"""

        await ctx.reply(message)

    @spotify.command(name='album', help='Shows information about a spotify album')
    async def spotify_album(self, ctx, *, album):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=album, type='album')
        if results['albums']['total'] == 0:
            await ctx.reply('No results found')
            return

        album = results['albums']['items'][0]
        message = f""">>> **{album['name']}**
        **Artist:** {album['artists'][0]['name']}
        **Release Date:** {album['release_date']}
        **Tracks:** {album['total_tracks']}
        **Popularity:** {album['popularity']}
        **URL:** {album['external_urls']['spotify']}"""

        await ctx.reply(message)

    @spotify.command(name='artist', help='Shows information about a spotify artist')
    async def spotify_artist(self, ctx, *, artist):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=artist, type='artist')
        if results['artists']['total'] == 0:
            await ctx.reply('No results found')
            return

        artist = results['artists']['items'][0]
        message = f""">>> **{artist['name']}**
        **Followers:** {artist['followers']['total']}
        **Popularity:** {artist['popularity']}
        **URL:** {artist['external_urls']['spotify']}"""

        await ctx.reply(message)

    @spotify.command(name='playlist', help='Shows information about a spotify playlist')
    async def spotify_playlist(self, ctx, *, playlist):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=playlist, type='playlist')
        if results['playlists']['total'] == 0:
            await ctx.reply('No results found')
            return

        playlist = results['playlists']['items'][0]
        message = f""">>> **{playlist['name']}**
        **Owner:** {playlist['owner']['display_name']}
        **Tracks:** {playlist['tracks']['total']}
        **URL:** {playlist['external_urls']['spotify']}"""

        await ctx.reply(message)

    @spotify.command(name='user', help='Shows information about a spotify user')
    async def spotify_user(self, ctx, *, user):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=user, type='user')
        if results['users']['total'] == 0:
            await ctx.reply('No results found')
            return

        user = results['users']['items'][0]
        message = f""">>> **{user['display_name']}**
        **Followers:** {user['followers']['total']}
        **URL:** {user['external_urls']['spotify']}"""

        await ctx.reply(message)

    @spotify.command(name='search', help='Searches for a spotify track')
    async def spotify_search(self, ctx, *, query):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=query, type='track')
        if results['tracks']['total'] == 0:
            await ctx.reply('No results found')
            return

        message = f""">>> **Search Results**
        **Tracks:** {results['tracks']['total']}
        **Albums:** {results['albums']['total']}
        **Artists:** {results['artists']['total']}
        **Playlists:** {results['playlists']['total']}
        **Users:** {results['users']['total']}"""

        await ctx.reply(message)

    @spotify.command(name='top', help='Shows the top tracks of a spotify user')
    async def spotify_top(self, ctx, *, user):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=user, type='user')
        if results['users']['total'] == 0:
            await ctx.reply('No results found')
            return

        user = results['users']['items'][0]
        results = self.spotify.current_user_top_tracks(limit=10)
        message = f""">>> **{user['display_name']}'s Top Tracks**
        **Tracks:** {results['total']}\n"""

        for i, track in enumerate(results['items']):
            message += f"{i + 1}. {track['name']} - {track['artists'][0]['name']}\n"

        await ctx.reply(message)

    @spotify.command(name='recent', help='Shows the recent tracks of a spotify user')
    async def spotify_recent(self, ctx, *, user):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=user, type='user')
        if results['users']['total'] == 0:
            await ctx.reply('No results found')
            return

        user = results['users']['items'][0]
        results = self.spotify.current_user_recently_played(limit=10)
        message = f""">>> **{user['display_name']}'s Recent Tracks**
        **Tracks:** {results['total']}\n"""

        for i, track in enumerate(results['items']):
            message += f"{i + 1}. {track['track']['name']} - {track['track']['artists'][0]['name']}\n"

        await ctx.reply(message)

    @spotify.command(name='recommend', help='Recommends a spotify track')
    async def spotify_recommend(self, ctx, *, track):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=track, type='track')
        if results['tracks']['total'] == 0:
            await ctx.reply('No results found')
            return

        track = results['tracks']['items'][0]
        results = self.spotify.recommendations(seed_tracks=[track['id']])
        message = f""">>> **Recommendations for {track['name']} by {track['artists'][0]['name']}**
        **Tracks:** {len(results['tracks'])}\n"""

        for i, track in enumerate(results['tracks']):
            message += f"{i + 1}. {track['name']} - {track['artists'][0]['name']}\n"

        await ctx.reply(message)

    @spotify.command(name='related', help='Shows related artists to a spotify artist')
    async def spotify_related(self, ctx, *, artist):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=artist, type='artist')
        if results['artists']['total'] == 0:
            await ctx.reply('No results found')
            return

        artist = results['artists']['items'][0]
        results = self.spotify.artist_related_artists(artist['id'])
        message = f""">>> **Related Artists to {artist['name']}**
        **Artists:** {len(results['artists'])}\n"""

        for i, artist in enumerate(results['artists']):
            message += f"{i + 1}. {artist['name']}\n"

        await ctx.reply(message)

    @spotify.command(name='genres', help='Shows the available spotify genres')
    async def spotify_genres(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.recommendation_genre_seeds()
        message = f""">>> **Available Genres**
        **Genres:** {len(results['genres'])}\n"""

        for i, genre in enumerate(results['genres']):
            message += f"{i + 1}. {genre}\n"

        await ctx.reply(message)

    @spotify.command(name='featured', help='Shows the featured spotify playlists')
    async def spotify_featured(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.featured_playlists()
        message = f""">>> **Featured Playlists**
        **Playlists:** {results['playlists']['total']}\n"""

        for i, playlist in enumerate(results['playlists']['items']):
            message += f"{i + 1}. {playlist['name']} - {playlist['owner']['display_name']}\n"

        await ctx.reply(message)

    @spotify.command(name='new', help='Shows the new spotify releases')
    async def spotify_new(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.new_releases()
        message = f""">>> **New Releases**
        **Albums:** {results['albums']['total']}\n"""

        for i, album in enumerate(results['albums']['items']):
            message += f"{i + 1}. {album['name']} - {album['artists'][0]['name']}\n"

        await ctx.reply(message)

    @spotify.command(name='categories', help='Shows the available spotify categories')
    async def spotify_categories(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.categories()
        message = f""">>> **Available Categories**
        **Categories:** {results['categories']['total']}\n"""

        for i, category in enumerate(results['categories']['items']):
            message += f"{i + 1}. {category['name']}\n"

        await ctx.reply(message)

    @spotify.command(name='category', help='Shows the playlists of a spotify category')
    async def spotify_category(self, ctx, *, category):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=category, type='category')
        if results['categories']['total'] == 0:
            await ctx.reply('No results found')
            return

        category = results['categories']['items'][0]
        results = self.spotify.category_playlists(category['id'])
        message = f""">>> **Playlists in {category['name']}**
        **Playlists:** {results['playlists']['total']}\n"""

        for i, playlist in enumerate(results['playlists']['items']):
            message += f"{i + 1}. {playlist['name']} - {playlist['owner']['display_name']}\n"

        await ctx.reply(message)

    @spotify.command(name='playlist_tracks', help='Shows the tracks of a spotify playlist')
    async def spotify_playlist_tracks(self, ctx, *, playlist):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.search(q=playlist, type='playlist')
        if results['playlists']['total'] == 0:
            await ctx.reply('No results found')
            return

        playlist = results['playlists']['items'][0]
        results = self.spotify.playlist_tracks(playlist['id'])
        message = f""">>> **Tracks in {playlist['name']}**
        **Tracks:** {results['total']}\n"""

        for i, track in enumerate(results['items']):
            message += f"{i + 1}. {track['track']['name']} - {track['track']['artists'][0]['name']}\n"

        await ctx.reply(message)

    @spotify.command(name='status', help='Shows the current spotify status')
    async def status(self, ctx):
        if not self.spotify_active:
            await ctx.reply('This command is currently disabled')
            return

        results = self.spotify.current_playback()
        if results is None:
            await ctx.reply('No results found')
            return

        progress = datetime.timedelta(milliseconds=results['progress_ms'])
        max_progress = datetime.timedelta(milliseconds=results['item']['duration_ms'])
        url = results['item']['external_urls']['spotify']
        artist = results['item']['artists'][0]['name']
        album = results['item']['album']['name']
        name = results['item']['name']

        minimum = 0
        maximum = 10
        progress_bar = '-' * maximum
        prog_normalized = int((results['progress_ms'] / results['item']['duration_ms']) * maximum)
        progress_bar = progress_bar[:prog_normalized] + '>' + progress_bar[prog_normalized + 1:]
        if len(progress_bar) > maximum:
            progress_bar = progress_bar[:maximum]

        message = f""">>> **{name}**
        **Artist:** {artist}
        **Album:** {album}
        **Progress:** {progress} / {max_progress}
        **URL:** {url}
        **Progress Bar:** {progress_bar}"""

        await ctx.reply(message)

    @commands.command(name='loripsum', help='Generates a random lorem ipsum')
    async def loripsum(self, ctx, sentences: int = 5, sentence_length: int = 5):
        WORDS = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'suspendisse', 'mattis',
                 'augue', 'at', 'dui', 'interdum', 'in', 'non', 'quam', 'eleifend', 'vulputate', 'ligula', 'vel', 'a',
                 'metus', 'urna', 'porta', 'euismod', 'eget', 'pretium', 'odio', 'morbi', 'posuere', 'sapien', 'eros',
                 'lobortis', 'fringilla', 'magna', 'laoreet', 'duis', 'sed', 'nisl', 'scelerisque', 'tristique',
                 'nulla', 'vestibulum', 'nibh', 'rutrum', 'ut', 'massa', 'nullam', 'vehicula', 'turpis', 'quis',
                 'iaculis', 'cras', 'pulvinar', 'neque', 'nec', 'hendrerit', 'vitae', 'mi', 'convallis', 'et', 'justo',
                 'tempus', 'leo', 'commodo', 'variusvestibulum', 'finibus', 'nunc', 'proin', 'venenatis', 'ultricies',
                 'nam', 'placerat', 'mauris', 'sagittis', 'suscipit', 'lectus', 'porttitor', 'aenean', 'eu',
                 'elementum', 'velit', 'cursus', 'id', 'donec', 'congue', 'fusce', 'felis', 'tortor', 'vivamus',
                 'dignissim', 'malesuada', 'libero', 'risus', 'egestas', 'nisi', 'tincidunt', 'nuncsuspendisse',
                 'potenti', 'gravida', 'dapibus', 'imperdiet', 'diam', 'tempor', 'erat', 'feugiat', 'purus', 'est',
                 'quisque', 'faucibus', 'aliquam', 'rhoncus', 'ac', 'luctus', 'sodales', 'arcu', 'pellentesque',
                 'dictum', 'nisiaenean', 'lacinia', 'ullamcorper', 'fermentum', 'ultrices', 'tellus', 'praesent',
                 'facilisis', 'auctor', 'molestie', 'maecenas', 'enim', 'phasellus', 'efficitur', 'elitfusce',
                 'volutpat', 'viverra', 'orci', 'curabitur', 'sem']
        SYMBOLS = ['.', '!', '?']

        message = ' '.join(
            f"{' '.join(random.choice(WORDS) for _ in range(sentence_length))}{random.choice(SYMBOLS)}"
            for _ in range(sentences)
        ).capitalize()

        await ctx.reply(file=discord.File(fp=io.StringIO(message), filename='loripsum.txt'))

    @commands.command(name='yt2mp4', help='Converts a YouTube video to mp4')
    async def yt2mp4(self, ctx, url: str):
        try:
            message = await ctx.reply('Finding video...')
            loop = self.bot.loop
            yt = await loop.run_in_executor(None, lambda: YouTube(url))
            stream = yt.streams.get_highest_resolution()

            await message.edit(content='Found Video, Downloading...')
            file = await loop.run_in_executor(None, stream.download)

            await message.edit(content='Downloaded, Uploading...')

            max_file_size = 100_000_000 if self.bot.user.premium else 25_000_000

            if os.path.getsize(file) > max_file_size:
                await message.edit(content=f'File too large to upload, here is a link instead. [Download]({stream.url})')
            else:
                await ctx.send(
                    content=f"Here is your content! [Direct Download]({stream.url})",
                    file=discord.File(fp=file, filename=f'{yt.title}.mp4')
                )

            os.remove(file)  # Clean up

        except AgeRestrictedError:
            await ctx.reply('This video is age restricted, I cannot download it!')
        except RegexMatchError:
            await ctx.reply('Invalid URL')

    @commands.command(name='yt2mp3', help='Converts a YouTube video to mp3')
    async def yt2mp3(self, ctx, url: str):
        try:
            message = await ctx.reply('Finding video...')
            loop = self.bot.loop
            yt = await loop.run_in_executor(None, lambda: YouTube(url))
            stream = yt.streams.get_audio_only()

            await message.edit(content='Found Video, Downloading...')
            file = await loop.run_in_executor(None, stream.download)

            await message.edit(content='Downloaded, Uploading...')

            max_file_size = 100_000_000 if self.bot.user.premium else 25_000_000

            if os.path.getsize(file) > max_file_size:
                await message.edit(content=f'File too large to upload, here is a link instead. [Download]({stream.url})')
            else:
                await ctx.send(
                    content=f"Here is your content! [Direct Download]({stream.url})",
                    file=discord.File(fp=file, filename=f'{yt.title}.mp3')
                )

            os.remove(file)  # Clean up

        except AgeRestrictedError:
            await ctx.reply('This video is age restricted, I cannot download it!')
        except RegexMatchError:
            await ctx.reply('Invalid URL')


async def setup(bot):
    await bot.add_cog(Utils(bot))

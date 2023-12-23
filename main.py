import os
import sys
import datetime
from pathlib import Path
from discord.ext import commands
from dotenv import load_dotenv
from pystyle import Colors, Colorate
from colorama import init, Fore


bot = commands.Bot(command_prefix='!', self_bot=True)   # ! is a placeholder, on ready it will be replaced with the prefix from config file
bot.remove_command('help')
bot.__version__ = '1.1.3'


def inital_window_setup():
    platform = sys.platform
    if platform == 'win32':
        os.system('cls')
        os.system('title Keiretsu V2 - By Lapis Pheonix')
        os.system('mode 100, 30')
    elif platform == 'linux':
        os.system('clear')
        os.system(b'\33]0;Keiretsu V2 - By Lapis Pheonix\a')
        os.system('\x1b[8;30;100t')
    else:
        print('Unsupported platform, some features may be unavailable.')


async def load_cogs() -> int:
    loaded = 0
    cog_dir = Path('./cogs')
    for cog_file in cog_dir.glob('*.py'):
        if not cog_file.name.startswith('_'):
            cog_name = cog_file.stem
            if cog_name == 'dev' and os.environ.get('DEV').lower() == 'false':
                continue

            await bot.load_extension(f'cogs.{cog_name}')
            loaded += 1
    return loaded


@bot.event
async def on_ready():
    init()
    inital_window_setup()
    await load_cogs()

    print(Colorate.Vertical(Colors.blue_to_green, """@@@@                 @@@@
@@@@               @@@@@@
@@@@              @@@@@  
@@@@            @@@@@    
@@@@          @@@@@      
@@@@        @@@@@        
@@@@      @@@@@          
@@@@    @@@@@            
@@@@  @@@@@              
@@@@@@@@@@@@             
@@@@@@@@ @@@@            
@@@@@@    @@@@@          
@@@@       @@@@@         
@@@@         @@@@@       
@@@@          @@@@@      
@@@@            @@@@     
@@@@             @@@@@   
@@@@              @@@@@  
@@@@                @@@@@
@@@@                 @@@@"""))
    prefix = os.environ.get('PREFIX')
    bot.command_prefix = prefix
    bot.boot_time = datetime.datetime.now()
    print(f'Logged in as {Fore.GREEN}{bot.user.name}{Fore.RESET}')
    print(f'Connected to {Fore.GREEN}{len(bot.guilds)}{Fore.RESET} guilds')
    print(f'Loaded {Fore.GREEN}{len(bot.commands)}{Fore.RESET} commands')
    print(f'Prefix: {Fore.GREEN}{prefix}{Fore.RESET}')


if __name__ == '__main__':
    load_dotenv()
    print('Booting Up...')
    bot.run(os.environ.get('TOKEN'), log_level=0)   # 0 = no debug, 1 = debug

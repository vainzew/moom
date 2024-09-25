import sys

sys.dont_write_bytecode = True

from smart_airdrop_claimer import base
from core.token import get_token
from core.info import get_info
from core.game import process_play_game

import time

# ANSI color codes
MAGENTA = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class Moonbix:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # ASCII banner
        self.banner = f"""
{MAGENTA} ___  _ _  ___  ___   ___  ___  ___   _  ___  ___  ___     {WHITE} Moonbix Auto Play Game
{MAGENTA}| . \| | ||_ _|/ __> | . \| . \| . | | || __>|  _>|_ _|    {GREEN} Author      : {WHITE} Alfansyah
{MAGENTA}| | ||   | | | \__ \ |  _/|   /| | |_| || _> | <__ | |     {WHITE} Telegram    : {GREEN} t.me/rynalfan
{MAGENTA}|___/|_|_| |_| <___/ |_|  |_\_\`___'\__/|___>`___/ |_|     {MAGENTA} STAY AWARE AND KEEP LEARNING
        """

    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Number of accounts: {base.white}{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")

                try:
                    token = get_token(data=data)

                    if token:

                        get_info(token=token)

                        process_play_game(token=token)

                        get_info(token=token)

                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 30 * 60
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        moonbix = Moonbix()
        moonbix.main()
    except KeyboardInterrupt:
        sys.exit()

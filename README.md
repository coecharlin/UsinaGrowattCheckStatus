# Growatt to Telegram Script

This Python 3 script logs into server.growatt.com, retrieves the data of your solar panels and sends it to your Telegram bot.

![Screenshot](https://i.imgur.com/K7mVQRX.png)

## Requirements:
 - Python 3
 - Growatt Login Details
 - Telegram Bot
 - Telegram Chat ID

## Instructions:   
 - If you don't have a Telegram bot yet, here's described how to get one (really easy): https://core.telegram.org/bots#6-botfather 
 - Next, obtain your chat id as follows: https://stackoverflow.com/questions/31078710/how-to-obtain-telegram-chat-id-for-a-specific-user#37396871
 - Lastly, set your Username, Password, Telegram API key and Telegram Chat ID in the script and you should be good to go! Call the script using `python3 growatt.py` and you should receive the statistics of your solar panel via Telegram immediately.
 - You can schedule the script using crontab to retrieve automated reports.
 
## Synology specific:
 - For Synology devices, download Python 3 using the package manager
 - Then install pip using: `wget https://bootstrap.pypa.io/get-pip.py && sudo python3 get-pip.py`
 - Create symlink to pip using: `ln -s /volume1/@appstore/py3k/usr/local/bin/pip /usr/bin` 
 - By default, the requests module is missing, so install it using pip: `sudo pip install requests`
 - Then call the script using `python3 growatt.py` 
 - You can schedule the script using the Task Scheduler in Synology.
 
 ## Acknowledgements:
 Many thanks to @Sjord for reverse engineering Growatt's API!

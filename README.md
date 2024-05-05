# L2notify
Simple script that OCR L2 window and sends notification via telegram if found given text.
It only works when the L2 window is active and the monitor is turned on.

# Requirements to run this script:
1. Python 3: https://www.python.org/ - make sure to instal pip package manager and and PATH variable.
2. If you need to install PIP separately, instructions can be found here: https://pip.pypa.io/en/stable/installation/
3. Tesseract WINDOWS Installer: https://github.com/UB-Mannheim/tesseract/wiki

# Creating Telegram bot:
1. Add BotFather to telegram contacts https://telegram.me/BotFather
2. Type /newbot - to generate a bot, give it a name and unique username that end in 'bot' (for example MyL2_bot)
3. The bot is created, you get t.me/address of bot and HTTPAPI key. Write down HTTP:API key.
4. Open your bot with t.me/name address.
5. Click Start and send a message.
6. Open this URL in a browser https://api.telegram.org/bot{our_bot_token}/getUpdates - replacing {our_bot_token} with given token from 
Eg: https://api.telegram.org/bot63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c/getUpdates
7. We will see a json like so
<code>
{
   "ok":true,
   "result":[
      {
         "update_id":83xxxxx35,
         "message":{
            "message_id":2643,
            "from":{
               "..."
            },
            "chat":{
               <color:red>"id":21xxxxx38,</color>
               "first_name":"...",
               "last_name":"...",
               "username":"@username",
               "type":"private"
            },
            "date":1703062972,
            "text":"/start"
         }
      }
   ]
}
</code>

Check the value of result.0.message.chat.id, and here is our Chat ID: 21xxxxx38
When we set the bot token and chat id correctly, the message test123 should be arrived on our Telegram bot chat.


# Installation
1. Open CMD and navigate to this folder
2. Edit mywife.py in any text editor and change values of:
line 10: bot_token = "XXX" - it's the HTTPAPI key
line 11: chat_id = "XXX" - it's the chat id we got from www
3. Run requirements using command:
pip install -r requirements.txt
4. Run the program 
python mywife.py

# Info
Script gets the position and size for Lineage II window.
Takes the screenshot of screen
Crops the screenshot to the contents of the window
Runs tesseract OCR to check if "To the nearest town" exist.
If exists sends notification via teleram.

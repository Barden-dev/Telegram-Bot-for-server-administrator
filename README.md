# Telegram-Bot-for-server-administrator

This bot can work on your server. When server/bot starts it sends notification.

You can reboot, shutdown server. Restart bot, get system info. 
Also you can use Wake-On-Lan functions, but you need configurate wakeonlan.sh script. 
And you can get global ip and local ip of server.

<b>To start, you need just run main.py</b>

<h3>Notes</h3>
In main.py, when bot sending message as it starts, it send message to first admin in list of admins in config.py
Function with restarting site won't work, because it needs user implementation
Function with restarting bot, works with systemctl, you need to configure service and name it tgbot.service. In raw work, this function doesn't work.

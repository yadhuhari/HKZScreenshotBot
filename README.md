# [Screenshotit_bot](https://tx.me/disneyteamscreenshotsbot)

> Telegram Bot For Screenshot Generation. Check Description for the live example 

## Added Heroku Support 😋
I had removed host in this repo so there is a less chances of heroku suspension.
For now it is not suspended by heroku but dont know when it gonna suspended.
Since i had removed host bot will download the entire file and then generate screenshots


## Description

An attempt to implement the screenshot generation of telegram files. Live version can be found here [@Screenshot_NsBot](https://t.me/Screenshot_NsBot "Screenshot Generator Bot").

## Installation Guide

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/disneyteam77/screenshot-bot)

### Prerequisites

* FFmpeg.
* Python3 (3.6 or higher).

### Local setup

> The setup given here is for a linux environment (Debian/Ubuntu).

* Clone to local machine.

``` bash
$ git clone https://github.com/odysseusmax/animated-lamp.git
$ cd animated-lamp
````

* Create and activate virtual environment.

```
$ python3 -m venv venv
$ source venv/bin/activate
```

* Install dependencies.

```
$ pip3 install -U -r requirements.txt
```

### Environment Variables

Properly setup the environment variables or populate `config.py` with the values. Setting up environment variables is advised as some of the values are sensitive data, and should be kept secret.

* `API_ID`(required) - Get your telegram API_ID from [https://my.telegram.org/](https://my.telegram.org/).

* `API_HASH`(required) - Get your telegram API_HASH from [https://my.telegram.org/](https://my.telegram.org/).

* `BOT_TOKEN`(required) - Obtain your bot token from [Bot Father](https://t.me/BotFather "Bot Father").

* `LOG_CHANNEL`(required) - Log channel's id.

* `DATABASE_URL`(required) - Mongodb database URI.

* `AUTH_USERS`(required) - Admin(s) of the bot. User's telegram id separated by space. Atleast one id should be specified.

* `SESSION_NAME`(optional) - Name you want to call your bot's session, Eg: bot's username.

* `MAX_PROCESSES_PER_USER`(optional) - Number of parallel processes each user can have, defaults to 2.

* `MAX_TRIM_DURATION`(optional) - Maximum allowed video trim duration in seconds. Defaults to 600s.

* `TRACK_CHANNEL`(optional) - User activity tracking channel's id. Only needed if you want to track and block any user. Disabled by default.

* `SLOW_SPEED_DELAY`(optional) - Delay required between each interaction from users in seconds. Defaults to 5s.

* `TIMEOUT` (optional) - Maximum time alloted to each process in seconds, after which process will be cancelled. Defaults to 1800s(30 mins).

* `DEBUG` (optional) - Set some value to use DEBUG logging level. INFO by default.

* `WORKER_COUNT` (optional) - Number of process to be handled at a time. Defaults to `20`.

### Run bot

`$ python3 -m bot`

Now go and `/start` the bot. If everything went right, bot will respond with welcome message.

## Supported commands and functions

### Commands

**General commands**

```
start - Command to start bot or check whether bot is alive.
help - Command to know about how to use bot.
settings - Command to configure bot's behavior'
set_watermark - Command to add custom watermark text to screenshots. Usage: 
---

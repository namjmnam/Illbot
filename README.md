# Illbot

## General info
This project aims to create a Telegram bot for multi-purpose uses. This bot will be used with privacy setting disabled (meaning, the bot can see any messages except for messages sent by other bots)

## Compatibility
Python version 3.6 is used, but no compatibility issue detected at the moment

## Setup
Any Python interpreter, commandline tools, terminal IDE will work.

Must create bot first.
Talk to @BotFather first then 

```
/start
/newbot
"bot name here without quotes"
"bot username here without quotes"
```

and get the HTTP API token that looks like xxxx:yyyy and replace "tokenhere" from the code.

To turn off the privacy mode:

```
/setprivacy
@"bot username here without quotes"
Disable
```

## How to use each scripts
* apireset.py
(Before usage, replace apitoken variable with the token from BotFather as string)
Use this script to reset updates. The API can be found here (replace {HTTP API} with the token):
https://api.telegram.org/bot{HTTP API}/getUpdates

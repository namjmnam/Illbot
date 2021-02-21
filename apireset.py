import requests, urllib.request, urllib.parse, json
# pip install requests
from datetime import datetime

apitoken = "tokenhere"
botapiurl = f'https://api.telegram.org/bot'+apitoken+'/getUpdates'

with urllib.request.urlopen(botapiurl) as url:
    data = json.loads(url.read().decode())

updateblock = data['result']

def resetUpdates():
    if updateblock == []: print("Update API is already empty")
    else:
        updateIDList = []
        for i in updateblock:
            sender = i['message']['from']['first_name']
            date = i['message']['date']
            # update_id = i['update_id']
            # text = i['message']['text']

            # Date to string format
            date += 9*3600 # 대한민국 시간대
            date = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

            if 'text' in i['message']: txt = date + ', ' + sender + ' : ' + i['message']['text']
            elif 'left_chat_member' in i['message']: 
                txt = date + ', ' + i['message']['left_chat_member']['first_name'] + " removed by " + sender
            elif 'new_chat_member' in i['message']:
                txt = date + ', ' + i['message']['new_chat_member']['first_name'] + " added by " + sender
            else:
                print("Error: json not valid")
                return None
            updateIDList.append(i['update_id'])

            print(txt + '\n    will be deleted')

        forgetID = max(updateIDList)
        with urllib.request.urlopen(botapiurl+'?offset='+str(forgetID+1)) as url:
            json.loads(url.read().decode())
        
        print("Reset completed")

def respondMsg():
    if updateblock == []: print("Update API is already empty")
    else:
        for i in updateblock:
            sender = i['message']['from']['first_name']
            room = i['message']['chat']['id']
            text = "Responding to " + sender

            # Issue: needs to check if the bot has access to the chatroom
            sendurl = "https://api.telegram.org/bot" + apitoken + "/sendMessage?chat_id=" + str(room) + "&text=" + urllib.parse.quote(text)
            with urllib.request.urlopen(sendurl) as url:
                json.loads(url.read().decode())
            print("Responded to " + sender + " at chat" + str(room))

# respondMsg()
resetUpdates()

import requests
import urllib
import time
import sys
import os

#if time.localtime().tm_hour != 16:
#    os._exit(0)
try:
    bot_token = sys.argv[1]
    bot_chatID = sys.argv[2]
except IndexError:
    print("not all parameters")
    os._exit(0)

URL = "https://rgooboor.by/api/v1/pages/page/21/"
response = requests.get(URL)
urlDownload = 'https://rgooboor.by/media/pages-files/'+str(response.content).split('https://rgooboor.by/media/pages-files/')[1].split('.xlsx?file=true')[0]+'.xlsx?file=true'
fileDownload = urlDownload.split('?file=true')[0].split('/')[-1]
response = requests.get(urlDownload)
open('./косуля европейская/'+urllib.parse.unquote(fileDownload), "wb").write(response.content)

def telegram_bot_sendtext(bot_message,bot_token,bot_chatID):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
telegram_bot_sendtext(str(time.localtime().tm_hour)+'  '+urllib.parse.unquote(fileDownload),bot_token,bot_chatID)


document = open('./косуля европейская/'+urllib.parse.unquote(fileDownload), "rb")
url = f"https://api.telegram.org/bot"+bot_token+"/sendDocument"
response = requests.post(url, data={'chat_id': bot_chatID}, files={'document': document})
content = response.content.decode("utf8")

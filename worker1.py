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

os.system('pip install pandas')
import pandas as pd
df = pd.read_excel('./косуля европейская/'+urllib.parse.unquote(fileDownload))
boorDict1 = dict()
cdv=5
for i in range(16):
    boorDict1['Республика Беларусь,'+df.values[2][0].split(' ')[1]+' область,'+df.values[5+i][0].strip()[:-2]+'ий район']=(df.values[5+i][1]-df.values[5+i][2])/cdv
for i in range(19):
    boorDict1['Республика Беларусь,'+df.values[24][0].split(' ')[1]+' область,'+df.values[27+i][0].strip()[:-2]+'ий район']=(df.values[27+i][1]-df.values[27+i][2])/cdv
for i in range(21):
    boorDict1['Республика Беларусь,'+df.values[49][0].split(' ')[1]+' область,'+df.values[52+i][0].strip()[:-2]+'ий район']=(df.values[52+i][1]-df.values[52+i][2])/cdv
for i in range(17):
    boorDict1['Республика Беларусь,'+df.values[76][0].split(' ')[1]+' область,'+df.values[79+i][0].strip()[:-2]+'ий район']=(df.values[79+i][1]-df.values[79+i][2])/cdv
for i in range(18):
    boorDict1['Республика Беларусь,'+df.values[99][0].split(' ')[1]+' область,'+df.values[102+i][0].strip()[:-2]+'ий район']=(df.values[102+i][1]-df.values[102+i][2])/cdv
for i in range(18):
    boorDict1['Республика Беларусь,'+df.values[123][0].split(' ')[1]+' область,'+df.values[126+i][0].strip()[:-2]+'ий район']=(df.values[126+i][1]-df.values[126+i][2])/cdv

os.system('pip install folium')
import time
from geopy.geocoders import Nominatim
import folium
from folium.plugins import MarkerCluster
world_map= folium.Map(tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(world_map)
boorDict2 = dict()
for i in boorDict1:
    time.sleep(3)
    geolocator = Nominatim(user_agent='myapplication')
    try:
        location = geolocator.geocode(i)
        print(location.raw)
    except:
        print(i)
        continue
    boorDict2[i]=[location.raw['lat'], location.raw['lon']]
boorDict0_1 = dict()
cdv=5
for i in range(16):
    boorDict0_1['Республика Беларусь,'+df.values[2][0].split(' ')[1]+' область,'+df.values[5+i][0].strip()[:-2]+'ий район']=(df.values[5+i][1]-df.values[5+i][3]-df.values[5+i][6])/cdv
for i in range(19):
    boorDict0_1['Республика Беларусь,'+df.values[24][0].split(' ')[1]+' область,'+df.values[27+i][0].strip()[:-2]+'ий район']=(df.values[27+i][1]-df.values[27+i][3]-df.values[27+i][6])/cdv
for i in range(21):
    boorDict0_1['Республика Беларусь,'+df.values[49][0].split(' ')[1]+' область,'+df.values[52+i][0].strip()[:-2]+'ий район']=(df.values[52+i][1]-df.values[52+i][3]-df.values[52+i][6])/cdv
for i in range(17):
    boorDict0_1['Республика Беларусь,'+df.values[76][0].split(' ')[1]+' область,'+df.values[79+i][0].strip()[:-2]+'ий район']=(df.values[79+i][1]-df.values[79+i][3]-df.values[79+i][6])/cdv
for i in range(18):
    boorDict0_1['Республика Беларусь,'+df.values[99][0].split(' ')[1]+' область,'+df.values[102+i][0].strip()[:-2]+'ий район']=(df.values[102+i][1]-df.values[102+i][3]-df.values[102+i][6])/cdv
for i in range(18):
    boorDict0_1['Республика Беларусь,'+df.values[123][0].split(' ')[1]+' область,'+df.values[126+i][0].strip()[:-2]+'ий район']=(df.values[126+i][1]-df.values[126+i][3]-df.values[126+i][6])/cdv
from geopy.geocoders import Nominatim
import folium
from folium.plugins import MarkerCluster
world_map= folium.Map(location=(53.8, 27),zoom_start=7)
for i in boorDict2:
    popup_text = """{}<br>
              {}<br>
              {}<br>"""
    popup_text = popup_text.format(i.split('Республика Беларусь,')[1],
                            str(int(boorDict0_1[i])*cdv),
                            str(int(boorDict1[i])*cdv)
                            )
    folium.CircleMarker(location = boorDict2[i], radius=int(boorDict0_1[i]), color='blue', fill =False).add_to(world_map)
    folium.CircleMarker(location = boorDict2[i], radius=int(boorDict1[i]), popup= popup_text, color='red', fill =True).add_to(world_map)
import datetime
t = datetime.date.today()

world_map.save(str(t.strftime('%d%m%Y'))+".html")
os.system('apt-get install -y firefox')
os.system('pip install selenium')
import io
from PIL import Image

img_data = world_map._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('image.png')

def sendImage(bot_image,bot_token,bot_chatID):
    url = "https://api.telegram.org/bot"+bot_token+"/sendPhoto";
    files = {'photo': open(bot_image, 'rb')}
    data = {'chat_id' : bot_chatID}
    r= requests.post(url, files=files, data=data)
sendImage('image.png',bot_token,bot_chatID)

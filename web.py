import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request


try:
    IMG_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.JPG'])
    TEXT_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.txt'])
    NDTV_NEWS = requests.get("https://www.ndtv.com/latest")
    NDTV_DATA = NDTV_NEWS.content
    NDTV_SOUP = BeautifulSoup(NDTV_DATA,"html.parser")  
    #WEB SCRIPTING  
    FIRST_URL = NDTV_SOUP.find_all('div', class_='news_Itm')[0].a['href']
    SECEND_URL = NDTV_SOUP.find_all('div', class_='news_Itm')[1].a['href']
    THIRED_URL = NDTV_SOUP.find_all('div', class_='news_Itm')[2].a['href']


    #DATA INPUT FROM DATA.JSON FILE
    DATA_FILE = 'data.json'
    with open(DATA_FILE) as f:
        DATA = json.load(f)
    #CHACK IF NOT URL AVALABLE FEOM DATA FILE
    if (DATA['FIRST_URL']!=FIRST_URL) and (DATA['SECEND_URL']!=FIRST_URL) and (DATA['THIRED_URL']!=FIRST_URL):
        #Requests FROM NEW NEWS URL
        NEWS_DATA = requests.get(FIRST_URL).content
        NEWS_SOUP = BeautifulSoup(NEWS_DATA,"html.parser")


        if FIRST_URL[0:21]=="https://www.ndtv.com/":
            NEWS_TITLE = NEWS_SOUP.find('h1', {'itemprop':'headline'})
            NEWS_DESCERIPTION = NEWS_SOUP.find('h2', class_="sp-descp")
            NEWS_CONTENT = NEWS_SOUP.find('div',{"itemprop":"articleBody"})
            if NEWS_CONTENT:
                
                with open("content/" + TEXT_FILE_NAME, "a") as out_file:
                    CONTENT = NEWS_CONTENT.find_all('p')
                    data = ''
                    for data in CONTENT:
                        ALL_CONTENT = (data.get_text()) 
                        out_file.writelines(data for data in ALL_CONTENT)
            NEWS_IMG = NEWS_SOUP.find('div',class_="ins_instory_dv_cont").img['src']
            if NEWS_IMG:
                
                urllib.request.urlretrieve(NEWS_IMG,'images/' + IMG_FILE_NAME)
            else:
                print("IMAGES NOT FOUND!")

            #CHAKE NEWS ALL DATA AVALABE AR NOT
            if NEWS_TITLE and NEWS_DESCERIPTION and NEWS_CONTENT:
                print("[+] UPDATE NEWS: " + NEWS_TITLE.text)
                DATA['TITLE'] = NEWS_TITLE.text
                DATA['DESCERIPTION'] = NEWS_DESCERIPTION.text    
                DATA['CONTENT'] = 'content/' + TEXT_FILE_NAME    
                DATA['IMAGES'] = 'images/' + IMG_FILE_NAME
                DATA['STATUS'] = 'E'
                DATA['UPDATE'].append({'TITLE': NEWS_TITLE.text,'DESCERIPTION':NEWS_DESCERIPTION.text,'CONTENT':'content/'+TEXT_FILE_NAME,'IMAGES': 'images/' + IMG_FILE_NAME})
            else:
                print("TITLE OR DESCRIPTION OR CONTENT TOTAL DATA ARE NOT AVALABLE....")
                print("NEW TYPE OF URL IS: " + FIRST_URL)
                print("CONTRACT DEVOLOPER +9831579787")

        
        if FIRST_URL[0:24]=="https://sports.ndtv.com/":
            NEWS_TITLE = NEWS_SOUP.find('h1', class_="sp-ttl")
            NEWS_DESCERIPTION = NEWS_SOUP.find('h2', class_="sp-descp")
            NEWS_CONTENT = NEWS_SOUP.find('div',class_="story__content")
            NEWS_IMG = NEWS_SOUP.find('div',class_="ins_instory_dv_cont").img['src']
            if NEWS_CONTENT:
                
                with open("content/" + TEXT_FILE_NAME, "a") as out_file:
                    CONTENT = NEWS_CONTENT.find_all('p')
                    data = ''
                    for data in CONTENT:
                        ALL_CONTENT = (data.get_text()) 
                        out_file.writelines(data for data in ALL_CONTENT)

            NEWS_IMG = NEWS_SOUP.find('div',class_="ins_instory_dv_cont").img['src']
            if NEWS_IMG: 
                urllib.request.urlretrieve(NEWS_IMG,'images/' + IMG_FILE_NAME)
            else:
                print("IMAGES NOT FOUND!")
            
            #CHAKE NEWS ALL DATA AVALABE AR NOT
            if NEWS_TITLE and NEWS_DESCERIPTION and NEWS_CONTENT:
                print("[+] UPDATE NEWS: " + NEWS_TITLE.text)
                DATA['TITLE'] = NEWS_TITLE.text
                DATA['DESCERIPTION'] = NEWS_DESCERIPTION.text    
                DATA['CONTENT'] = 'content/' + TEXT_FILE_NAME    
                DATA['IMAGES'] = 'images/' + IMG_FILE_NAME
                DATA['STATUS'] = 'E'
                DATA['UPDATE'].append({'TITLE': NEWS_TITLE.text,'DESCERIPTION':NEWS_DESCERIPTION.text,'CONTENT':'content/'+TEXT_FILE_NAME,'IMAGES': 'images/' + IMG_FILE_NAME})
                   
            else:
                print("TITLE OR DESCRIPTION OR CONTENT TOTAL DATA ARE NOT AVALABLE....")
                print("NEW TYPE OF URL IS: " + FIRST_URL)
                print("CONTRACT DEVOLOPER +9831579787")
        
        if FIRST_URL[0:22]=="https://food.ndtv.com/":
            NEWS_TITLE = NEWS_SOUP.find('h1', {'itemprop':'headline'})
            NEWS_DESCERIPTION = NEWS_SOUP.find('h2', class_="sp-descp")
            NEWS_CONTENT = NEWS_SOUP.find('div', class_="expand-txt")
            if NEWS_CONTENT:
                
                with open("content/" + TEXT_FILE_NAME, "a") as out_file:
                    CONTENT = NEWS_CONTENT.find_all('p')
                    data = ''
                    for data in CONTENT:
                        ALL_CONTENT = (data.get_text()) 
                        out_file.writelines(data for data in ALL_CONTENT)
                        
            NEWS_IMG = NEWS_SOUP.find('div',class_="ins_instory_dv_cont").img['src']
            if NEWS_IMG:
                IMG_FILE_NAME = "_".join([datetime.now().strftime("%y%m%d%H%M%S"),'.JPG'])
                urllib.request.urlretrieve(NEWS_IMG,'images/' + IMG_FILE_NAME)
            else:
                print("IMAGES NOT FOUND!")
            
            #CHAKE NEWS ALL DATA AVALABE AR NOT
            if NEWS_TITLE and NEWS_DESCERIPTION and NEWS_CONTENT:
                print("[+] UPDATE NEWS: " + NEWS_TITLE.text)
                DATA['TITLE'] = NEWS_TITLE.text
                DATA['DESCERIPTION'] = NEWS_DESCERIPTION.text    
                DATA['CONTENT'] = 'content/' + TEXT_FILE_NAME    
                DATA['IMAGES'] = 'images/' + IMG_FILE_NAME
                DATA['STATUS'] = 'E'
                DATA['UPDATE'].append({'TITLE': NEWS_TITLE.text,'DESCERIPTION':NEWS_DESCERIPTION.text,'CONTENT':'content/'+TEXT_FILE_NAME,'IMAGES': 'images/' + IMG_FILE_NAME})
                
            else:
                print("TITLE OR DESCRIPTION OR CONTENT TOTAL DATA ARE NOT AVALABLE....")
                print("NEW TYPE OF URL IS: " + FIRST_URL)
                print("CONTRACT DEVOLOPER +9831579787")
        
        if FIRST_URL[0:23]=="https://gadgets360.com/":
            NEWS_TITLE = NEWS_SOUP.find('div', class_="lead_heading").h1
            NEWS_DESCERIPTION = NEWS_SOUP.find('h2', class_="sdesc")
            NEWS_CONTENT = NEWS_SOUP.find('div', class_="content_text")
            if NEWS_CONTENT:
                
                with open("content/" + TEXT_FILE_NAME, "a") as out_file:
                    CONTENT = NEWS_CONTENT.find_all('p')
                    data = ''
                    for data in CONTENT:
                        ALL_CONTENT = (data.get_text()) 
                        out_file.writelines(data for data in ALL_CONTENT)
            
            #CHAKE NEWS ALL DATA AVALABE AR NOT
            if NEWS_TITLE and NEWS_DESCERIPTION and NEWS_CONTENT:
                print("[+] UPDATE NEWS: " + NEWS_TITLE.text)
                DATA['TITLE'] = NEWS_TITLE.text
                DATA['DESCERIPTION'] = NEWS_DESCERIPTION.text    
                DATA['CONTENT'] = 'content/' + TEXT_FILE_NAME    
                DATA['IMAGES'] = 'images/' + IMG_FILE_NAME
                DATA['STATUS'] = 'E'
                DATA['UPDATE'].append({'TITLE': NEWS_TITLE.text,'DESCERIPTION':NEWS_DESCERIPTION.text,'CONTENT':'content/'+TEXT_FILE_NAME,'IMAGES': 'images/' + IMG_FILE_NAME})
            else:
                print("TITLE OR DESCRIPTION OR CONTENT TOTAL DATA ARE NOT AVALABLE....")
                print("NEW TYPE OF URL IS: " + FIRST_URL)
                print("CONTRACT DEVOLOPER +9831579787")


        #UPDATE URL FROM DATA JSON
        DATA["FIRST_URL"] = FIRST_URL 
        DATA["SECEND_URL"] = SECEND_URL 
        DATA["THIRED_URL"] = THIRED_URL
        json.dump(DATA, open(DATA_FILE, "w"), indent = 2)            
    else:
        print("[+] NOT UPDATE URL PLS WATE")
            
except Exception as e:   
        print("ERROR: FROM FILE NAME web.py")  
        print(e)

exit()


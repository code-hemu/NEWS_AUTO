import json
import re

try:
    l = {" 1 ":" one "," 2 ":" two "," 3 ":" three "," 4 ":" four "," 5 ":" five "," 6 ":" six "," 7 ":" seven "," 8 ":" eight "," 9 ":" nine "," 10 ":" ten "," 100 ":" one hundred "," 1000 ":" one thousand "," 10000 ":" ten thousand "," 100000 ":" one hundred thousand ","ONE":"1","TWO":"2","THREE":"3","FOUR":"4","FIVE":"5","SIX":"6","SEVEN":"7","EIGHT":"8","NINE":"9","TEN":"10","\xa0":" ","INDIA ":"India(Bharat)","THIRD":"3rd","BEFORE":"previous","PREVIOUS":"before","AFTER":"next","NEXT":"after","NDTV":"NEEDEVERY.IN","AND":"&","SMART":"Clever","CLEVER":"SMART","DUMB":"stupid","STUPID":"dumb","BAD":"inferior","INFERIOR":"bad","AWFUL":"horrible","HORRIBLE":"awful","IMPORTANT":"essential","IRRELEVANT":"useless","USELESS":"irrelevant","INTERSTING":"fascinating","BORING":"commonplace","GOOD":"excelent","EXCELLENT":"good","EXACT":"specific","SPECIFIC":"exact","SUITABLE":"unifrom","TOTAL":"all","ALL":"total","NONE":"nothing","MAKE":"create","FIRST":"1st"," 1ST ":"first"} 

    #DATA INPUT FROM DATA.JSON FILE
    DATA_FILE = 'data.json'
    with open(DATA_FILE) as f:
        DATA = json.load(f) 

    #DATA JSON FILE SELECT ITEM   
    TITLE = DATA['TITLE']
    DESCERIPTION = DATA['DESCERIPTION']
    CONTENT = DATA['CONTENT']
 
    pattern = '|'.join(sorted(re.escape(k) for k in l))
    NEWS_TITLE = re.sub(pattern, lambda m: l.get(m.group(0).upper()), TITLE, flags=re.IGNORECASE)
    NEWS_DESCERIPTION = re.sub(pattern, lambda m: l.get(m.group(0).upper()), DESCERIPTION, flags=re.IGNORECASE)

    POST_FILE = 'post.json'
    with open(POST_FILE) as POST_DATA:
        POST = json.load(POST_DATA)
    POST["TITLE"] = NEWS_TITLE
    POST['DESCROPTION'] = NEWS_DESCERIPTION
    print("[+] NEW TITLE: "+ NEWS_TITLE)
    print("[+] NEW DESCERIPTION: "+ NEWS_DESCERIPTION)
    print("[+] CONTENT")
    with open(CONTENT) as CONTENT_DATA:
       lines = CONTENT_DATA.read()
       NEWS_CONTENT = re.sub(pattern, lambda m: l.get(m.group(0).upper()),  lines, flags=re.IGNORECASE)
       print(NEWS_CONTENT)
       POST['CONTENT'] = NEWS_CONTENT
    
    json.dump(POST, open(POST_FILE, "w"), indent = 2) 

    DATA['STATUS'] = 'U'
    json.dump(DATA, open(DATA_FILE, "w"), indent = 2)  

except Exception as e:   
        print("ERROR FROM FILE NAME edit.py: ")  
        print(e)
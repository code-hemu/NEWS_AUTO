import httplib2
import json
from googletrans import Translator
from apiclient.discovery import build
from oauth2client.file import Storage

def get_credentials():
    STORAGE = Storage('credentials.dat')
    credentials = STORAGE.get()
    if credentials is None or credentials.invalid:
        print("CREATE 'credentials.dat' USE python api.py")
    return credentials

try:
    POST_FILE = 'post.json'
    with open(POST_FILE) as POST_DATA:
        POST = json.load(POST_DATA)
    
    hindi_translator_c = Translator()
    HTNDI_CONTENT = hindi_translator_c.translate(POST['CONTENT'],src='en', dest='hi')
    hindi_translator_t = Translator()
    HTNDI_TITLE = hindi_translator_t.translate(POST['TITLE'],src='en', dest='hi')
    hindi_translator_d = Translator()
    HTNDI_DESCROPTION = hindi_translator_d.translate(POST['DESCROPTION'],src='en', dest='hi')

    
    b_translator_c = Translator()
    BANGOLI_CONTENT = b_translator_c.translate(POST['CONTENT'],src='en', dest='bn')
    b_translator_t = Translator()
    BANGOLI_TITLE = b_translator_t.translate(POST['TITLE'],src='en', dest='bn')
    b_translator_d = Translator()
    BANGOLI_DESCROPTION = b_translator_d.translate(POST['DESCROPTION'],src='en', dest='bn')


    if POST["IMAGES"]:
        HINDI_CONTENT = "<h3>"+HTNDI_DESCROPTION.text+"</h3><div class='separator' style='clear: both;'><a href='' style='display: block; padding: 1em 0; text-align: center; '><img alt='"+HTNDI_TITLE.text+"' border='0' data-original-height='836' data-original-width='1254' src='"+POST["IMAGES"]+"'/></a></div><p>"+HTNDI_CONTENT.text+"</p>"

        BANGOLI_CONTENT = "<h3>"+BANGOLI_DESCROPTION.text+"</h3><div class='separator' style='clear: both;'><a href='' style='display: block; padding: 1em 0; text-align: center; '><img alt='"+BANGOLI_TITLE.text+"' border='0' data-original-height='836' data-original-width='1254' src='"+POST["IMAGES"]+"'/></a></div><p>"+BANGOLI_CONTENT.text+"</p>"

        ENGLISH_CONTENT = "<h3>"+POST['DESCROPTION']+"</h3><div class='separator' style='clear: both;'><a href='' style='display: block; padding: 1em 0; text-align: center; '><img alt='"+HTNDI_TITLE.text+"' border='0' data-original-height='836' data-original-width='1254' src='"+POST["IMAGES"]+"'/></a></div><p>"+POST['CONTENT']+"</p>"


    else:
        HINDI_CONTENT = "<h3>"+ HTNDI_DESCROPTION.text +"</h3><p>"+ HTNDI_CONTENT.text +"</p>"
        BANGOLI_CONTENT = "<h3>"+ HTNDI_DESCROPTION.text +"</h3><p>"+ HTNDI_CONTENT.text +"</p>"
        ENGLISH_CONTENT = "<h3>"+POST['DESCROPTION']+"</h3><p>"+POST['CONTENT']+"</p>"
       
    """Returns an authorised blogger api service."""
    credentials = get_credentials()
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('blogger', 'v3', http=http)
    posts = service.posts()


    hindi_body = {
            "title": HTNDI_TITLE.text,
            "content": HINDI_CONTENT,
            "labels"  : "test_post,test,post",
            
        } 
    bangla_body = {
            "title": BANGOLI_TITLE.text,
            "content": BANGOLI_CONTENT,
            "labels"  : "test_post,test,post",
            
        }   

    english_body = {
            "title": POST['TITLE'],
            "content": ENGLISH_CONTENT,
            "labels"  : "test_post,test,post",
            
        }
    
    english_insert = posts.insert(blogId='5813569594685204437', body=english_body).execute()#needevery.in
    hindi_insert = posts.insert(blogId='1269206445428046340', body=hindi_body).execute()#hindi.needevery.in
    bangla_insert = posts.insert(blogId='2292694093942997317', body=bangla_body).execute()#bangoli.needevery.in

    

    print(english_insert['url'])
    print(hindi_insert['url'])
    print(bangla_insert['url'])
    
    # with open("data.csv", "a+") as file:
    #     file.write("\n"+Post_url+"," )   

except Exception as e:   
        print("ERROR FROM FILE NAME blogger.py: ")  
        print(e) 
 

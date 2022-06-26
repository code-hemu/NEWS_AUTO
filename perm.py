import json
from Google import Create_Service

try:
    CLIENT_SECRET_FILE = 'client-secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    #DATA INPUT FROM DATA.JSON FILE
    DATA_FILE = 'data.json'
    with open(DATA_FILE) as f:
        DATA = json.load(f)
    with open('image.json') as IMAGE_FILE_DATA:
        UPLOAD_DATA = json.load(IMAGE_FILE_DATA)
    if UPLOAD_DATA['id']:
        # Update Sharing Setting
        file_id = UPLOAD_DATA['id']

        request_body = {
            'role': 'reader',
            'type': 'anyone'
        }

        response_permission = service.permissions().create(
            fileId=file_id,
            body=request_body
        ).execute()

        # Print Sharing URL
        response_share_link = service.files().get(
            fileId=file_id,
            fields='webViewLink'
        ).execute()
        print("[+] "+response_share_link)

        POST_FILE = 'post.json'
        with open(POST_FILE) as POST_DATA:
            POST = json.load(POST_DATA)
        POST['IMAGES'] = "https://lh3.googleusercontent.com/d/"+ file_id  
        print("[+] https://lh3.googleusercontent.com/d/"+ file_id)
        json.dump(POST, open(POST_FILE, "w"), indent = 2) 
        
        DATA['STATUS'] = 'B'
        json.dump(DATA, open(DATA_FILE, "w"), indent = 2)  
        
    else:
        print("IMAGE ID NOT AVALABLE!")

except Exception as e:   
    print("ERROR FROM FILE NAME upload.py: ")  
    print(e)
	
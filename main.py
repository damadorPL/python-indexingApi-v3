from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
'''
url = "url do zaindeksowania"
'''
print("Podaj adres do zaindeksowania")
url = str(input())
split = ","
if split in url:
    urls = url.split(", ")
else:
    urls = url.split(",")
'''
JSON_KEY_FILE = "scieżka do pliku z kluczem api"
'''
JSON_KEY_FILE = "nazwa_pliku.json"

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# Autoryzacja klucza API
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

# Wysłanie requestu
'''
URL_UPDATED - aktualizacja urla
URL_DELETED - usunięcie urla z indeksu
Wystarczy zmienić poniższy 'type'
'''
for url in urls:
    content = {}
    content['url'] = url
    content['type'] = "URL_UPDATED"
    json_content = json.dumps(content)
    print(content)
    response, content = http.request(ENDPOINT, method="POST", body=json_content)
    result = json.loads(content.decode())

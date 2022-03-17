from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

class ToMuchURLS:
    """Wyjątek gdy adresów jest więcej niż 100"""


'''
url = "url do zaindeksowania"
'''
print("Podaj adres do zaindeksowania (max 100), odzielone przecinkiem.")
url = str(input())
split = ","
if split in url:
    urls = url.split(", ")
else:
    urls = url.split(",")
"""
Poniższe ograniczenie można zwiększyć, jeśli został zwiększony limit w Indexing Api w GCP.
"""
if len(urls) > 100:
    raise ToMuchURLS('Za dużo adresów URL, maksymalnie 100')
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
    send_url = {}
    send_url['url'] = url
    send_url['type'] = "URL_UPDATED"
    json_content = json.dumps(send_url)
    print(send_url)
    response, send_url = http.request(ENDPOINT,
                                      method="POST",
                                      body=json_content)
    result = json.loads(send_url.decode())

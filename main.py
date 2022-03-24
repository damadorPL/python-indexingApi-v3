from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

class TooManyURLs:
    """Wyjątek gdy adresów jest więcej niż 100"""

class StopApp:
    """Wyjątek zatrzymujący aplikację podczas złego wyboru z menu"""

print('Wybierz jedną z dwóch opcji:\n1. Aktualizacja URLi - Przesłanie do indeksu\n2. Usunięcie adresów URL z indeksu')
option = input('Wybierz 1/2:')

if option == "1":
    choice = "URL_UPDATED"
elif option == "2":
    choice = "URL_DELETED"
else:
    raise StopApp("Wybrałęś złą opcję")

'''
if dzielący listę adresów na listę. 
'''
print("Podaj adresy (max 100), odzielone przecinkiem.")
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
    raise TooManyURLs('Za dużo adresów URL, maksymalnie 100')
'''
JSON_KEY_FILE = "scieżka do pliku z kluczem api, domyślna nazwa pliku indexing_api_key.json"
'''
JSON_KEY_FILE = "indexing_api_key.json"

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# Autoryzacja klucza API
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

# Wysłanie requestu
'''
URL_UPDATED - aktualizacja urla
URL_DELETED - usunięcie urla z indeksu
'''
for url in urls:
    send_url = {}
    send_url['url'] = url
    send_url['type'] = choice
    json_content = json.dumps(send_url)
    print(send_url['url'], " --> ", send_url['type'])
    response, send_url = http.request(ENDPOINT,
                                      method="POST",
                                      body=json_content)
    result = json.loads(send_url.decode())

import requests

response = requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)

dosya = open("usom.txt","a")
dosya.write(str(response.content))
dosya.close
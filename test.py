import requests

url='https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/comm'
headers= {
    'x-rapidapi-key': '4309cbe9e5msh69d6d9f465b9939p10ca40jsn47eb7087c12b',
    'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
  }

response = requests.get(url,headers=headers)
print(response.json())

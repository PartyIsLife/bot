
try:
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Bishkek&lang=RU&appid=25be154c3da87b2c00e32167e066bd1a')
    j = r.json()
    print(j['weather'][0]['main'])
except:
   print('error')

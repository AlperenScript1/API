import requests  #? HTTP istekleri (GET, POST vb.) göndermek için kullanılır


#! ==TOKEN OLMADAN API KULLANIMI (En sade, temel yapı)==
url = "https://api.collectapi.com/weather/getWeather"  #! API Aldığımız sayfanın adresi (API key değil)

#? API’nin kabul ettiği parametreler burada dictionary (sözlük) olarak verilir. URL’in sonuna ?key1=val1&key2=val2 olarak eklenen değerlerin Python karşılığıdır. 
#? Örnek: Bir hava durumu API’si “şehir” ve “dil” isterse, bunlar params içinde verilir.
params = {
    "city": "Ankara",   
    "lang": "tr"        
}

#? API GET isteği gönderiyor. (Token olmadığı için headers yok)
response = requests.get(url, params=params)

#? Gelen JSON metnini Python dict/list yapısına çeviriyoruz
data = response.json()

#? Çıktıyı yazdırıyoruz (istersen silebilirsin)
print("Tokensiz API sonucu:")
print(data)

#TODO:Kısaca temel yapı:
#requests kütüphanesini import et → HTTP isteği göndermek için.
#URL belirle → Hangi API’den veri çekileceğini gösterir.
#Params belirle → API’nin istediği parametreler (şehir, dil vb.).
#GET isteği gönder → requests.get(url, params=params).
#JSON olarak al → .json() ile Python objesine çevir.


#! ==TOKEN (API KEY) İLE API KULLANIMI==
url = "https://api.collectapi.com/weather/getWeather"  

#? Aynı parametreleri tekrar kullanıyoruz
params = {
    "city": "Ankara",
    "lang": "tr"
}

#? Token gerekiyorsa → headers içine eklenir.
#? Format CollectAPI'de:    authorization: "apikey SENIN_KEYIN"
headers = {
    "authorization": "apikey 7Ac19FT2JWYeUn5FkQCXap:1X3nal4BYGB0gNtST2k3MI",
    "content-type": "application/json"
}

#? Bu sefer headers + params ikisi birden gönderiliyor
response = requests.get(url, params=params, headers=headers)

#? JSON'u yine Python’a çeviriyoruz
data = response.json()

print("Tokenli API sonucu:")
print(data)
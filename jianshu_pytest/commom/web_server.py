from suds.client import Client

# http://ws.webxml.com.cn/WebServices/WeatherWS.asmx
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
print(client)
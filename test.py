import jwt
import requests
from datetime import datetime, timedelta
requests.packages.urllib3.disable_warnings()

payload = {
    'GUAC_ID': 'connection_id',
    'guac.hostname': '127.0.0.1',
    'guac.protocol': "vnc",
    'guac.port': '5901',
    'guac.password': 'password',
    'exp': datetime.utcnow() + timedelta(seconds=3600)
}


jwtToken = jwt.encode(payload, 'PR8R4UA4L16JYJMGI5LD6QSG8EK0XIW2W73AB6RIKNIZ7VIOGK32VXZF4SE9VWB2IQ7J44Q1TG6UUYV9IV5RREVTMN5H990DWHYEPZGVIIUYZZU3AFHDHZI82QVPVG4JAOXLI1UFTN4KNEHOFN3PIPLKK6CV5VJSV3A2KU7HKKFNI86CWEJEGGSB27C4WD3KHJ3S2OF81IDLFKH0C7USZ4MFWPHHE1E7LHRB3WSDKOF6F7414612NIB3S3OOZRC8', algorithm="HS512")

print(jwtToken)
resp = requests.post('http://localhost:8080/guacamole/api/tokens', data={'token': jwtToken}, verify=False)

print(resp.text)

from base64 import encode
import os
import sys
import urllib.request
client_id = "8zgHSJ0ruj05fbxsqm0x"
client_secret = "XQ0Uay6KBN"
encText = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    encoded_text = response_body.decode('utf-8')
    print(encoded_text)
else:
    print("Error Code:" + rescode)


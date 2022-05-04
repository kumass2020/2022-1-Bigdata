import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd

ServeceKey = 'qY0r9GRf5VlSv6JpVhANeqiWBw4%2BviV7%2F9zc7ajMI2Of1CQY4y4hB1WuhU1gWg0XTTq3ViwAAeagnTESA%2FtYTg%3D%3D'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
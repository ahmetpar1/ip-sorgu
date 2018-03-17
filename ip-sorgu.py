#!/usr/bin/python3
import urllib.request

baglan = urllib.request.urlopen("http://icanhazip.com/")
cıktı = baglan.read()
cıktı = cıktı.decode("utf-8")
cıktı = cıktı.strip("\n")

print (cıktı)
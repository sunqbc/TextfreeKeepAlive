#coding: utf-8

from textnow import textnow_sms
import os

username = os.environ["TEXTNOW_USERNAME"]
password = os.environ["TEXTNOW_PASSWORD"]
numbers = os.environ["TEXTNOW_NUMBER"]
msg = os.environ["TEXTNOW_MSG"]
#text = textnow_sms.Textnow(username, password, numbers, msg)

#text.send_text()

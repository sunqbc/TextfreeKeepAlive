#coding: utf-8

from textfree import textfree_sms
import os

username = os.environ["TEXTNOW_USERNAME"]
password = os.environ["TEXTNOW_PASSWORD"]
numbers = os.environ["TEXTNOW_NUMBER"]
msg = os.environ["TEXTNOW_MSG"]
text = textfree_sms.textfree(username, password, numbers, msg)

text.send_text()

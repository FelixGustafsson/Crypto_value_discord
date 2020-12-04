import requests
from bs4 import BeautifulSoup
import discord
from discord import Webhook, RequestsWebhookAdapter, File

WEBHOOK_URL = ''
WEBHOOK_ID = ''
whitelist = [
    'div'
]

# Code for Bitcoin

url = 'https://www.coindesk.com/price/bitcoin'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
outputb = []

for t in text: 
    if t.parent.name in whitelist:
        outputb.append(t)

messageb1 = outputb[31]
messageb2 = outputb[32]

webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_URL,\
 adapter=RequestsWebhookAdapter())

webhook.send('**Bitcoin:**\nPrice for 1 Bitcoin right now: {} $ \nPercentage last 24h: {}'.format(messageb1, messageb2))

# Code for Ethereum

url = 'https://www.coindesk.com/price/ethereum'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
outpute = []

for t in text: 
    if t.parent.name in whitelist:
        outpute.append(t)

messagee1 = outpute[36]
messagee2 = outpute[37]

webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_URL,\
 adapter=RequestsWebhookAdapter())

webhook.send('**Ethereum:**\nPrice for 1 Ethereum right now: {} $ \nPercentage last 24h: {}'.format(messagee1, messagee2))

# Code for XRP

url = 'https://www.coindesk.com/price/xrp'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
outputx = []

for t in text: 
    if t.parent.name in whitelist:
        outputx.append(t)

messagex1 = outputx[41]
messagex2 = outputx[42]

webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_URL,\
 adapter=RequestsWebhookAdapter())

webhook.send('**XRP:**\nPrice for 1 XRP Right now: {} $ \nPercentage last 24h: {}\n----------------------------------'.format(messagex1, messagex2))



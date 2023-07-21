import time
import datetime
import random
import sqlite3
import threading
import json, re, sys
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import secrets
import requests
import urllib.parse



key = b64decode("jq1qlNmRamRjcfptuC+rPZlFvOxDoTLeUOCpuy9gsjY=")
iv = get_random_bytes(AES.block_size)

def encrypt(data):
  iv = get_random_bytes(AES.block_size)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'), 
    AES.block_size)))


s = requests.Session()

pid = '76725'

deviceId = secrets.token_hex(8)

productId = pid

toEncrypt = f"authtoken=2GEsAf8a9JoFnaRchLTaf&ref={productId}&os_type=android&os_version=29&app_version=4.5.4&device_id={deviceId}&device_model=Googlesargo&token_id="

toEncrypt2 = 'authtoken=2GEsAf8a9JoFnaRchLTaf&panier={"context":{"proposition_ope":null,"tableau_code_promo":[],"code_magasin":"","nombre_operation":null,"megacarte_classe":"","megacarte":0,"panier":[{"ref":"76725","prix":1.00,"type_transaction":"Vente","quantite":1}],"tableau_code_promo_trouve":null},"livraison":{"selectedTransport":{"titre":"Livraison en magasin","price":0,"type":"micromania","relaisid":null}},"cmdid":-1,"emballageCadeau":{"prixEmballageCadeau":0.0,"emballageCadeauSelected":false},"avantages":null,"paiement":{"totalTTC":1.00,"cb":1.00,"bonAchat":null,"carteCadeau":null},"coordonnees":{"megacarte":"","email":"","creationMegacarte":false,"adresseLivraison":null,"adresseFacturation":null},"header":null,"horaires":""}&os_type=android&os_version=25&app_version=4.5.4&device_id=75a9f61d383c13f8&device_model=samsungdream2qltezh&token_id=&email=lucasdup@gmail.com'
encryptedparams = encrypt(toEncrypt2).decode('utf-8')

encoded = urllib.parse.quote_plus(encryptedparams)

produrl = f"http://gameup.com/micromania.fr/webservapp/ajout_panier.php?authtoken={encoded}"

headers1 = {
"Connection": "Keep-Alive",
"Cookie": "SERVERIDGAMEUP=APP03",
"Cookie2": "$Version=1",
"Accept-Encoding": "gzip",
"Host": "gameup.com",
"Content-Length": "0"
}

r = requests.get(produrl, headers=headers1)

print(r.text)

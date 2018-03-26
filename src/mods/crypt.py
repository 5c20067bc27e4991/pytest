#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

cont = 'Hello'

with open('id_rsa', 'r') as rsa_key:
    rsa_cont = rsa_key.read()

priKey = RSA.importKey(rsa_cont)
signer = PKCS1_v1_5.new(priKey)
hash_obj = MD5.new(cont.encode('utf-8'))
signature = base64.b64encode(signer.sign(hash_obj))
# print(signature)


with open('id_rsa.pub', 'r') as rsa_pub:
    rsa_cont = rsa_pub.read()
pubKey = RSA.importKey(rsa_cont)
h = MD5.new(cont.encode('utf-8'))
verifier = PKCS1_v1_5.new(pubKey)
if verifier.verify(h, base64.b64decode(signature)):
    print("Verify signature successfully.")
else:
    print('Invalid signature!')
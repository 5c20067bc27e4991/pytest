#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

cont = 'Hello'
rsa_file = 'id_rsa'
rsa_pub_file = 'id_rsa.pub'


def sign(rsa_file, cont):
    with open(rsa_file, 'r') as rsa_key:
        rsa_cont = rsa_key.read()

    priKey = RSA.importKey(rsa_cont)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = MD5.new(cont.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature


def veri_sign(rsa_pub_file, cont, signature):
    with open(rsa_pub_file, 'r') as rsa_pub:
        rsa_cont = rsa_pub.read()
    pubKey = RSA.importKey(rsa_cont)
    h = MD5.new(cont.encode('utf-8'))
    verifier = PKCS1_v1_5.new(pubKey)
    if verifier.verify(h, base64.b64decode(signature)):
        print("Verify signature successfully.")
    else:
        print('Invalid signature!')

SIGN1 = sign(rsa_file, cont)
veri_sign(rsa_pub_file, cont, SIGN1)
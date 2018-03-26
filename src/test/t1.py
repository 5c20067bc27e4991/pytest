#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import base64
from Crypto.PublicKey import RSA

privateKey = '''MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAOG/8J9TP8cN7upNoZ+LoBs9xImv
4hHAwO/gq7TLGjZ5IoUIxWPJbGtUI+muXsFf8tBfjE3p86ava1R1Ji0c0Sh98bPT4lFMqGFWV5OJ
d2VbvLGG4DclFzkZxMuB4M7sSvXlKdfawHuFFG/HiEEzjuiROfqWlP3qZ6Ix0QLRhE9HAgMBAAEC
gYBdPujnBn3rfIfY4+QEgKnLVsIdlTat2o5XBtglv1a+dV6a0LqnswVDd+e1mD6vZTBofW74p8/q
Y77TjegM7kA90Nw9N4z2uuhn7kXFNI+RiA2MUXcqf4Vwb/64wRpqH70abZzCuyhxQYXqNqEmJuL4
jAxMoxztxj4BvXt5zk9ekQJBAPLwghERrLNgu+ty/Fmdk15NWE/Eoazig15THPEgrZ5Ruaq90U9O
4sTWbYgDLYJI75uDTgFoPE+VHkT40WspYZMCQQDt4tsPwVHtXEX4sYclEAbWzXEYDlNXCA3zvWf6
9cb9N+oY4FfMuThFdfpC5H2D+5bhqCRLZUzuvthS7i18ljv9AkEApJkFVvFFtIc+60iN513XAhaf
VfRgohUacqcXPdwpJdIzXJadIQHOrRSnQ3b7t4EZLqFpEZUA/96Fkq+Om+9+lwJBAK0fjwt9RrF2
mNmv4UnAyyliZC78pfxNuVGsg1LpsYKxQaYPBvbPyTsL7DDodswpuhnJs3hHZeDOdUKNYf8smsUC
QDhQqQHjf6Kf9ZI/zO6Ldvn0y5cMomzfFaH8ltRcjuNB8num1Vt0Oyk+k90q+OYak5twRvKGGsQD
8v+gOIQ8ZfA='''

private_keyBytes = base64.b64decode(privateKey)
print(private_keyBytes)
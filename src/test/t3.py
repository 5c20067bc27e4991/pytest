#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import socket


def test(t):
    return json.dumps(t)

print(test([1, 2, 3]))
print(type(json.dumps([1, 2, 3])))

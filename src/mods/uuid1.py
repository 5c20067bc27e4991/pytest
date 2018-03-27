#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uuid

print(uuid.uuid1())
print(len(str(uuid.uuid1())))
# f727f2be-316a-11e8-948d-005056c00001

print(uuid.uuid3(uuid.NAMESPACE_DNS, 'test'))
# 45a113ac-c7f2-30b0-90a5-a399ab912716

print(uuid.uuid4())
# 606b7662-8c28-46b5-9bc1-91fd47dae741

print(uuid.uuid5(uuid.NAMESPACE_DNS, 'test'))
# 4be0643f-1d98-573b-97cd-ca98a65347dd

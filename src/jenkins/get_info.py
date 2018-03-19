#!/usr/bin/env python
import os

JOB_NAME = os.system("echo $JOB_NAME")

print(JOB_NAME)
print(os.environ)

#!/usr/bin/env python3

import requests
import time
import json
import logging
import json
import sys
import os
from datetime import datetime

try:
   # Load configs.json
   configs = json.load(open(os.getcwd() + '/config.json'))

   api = configs['api']
   filepath = configs['filepath']
   filepath = configs['filepath']
   refresh_rate_in_seconds = configs['refresh_rate_in_seconds']
   print("Starting script with", refresh_rate_in_seconds, "s delay")

   while True:
      multiple_files = [('myfile', ('file.dat', open(filepath, 'rb')))]
      resp = requests.post(api, files=multiple_files)
      if resp.status_code == 200:
         print(datetime.now(), " - File uploaded with success")
      else:
         print(datetime.now(), " - Failed ", filepath)
      time.sleep(refresh_rate_in_seconds)

except Exception as e:
   logging.error('Error at %s', 'division', exc_info=e)

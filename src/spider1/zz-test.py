#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import urllib2

baseurl = 'https://fr.tlscontact.com/cn/BJS/ajax/document.php/'
hd = {
    # 'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.888',
    # 'Cookie': 'TLScontact=9443c824b2df9eb917a62062f6169357; TLScontact=d9bda97166462ce70984010bf9ea8b2c; uid=Cls0EFryvpOlRQvEBHvLAg==; TLScontact=9fba4bfbff4b189ff474db945a5dd69f; _ga=GA1.2.104976181.1525859119; _gid=GA1.2.1891533135.1525859119',
    'Cookie':'TLScontact=a2db1faa89ae4e2a0e0f7eef37c20a84; uid=CltUFlrPKDiKvUWvAyeLAg==; _ga=GA1.2.527295509.1523525689; _gid=GA1.2.248851365.1525835027; TLScontact=d38ef54c185db0646a8b8729d9e50d69',
    'Host': 'fr.tlscontact.com',
    'Referer': 'https://fr.tlscontact.com/cn/BJS/myapp.php?fg_id=4273644'
}

args = {'f_id': '6052972',
      'doc_type': 'application_form_original',
      'process': 'document_download',
      '_sid': '174d3c2fce9fc427780f56b705630786'
        }
args = urllib.urlencode(args)
request = urllib2.Request(baseurl + args, headers=hd)
# request.add_header('header1', 'hehe')
reponse = urllib2.urlopen(request)
print(request.get_full_url())

# print(request.get_header('User-Agent'))
# print(request.get_header('Header1'))
print(reponse.code)
html = reponse.read()
with open('zz.html', 'w') as f:
    f.write(html)

print('Done!')

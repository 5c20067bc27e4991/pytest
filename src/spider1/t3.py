import urllib2    
req = urllib2.Request('https://www.baidu.com')
response = urllib2.urlopen(req)    
the_page = response.read()    
print the_page

request = urllib2.Request(baseurl + search_url, headers=UA)
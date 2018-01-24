# -*- coding: utf-8 -*-
'''
Created on 2017年4月6日
@author: guanglin
'''
##HTMLParser示例：获取人人网首页上的各各链接地址 
#coding: utf-8 
from htmlentitydefs import entitydefs 
import HTMLParser,urllib,urllib2
def getimage(addr): 
    u = urllib2.urlopen(addr)
    data = u.read() 
    filename=addr.split('/')[-1] 
    f=open(filename,'wb') 
    f.write(data) 
    f.close() 
    print filename+'已经生成！' 
class TitleParser(HTMLParser.HTMLParser): 
    def __init__(self): 
        self.taglevels=[] 
        self.handledtags=['a'] 
        self.processing=None 
        self.linkstring='' 
        self.linkaddr='' 
        HTMLParser.HTMLParser.__init__(self)        
    def handle_starttag(self,tag,attrs): 
        if tag in self.handledtags: 
            for name,value in attrs: 
                if name=='href': 
                    self.linkaddr=value 
            self.processing=tag 

    def handle_data(self,data): 
        if self.processing: 
            self.linkstring +=data 
            #print data.decode('utf-8')+':'+self.linkaddr 
    def handle_endtag(self,tag): 
        if tag==self.processing: 
            print self.linkstring.decode('utf-8')+':'+self.linkaddr 
            self.processing=None 
            self.linkstring='' 
    def handle_entityref(self,name): 
        if entitydefs.has_key(name): 
            self.handle_data(entitydefs[name]) 
        else: 
            self.handle_data('&'+name+';') 

    def handle_charref(self,name): 
        try: 
            charnum=int(name) 
        except ValueError: 
            return 
        if charnum<1 or charnum>255: 
            return 
        self.handle_data(chr(charnum)) 

    def gettitle(self): 
        return self.linkaddr 
tp=TitleParser() 
tp.feed(urllib2.urlopen('http://www.renren.com/').read())
# import pymysql

import urllib.request

import sys

#from bs4 import BeautifulSoup

#from lxml import etree

import lxml.html



# conn = pymysql.connect(host="127.0.0.1",port=3307, user="root",password="123456",database="myvideos")

# cursor = conn.cursor()

# sql = "INSERT INTO `video` (`str_id`, `title`, `video_href`, `img_src`, `episodes`, `type_id`, `group_id`, `year`, `area`, `score`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

# a=0

# cursor.execute(sql, [a,"呵呵呵",a,a,a,a,a,a,a,a])

# conn.commit()

# cursor.close()

# conn.close()

class myTest:

      def __init__(self):
        a=0

      def getlist(url):

        # url="https://v.youku.com/v_show/id_XNDI3Nzc0OTgyMA==.html"




        req = urllib.request.Request(url)

        webpage = urllib.request.urlopen(req)

        html = webpage.read()

        etree = lxml.html.etree

        element = etree.HTML(html)




        # film=element.xpath('//div[contains(@class,"video-status")]//span/text()')
        #
        # slow=element.xpath('//div[contains(@class,"hehehe")]')
        #
        # #电影
        # try:
        #   mystring=str(film)
        #   aaa=mystring[0:len(mystring)]
        #   return "success"
        # except:
        #    return None


        #电视剧
        items=element.xpath('//span[contains(@class,"video-status")]/span/text()') #总集数


        upd=element.xpath('//span[contains(@class,"video-status")]/span/span/text()') #未更新集数




        try:
         myString=str(items)
         begin=myString.index("共")
        except:
           return None



        sum=int(myString[begin+1:len(myString)-3])

        update=sum
        if(upd!=None):
          upd=str(upd)
          if(upd!="[]"):
           update=upd[2:len(upd)-2]

        # print("总:"+str(sum)+"更:"+str(update))

        return [sum,update]




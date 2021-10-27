import pymysql

import urllib.request

import json

from myTest import myTest

from getEpisode import getEpisode

conn = pymysql.connect(host="127.0.0.1",port=3307, user="root",password="123456",database="myblog")

cursor = conn.cursor()
number=0
useful=0
insert=0

begin=1
for i in range(1,1000):

   # url="https://list.youku.com/category/page?c=97&a=&s=4&d=1&type=show&p="+str(i)

   url="https://list.youku.com/category/page?c=96&a=%E6%B3%B0%E5%9B%BD&s=4&type=show&p="+str(i)

   # url="https://list.youku.com/category/page?c=97&a=&s=2&d=1&type=show&p="+str(i)

   # url="https://list.youku.com/category/page?c=96&type=show&p="+str(i)  #电影

   # url="https://list.youku.com/category/page?c=96&s=5&type=show&p="+str(i)  #电影

   # url="https://list.youku.com/category/page?c=100&u=&s=5&type=show&p="+str(i)  #动漫

   req = urllib.request.Request(url)

   theJson=urllib.request.urlopen(req)

   myJson=json.loads(theJson.read())

   if(len(myJson['data'])<=0):
       print("最后一页:"+str(i))
       break
   for msg in myJson['data']:
    try:
     img=msg['img']
     title=msg['title']
     videoId=msg['videoId']
     videoLink="//v.youku.com/v_show/id_"+msg['videoId']+".html"
    except:
        print("当前页数："+str(i)+"出错")
        number=number+1
        continue
    number=number+1
    # mylist=myTest.getlist("http:"+str(videoLink))
    # if(mylist!=None):
    print(title+"，当前页数:"+str(i))
    useful=useful+1
    sql="INSERT INTO `video` (`video_id`, `title`, `img_src`, `episodes`, `updates`, `type_id`) VALUES (%s,%s,%s,%s,%s,%s)"

    flag=0
    try:
           cursor.execute(sql, [videoId,title,img,1,1,2])
           conn.commit()
           insert=insert+1
    except:
           conn.rollback()
           flag=1
       # if flag==0:
       #     print("正在插入集数")
       #
       #     sql1="SELECT `v_id` FROM `video` where `video_id`=%s"
       #
       #     cursor.execute(sql1,[videoId])
       #
       #     v_id=cursor.fetchall()
       #
       #     getEpisode.getlist(title,v_id,mylist[1])
    # else:
    #     print("无效，当前页数"+str(i))


    # 电视剧
    # if(mylist!=None):
    #  print(title)
    #  print(mylist[0])
    #  print(mylist[1])
    #  useful=useful+1
    #  sql="INSERT INTO `video` (`video_id`, `title`, `video_href`, `img_src`, `episodes`, `update`, `type_id`) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    #  try:
    #   cursor.execute(sql, [videoId,title,videoLink,img,mylist[0],mylist[1],1])
    #   conn.commit()
    #   insert=insert+1
    #  except:
    #      conn.rollback()
     # print(img+","+title+","+videoId+","+videoLink)


print("总："+str(number)+"有效:"+str(useful)+"插入成功:"+str(insert))
cursor.close()
conn.close()

# mylist=myTest.getlist("https://v.youku.com/v_show/id_XNDIzMjcyNjUwNA==.html")

# print(mylist[0])
# print(mylist[1])
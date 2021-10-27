import pymysql
import json as Json
from selenium import webdriver as WebDriver
import requests




class yuxueyuan():


  def __init__(self):
    a=0




  def getCookie(self,name,value):
     return {
       'domain': '.drcuiyutao.com',
       'name': name,
       'value': value,
       'path': '/',
       'expires': None,
       'httpOnly': False,
       'HostOnly': False,
       'Secure': False,
     }

  def getWechatCookie(self,name,value):
    return {
      'domain': '.weixin.qq.com',
      'name': name,
      'value': value,
      'path': '/',
      'expires': None,
      'httpOnly': False,
      'HostOnly': False,
      'Secure': False,
    }

y = yuxueyuan()


# 进入浏览器设置
# options = WebDriver.ChromeOptions()
# 设置中文
#options.add_argument('Host="weixin.drcuiyutao.com"')
#options.add_argument('Connection="keep-alive"')
#options.add_argument('Accept="application/json, text/plain, */*"')
#options.add_argument('Referer="https://weixin.drcuiyutao.com/yxy-edu-web/evaluation?evaluationTypeCode=d2c3eaf4ea9e42ae98c78d3a154b8ec5&eScFrom=wechatmenu&code=071It0000PJ0eL1uyW100U3NHa1It00T&state="')
#options.add_argument('Accept-Encoding="gzip, deflate"')
#options.add_argument('Accept-Language="zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"')

# 更换头部
#options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat"')
#options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')
# 创建浏览器对象


#browser = WebDriver.Chrome(options=options)


conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")


cursor = conn.cursor()


#先根据不同月份年龄拿到题目，保存题目，然后再获取测评结果

getQuestionUrl = "https://yxyapi2.drcuiyutao.com/yxy-edu-gateway/api/json/quiz/quizQuestion"


age = 3#初始年龄
month=1#初始月份
end=0


for a in range(1,10):

  if end==1:#结束了  没有该年龄对应的测评
    break





  for m in range(1,80):

    #请求json
    data = {
      "monthRange": m,
      "ageRange": age,
      "appDevice": {
        "clientversion": "",
        "birthday": "",
        "accountId": "569954511711461376",
        "packageName": "",
        "ostype": 0,
        "imei": "",
        "appcode": "",
        "expectedDate": "",
        "build_serial": "",
        "osversion": "",
        "yxyskin": 0,
        "sign": "",
        "android_id": "",
        "userID": "13706174",
        "t": "",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTYxMzk2MDI2OTAxNX0.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiI1Njk5NTQ1MTE3MTE0NjEzNzYiLCJsb2dpblR5cGUiOiJ3ZWl4aW4iLCJsb2dnZXIiOiJvcmcuYXBhY2hlLmxvZ2dpbmcuc2xmNGouTG9nNGpMb2dnZXJAMTRjMThkYzUiLCJhcHBDb2RlIjoiWVVYWSIsImRldmljZW5vIjoibnVsbCIsImV4cCI6MTYxMzk2Mzg2OSwiaWF0IjoxNjEzOTYwMjY0LCJqdGkiOiIwIiwibWVtYmVySWQiOiIxMzcwNjE3NCJ9.moFyJAYp8qTXVLYxIIjokX0ATDcHrcnha5PH-cFXsZc",
        "hgestation": 0,
        "deviceno": "",
        "prematureOpen": 0,
        "channel": "",
        "loginType": 0,
        "reqrefer": "h5",
        "req_refer": "h5"
      },
      "childId": "569955350219087872",
      "memberId2": ""
    }

    #请求头
    headers = {
                "Host": "yxyapi2.drcuiyutao.com",
                "Connection": "keep-alive",
                "Content-Length": "1201",
                "Accept": "application/json, text/plain, */*",
    "Origin": "https://weixin.drcuiyutao.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://weixin.drcuiyutao.com/yxy-edu-web/testing?evaluationTypeCode=d2c3eaf4ea9e42ae98c78d3a154b8ec5&eScFrom=wechatmenu&nickName=%E5%9B%AD%E5%AE%9D_g6OenWmV0a&next=testing&chooseFlag=false&titleFlag=true&childId=569955350219087872&birthday=1611072000000&month=1&monthRange=2&ageRange=1&_channel=wx",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
    }



    try:


      # body = Json.JSONEncoder().encode(data)
      # postdata=urllib.parse.urlencode(data).encode('utf-8')

      # postdata=urllib.parse.urlencode(data).encode('utf-8')
      # postdata = "body=%7B%22quizRecordId%22%3A5000103%2C%22childId%22%3A%22569955350219087872%22%2C%22appDevice%22%3A%7B%22clientversion%22%3A%22%22%2C%22birthday%22%3A%22%22%2C%22accountId%22%3A%22569954511711461376%22%2C%22packageName%22%3A%22%22%2C%22ostype%22%3A0%2C%22imei%22%3A%22%22%2C%22appcode%22%3A%22%22%2C%22expectedDate%22%3A%22%22%2C%22build_serial%22%3A%22%22%2C%22osversion%22%3A%22%22%2C%22yxyskin%22%3A0%2C%22sign%22%3A%22%22%2C%22android_id%22%3A%22%22%2C%22userID%22%3A%2213706174%22%2C%22t%22%3A%22%22%2C%22token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTYxMzk2MDI2OTAxNX0.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiI1Njk5NTQ1MTE3MTE0NjEzNzYiLCJsb2dpblR5cGUiOiJ3ZWl4aW4iLCJsb2dnZXIiOiJvcmcuYXBhY2hlLmxvZ2dpbmcuc2xmNGouTG9nNGpMb2dnZXJAMTRjMThkYzUiLCJhcHBDb2RlIjoiWVVYWSIsImRldmljZW5vIjoibnVsbCIsImV4cCI6MTYxMzk2Mzg2OSwiaWF0IjoxNjEzOTYwMjY0LCJqdGkiOiIwIiwibWVtYmVySWQiOiIxMzcwNjE3NCJ9.moFyJAYp8qTXVLYxIIjokX0ATDcHrcnha5PH-cFXsZc%22%2C%22hgestation%22%3A0%2C%22deviceno%22%3A%22%22%2C%22prematureOpen%22%3A0%2C%22channel%22%3A%22%22%2C%22loginType%22%3A0%2C%22reqrefer%22%3A%22h5%22%2C%22req_refer%22%3A%22h5%22%7D%2C%22memberId2%22%3A%22%22%7D"

      # print(postdata)

      # req = urllib.request.Request(url=getQuestionUrl,headers=headers,data=postdata,method='Post')

      print("当前age："+str(age)+"--month："+str(m))


      postdata = "body=%7B%22monthRange%22%3A"+str(m)+"%2C%22ageRange%22%3A"+str(age)+"%2C%22appDevice%22%3A%7B%22clientversion%22%3A%22%22%2C%22birthday%22%3A%22%22%2C%22accountId%22%3A%22569954511711461376%22%2C%22packageName%22%3A%22%22%2C%22ostype%22%3A0%2C%22imei%22%3A%22%22%2C%22appcode%22%3A%22%22%2C%22expectedDate%22%3A%22%22%2C%22build_serial%22%3A%22%22%2C%22osversion%22%3A%22%22%2C%22yxyskin%22%3A0%2C%22sign%22%3A%22%22%2C%22android_id%22%3A%22%22%2C%22userID%22%3A%2213706174%22%2C%22t%22%3A%22%22%2C%22token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTYxMzk2MDI2OTAxNX0.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiI1Njk5NTQ1MTE3MTE0NjEzNzYiLCJsb2dpblR5cGUiOiJ3ZWl4aW4iLCJsb2dnZXIiOiJvcmcuYXBhY2hlLmxvZ2dpbmcuc2xmNGouTG9nNGpMb2dnZXJAMTRjMThkYzUiLCJhcHBDb2RlIjoiWVVYWSIsImRldmljZW5vIjoibnVsbCIsImV4cCI6MTYxMzk2Mzg2OSwiaWF0IjoxNjEzOTYwMjY0LCJqdGkiOiIwIiwibWVtYmVySWQiOiIxMzcwNjE3NCJ9.moFyJAYp8qTXVLYxIIjokX0ATDcHrcnha5PH-cFXsZc%22%2C%22hgestation%22%3A0%2C%22deviceno%22%3A%22%22%2C%22prematureOpen%22%3A0%2C%22channel%22%3A%22%22%2C%22loginType%22%3A0%2C%22reqrefer%22%3A%22h5%22%2C%22req_refer%22%3A%22h5%22%7D%2C%22childId%22%3A%22569955350219087872%22%2C%22memberId2%22%3A%22%22%7D"

      html = requests.post(url=getQuestionUrl,data=postdata,headers=headers)
      print(html.content)

      # theJson=urllib.request.urlopen(req)#拿到json



      # myJson=Json.loads(theJson.read())#解析json字符串
      myJson = Json.loads(html.content)
      print(myJson)



      if myJson['code']=='0':
        end=1
        print("获取数据出错了，原因："+myJson['msg'])
        break



      if len(myJson['data'])<=0:
        end=1
        print("age："+str(age)+"--month："+str(m)+"无数据了")
        break


      # for msg in myJson['data']:
      msg = myJson['data']
      quizQuestion = msg['quizQuestion']

      for qs in quizQuestion:
        title =  qs['abilityItemNmae']
        titleId = qs['abilityItem']
        list = qs['list']
        for it in list:
          pointDetail = it['abilityPointDetail']
          pointTitle = it['abilityPointTitle']
          content = it['content']
          imgUrl = it['imgUrl']
          remark = it['remark']
          sql = "INSERT INTO `ceping` (`month`,`age`,`title`, `titleId`, `abilityPointDetail`, `abilityPointTitle`,`content`,`imgUrl`,`remark`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          cursor.execute(sql, [m,age,title,titleId,pointDetail,pointTitle,content,imgUrl,remark])
          conn.commit()






    except Exception as ex:
      end=1
      print("age："+str(age)+"--month："+str(m)+"获取题目出错了，原因"+str(ex))

      break

  break



cursor.close()
conn.close()



















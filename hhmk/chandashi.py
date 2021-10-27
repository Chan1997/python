# -*- coding:utf-8 -*-
import pymysql
import json as Json
from urllib import parse
import time

import requests

class Chandashi():

    def __init__(self):
        a=0

    def getCookie(self):
        return {
            'cds_asm_token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyODM3NzYiLCJpYXQiOjE2MjYxNjYyMzUsImV4cCI6MTYyODc1ODIzNX0.01zx8TgSKe4PPEmomVqEwklag-HTpXCBWPPQba2Ptio',
        }

c = Chandashi()


header = {
    "Host": "www.chandashi.com",
    "Connection": "keep-alive",
    "sec-ch-ua" :"\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "Accept":"application/json, text/plain, */* ",
    "sec-ch-ua-mobile":"?0",
    "Origin": "https://mos.etmcn.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36t",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://www.chandashi.com/new/apps/downloadestimate?appId=523063187&country=cn",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
}

header2 = {
    "Host": "www.chandashi.com",
    "Connection": "keep-alive",
    "sec-ch-ua" :"\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "Accept":"application/json, text/plain, */* ",
    "sec-ch-ua-mobile":"?0",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36t",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://www.chandashi.com/new/search/index?keyword=%E5%AE%9D%E5%AE%9D%E6%A0%91&keywordRevise=1&iosVersion=14&country=cn&from=input&dataType=kw&date1=20210713&date2=20210712",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
}

# cookie = {
#     "cds_asm_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyODM3NzYiLCJpYXQiOjE2MjYxNjYyMzUsImV4cCI6MTYyODc1ODIzNX0.01zx8TgSKe4PPEmomVqEwklag-HTpXCBWPPQba2Ptio",
#     "cds_session_id":"kb7bnpmrkpv9dffc897rqa6q76"
# }

f=open('D:\getWechatData\chandashi.txt','r')#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'): #按照字符：进行划分读取
  name,value=line.strip().split('=',1)
  cookies[name]=value #为字典cookies添加内容



conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")


cursor = conn.cursor()

# 拼上appId
getDownloadUrl="https://www.chandashi.com/interf/v1/apps/downloadEstimate?country=cn&appId="

# 拼上keyword
getAppListUrl ="https://www.chandashi.com/interf/v1/search/index?revise=1&country=cn&iosVersion=14&from=input&date1=20210713&date2=20210712&dataType=kw&page=1&pageSize=50&client_id=10085&sign=A22BFC1092D2093B72ACD6787D8BE9C0327E09&keyword="


#parse.quote('宝宝树') 中午转码


appNames="宝宝树,妈妈网,宝宝知道,育学园,孕育提醒,孕育专家,辣妈帮,孕期伴侣,宝宝记-原柚宝宝,丁香妈妈,年糕妈妈,妈妈社区,布谷妈妈,米米孕育课堂,孕迹暖暖,好孕妈,小鲤鱼育儿指南,大肚皮助手,女性日记 Flo,Life Ofmom,comper女性-育龄女性健康助手,sprout,团团育儿,babytime,贝贝,国际妈咪-国妈母婴,蜜芽宝贝,孩子王,妈妈购,臻会挑,乐友,海拍客,行云货仓,挚爱母婴,一起牛,拿趣,花粉儿,转转,闲鱼,海带,中国母婴之家,海拍客,丁香医生,春雨医生,医鹿,用药助手,好孕妈妈,生生母婴,妈妈来了,小红书,棒棒糖,疯狂造人,排卵期计算器,棒米月经期助手-女性备孕怀孕指南管家,孕橙-备孕助手和排卵期计算器,好孕帮,排卵期计算器和最专业的孕期备孕助手,Ovulation Calculator Fertile Tracker&Calender,Glow Period,fertility ftacker,花生备孕,好孕说,柠檬胎动点点-胎动计数器和宫缩记录器,胎动记录-数胎动监测计数器,豌豆胎动,胎动监测管家,宫缩记录器,萌动,Pregnancy Test Checker,胎教音乐盒,胎教故事,胎教音乐合集,胎教音乐盒,噪音计,孕妇饮食禁忌,孕妇孕期食谱,孕期营养师,薄荷,美丽修行,真我,心心美妆,孕妇瑜伽,孕妇瑜伽-孕期及产后修复瘦身恢复,全是瑜,叨特,胎儿体重计算器,胎儿超声,280days,Femometer Intermittent Fasting,G 动-凯格尔运动锻炼软件,如初康复-专注产后女性盆底肌康复,凯格尔大师-性福提升神器,easy kegel,澜渟-盆底肌修复、凯格尔运动,7动-凯格尔成人性爱健康运动,科学坐月子,月子食谱,宝宝起名,富贵起名,周易起名大师,亲宝宝,绿豆熊宝宝,时光小屋,宝宝拍拍,时光记,宝宝相册,宝宝时光,宝宝树小时光,口袋宝宝,baby story,baby pics,baby camera,CHOMP,gif maker,拾柒,宝宝生活记录,宝宝生活记录和育儿日记-Piyo 日志,宝宝生活记录本,babyline-育儿日记,宝贝全记录,早安宝贝,宝宝护理能手,婴儿成长曲线表,成长记录,萌煮,宝宝辅食大全,婴儿食谱,半米宝宝食谱,儿童营养食谱,sleeptune,潮汐,Guva,sound sleeper,小睡眠,小豆苗,超级疫苗表,金苗宝,Kinedu：baby development plan,the wonder weeks,palyfully baby development app,凯叔讲故事,儿童睡前故事,宝宝巴士,阿布睡前故事,宝宝巴士故事,星宝乐园,喜马拉雅儿童,口袋故事,小伴龙,Baby Music,宝宝巴士儿歌,小花生,孩宝小镇,喜猫儿故事,咿啦看书,kada故事,洪恩故事,iHuman Books,伴鱼绘本,麦田亲子绘本,童话故事社,久趣英语绘本,绘本宝,英语绘本故事,三字经,FarFaria ,小雪老师优选,星宝绘本,绘本森林,Drawing （儿童画画游戏）,涂鸦涂色画画,Drawinggames,Toca band,秘密花园,Play & Learn Science,Breathe, Think, Do with Sesame,find my pair,触摸卡,宝宝拼图游戏,MarcoPolo－天气,MarcoPolo－海洋,宝宝行为认知,汽车卡车,十万个为什么语音版,儿歌多多,金宝贝启蒙,毛毛虫幼儿园,趣味食物,Khan kids,涂鸦,阿U学科学kids,麦田认字,儿童阅读训练营,哆哆儿歌,爱宝贝,Busyshapes,Playkids,Starfall,宝宝巴士世界,蒙特梭利幼儿园,小彼恩,火火兔,小步在家早教,爱宝贝早教全计划-儿童育儿恐龙拼音小游戏,宝宝识字卡,悟空识字,天天识字,宝宝巴士汉字,阳阳爱写字,宝宝早教社-婴儿早教之幼儿识字软件,Mother Goose Nursery Rhymes,斑马英语,小小优趣,starfall ABCs,英语启蒙动画,成长兔英语,少儿趣配音,PalFish Read,叽里呱啦,汐望学谷,都都数学,宝宝数学训练,洪恩数学,Todomath,Fiete Puzzle,Code Karts,Lightbot：Code Hour,Tynker JR,Kidlo Coding,编程王国：米亚夺宝,指令农场少儿编程,Daisy the Dinosaur,Scratch Jr"

appList = appNames.split(",")

index = 0
for appName in appList:

  print("当前app："+appName)

  try :



    # 先获得该appId
    encodeAppName = parse.quote(appName)


    # currentTime = str(time.time()-1000)
    #
    # timeIndex = currentTime.find('.')
    #
    # if timeIndex >=0:
    #     currentTime =  currentTime[0:timeIndex]1626230980

    resListHtml = requests.request('GET',url=getAppListUrl+encodeAppName+"&timestamp="+str(1626230980),headers=header2)




    print(resListHtml.content)

    listJson = Json.loads(resListHtml.content)

    #错误码
    code = listJson['code']

    if code !=0:
        if code == 3002:
            print("出错了，权限异常")
            raise Exception("出错了，错误响应码："+code+"，原因："+listJson['msg'])
        print("出错了，错误响应码："+code+"，原因："+listJson['msg'])
        raise Exception("出错了，错误响应码："+code+"，原因："+listJson['msg'])

    #返回数据
    listJsonData = listJson['data']

    if(listJsonData == None):
        print("返回数据为空，app名字："+appName)
        continue


    # resAppList = listJsonData['list']
    # if resAppList == None or len(resAppList) <1 :
    #     print("返回数据的list为空，app名字："+appName)
    #     continue

    keyworData = listJsonData['keywordData']

    if keyworData ==None :
        print("获取applist出错了，错误响应码："+str(code)+"，原因："+str(listJson['msg']))
        raise Exception("出错了，错误响应码："+str(code)+"，原因："+str(listJson['msg']))



    trackName = keyworData['keyword'] #找到的app名字
    trackId = keyworData['top_app'] #appId




    resAppHtml = requests.request('GET',url=getDownloadUrl+str(trackId),headers=header,cookies=cookies)

    print(resAppHtml.content)
    appJson = Json.loads(resAppHtml.content)

    appCode = appJson['code']


    if appCode != 0:
          print("获取app明细出错了，错误响应码："+str(appCode)+"，原因："+str(appJson['msg']))
          raise Exception("出错了，错误响应码："+str(appCode)+"，原因："+str(appJson['msg']))

     #返回数据
    appJsonData = appJson['data']

    yesterdayDownload = appJsonData['yesterday_download']

    thirtyDayDownload = appJsonData['thirty_download_total']

    downloadAvg = appJsonData['thirty_download']

    sql = "INSERT INTO `chandashi` (`app_id`,`app_name`,`find_app_name`,`download_avg`,`yesterday_download`,`thirty_day_download`) values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, [trackId,appName,trackName,downloadAvg,yesterdayDownload,thirtyDayDownload])
    conn.commit()








    time.sleep(0.3)
    index=index+1
    break


  except Exception as ex:
      print("出错了，app名字："+appName+" ,原因:"+str(ex))
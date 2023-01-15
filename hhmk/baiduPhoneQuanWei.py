import pymysql
import urllib.request
import lxml.html
from urllib import parse
from urllib.parse import urlencode
# from selenium import webdriver
import time
import requests
import json as Json
import pandas as pd
import math
from selenium.webdriver.chrome.options import Options
import random
# from selenium.webdriver.common.touch_actions import TouchActions
from appium import webdriver
from bs4 import BeautifulSoup
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction


class Baidu():
    def __init__(self):
        a=0

    def getUA(self):
        uaList = [
            #360
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            #chrome
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
            #"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",

            #firefox
            #"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
            #"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0",

            #ie11
            #"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            #ie8
            #"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; 4399Box.1357; 4399Box.1253; 4399Box.1357)",

            #2345王牌
            #"Chrome/39.0.2171.99 Safari/537.36 2345Explorer/6.5.0.11018",

            #搜狗
            #"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
            #opera
            #"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"

        ]
        headers = random.choice(uaList)
        return headers



baidu = Baidu()

conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")

cursor = conn.cursor()

header = {
    "Host": "m.baidu.com",
    "Connection": "close",
    "Cache-Control":"max-age=0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer":"https://www.chandashi.com/new/apps/downloadestimate?appId=523063187&country=cn",
    # "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie":"BDICON=10123156; BIDUPSID=AEB5A3EC19E87D5647D9AEB9A39606C2; PSTM=1603353785; BAIDUID=AEB5A3EC19E87D5627D933D4171AB19E:SL=0:NR=10:FG=1; BDUSS=jFDWkNqbEpMYUJ6Sk1Mcm9BdzRlSVNSV3pqQVRCaGt6eUNmQjdUTjRYTjJoTWRnRVFBQUFBJCQAAAAAAAAAAAEAAAArgj4mYXNkZmZnZ2dkc2Zzc2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHb3n2B2959gd; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=107319_110085_127969_128698_168389_170704_174434_176398_176553_176678_177061_177094_177167_177414_177480_177965_178140_178328_178494_178639_178804_179201_179350_179402_179459_179520_180123_180285_180324_180357_180364_180407_180415_180436_180512_180608_180654_180673_180699_180751_180758_180823_180868_180890_181191_181218_181250_181261_181295_181327_181428_181434_181444_181611_181649_181661_181669_181834; SE_LAUNCH=5%3A1626684865; delPer=0; rsv_i=7d7a67rIRYArIWUdO28cwShCfrKHxeO2JyTHEh5jmgeP6Fu3jFUyuU1UxCzcMXlivVT5b66mC%2BRCw2ggdSi1cYzbWzu7FOE; plus_lsv=54ca094a896f99d9; plus_cv=1::m:7.94e+147; BDICON=10123156; BDPASSGATE=IlPT2AEptyoA_yiU4V_H3kIN8ejRYrmAH4eGSzRh3FePdCyWmhHWAb-IXjLOUZm8AiTM-Y3fo_-zd5fCQjpfjKMThgMAfztqfFe6xqe25aTvL_NgzbIZCbDJOFkpzPXqav26z4wh1wRW4C9vfOHJpuo4ivKl73JQb4rc6VL2a_zXAlqR2WmJxlmEOolmO-0APNu594rXnEpZKS_1APHyRi8ybVciEHwL8b7pg2Aa24eDyyMAIeHuZMIpDG8vJpFeEQio1fWU60ul2-QvrpMnVjwt-kOqztC; BA_HECTOR=a52181a0a52l0l80081gfb1dq0q; BDSVRTM=70; PSINO=7"
}

baiduDomain = "http://m.baidu.com/ssid=047b4d72d8bcc9a7d8adcfc8c9ad8354/s"


keyword = parse.quote("宝宝该吃什么药")

reqData={
   "word":keyword,
    "sa":"tb",
    "ts":"3352449",
    "t_kt":"0",
    "ie":"utf-8",
    "rsv_t":"db01xx%2BrgqlyinsK7NxlT1crGC4nCQhX6oHkhKVZ7uSGzArlEr71",
    "rsv_pq":"8647003807584802332",
    "ss":"100",
    "sugid":"6351245963949692349",
    "rqlang":"zh",
    "rsv_sug4":"2338",
    "oq":keyword
}

f=open('D:\getWechatData\cookie_baidu.txt','r')#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'): #按照字符：进行划分读取
    name,value=line.strip().split('=',1)
    cookies[name]=value #为字典cookies添加内容

reqDataStr = urlencode(reqData)

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('lang=zh_CN.utf-8')
# MobileUserAgent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123f) NetType/WIFI Language/zh_CN'
# chrome_options.add_argument('User-Agent='+MobileUserAgent)


# browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# browser.execute_cdp_cmd('Network.setUserAgentOverride',{
#     "userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123f) NetType/WIFI Language/zh_CN"
#
# })
# browser.add_cookie({
#     "acw_tc":"0ed7ac9816139602472732069e7ebb1f301daf66ee41b372ec95c202d9",
#
# })

# browser.get("http://m.baidu.com")
# opener = urllib.request.build_opener()

# opener.addheaders.append(('Cookie', 'BDICON=10123156; BIDUPSID=AEB5A3EC19E87D5647D9AEB9A39606C2; PSTM=1603353785; BAIDUID=AEB5A3EC19E87D5627D933D4171AB19E:SL=0:NR=10:FG=1; BDUSS=jFDWkNqbEpMYUJ6Sk1Mcm9BdzRlSVNSV3pqQVRCaGt6eUNmQjdUTjRYTjJoTWRnRVFBQUFBJCQAAAAAAAAAAAEAAAArgj4mYXNkZmZnZ2dkc2Zzc2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHb3n2B2959gd; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=107319_110085_127969_128698_168389_170704_174434_176398_176553_176678_177061_177094_177167_177414_177480_177965_178140_178328_178494_178639_178804_179201_179350_179402_179459_179520_180123_180285_180324_180357_180364_180407_180415_180436_180512_180608_180654_180673_180699_180751_180758_180823_180868_180890_181191_181218_181250_181261_181295_181327_181428_181434_181444_181611_181649_181661_181669_181834; SE_LAUNCH=5%3A1626684865; delPer=0; rsv_i=7d7a67rIRYArIWUdO28cwShCfrKHxeO2JyTHEh5jmgeP6Fu3jFUyuU1UxCzcMXlivVT5b66mC%2BRCw2ggdSi1cYzbWzu7FOE; plus_lsv=54ca094a896f99d9; plus_cv=1::m:7.94e+147; BDICON=10123156; BDPASSGATE=IlPT2AEptyoA_yiU4V_H3kIN8ejRYrmAH4eGSzRh3FePdCyWmhHWAb-IXjLOUZm8AiTM-Y3fo_-zd5fCQjpfjKMThgMAfztqfFe6xqe25aTvL_NgzbIZCbDJOFkpzPXqav26z4wh1wRW4C9vfOHJpuo4ivKl73JQb4rc6VL2a_zXAlqR2WmJxlmEOolmO-0APNu594rXnEpZKS_1APHyRi8ybVciEHwL8b7pg2Aa24eDyyMAIeHuZMIpDG8vJpFeEQio1fWU60ul2-QvrpMnVjwt-kOqztC; BA_HECTOR=a52181a0a52l0l80081gfb1dq0q; BDSVRTM=70; PSINO=7'))
# webpage = opener.open(fullurl=baiduDomain+"?"+reqDataStr)
# req = urllib.request.Request(url=baiduDomain+"?"+reqDataStr,headers=header)
# inputBox=browser.find_element_by_id('index-kw')
# submitBox=browser.find_element_by_id('index-bn')

# workbook = xlrd.open_workbook('D:\Answer_2000_queries_1.xlsx')


data = pd.read_excel(io="D:\Baidukeyword\d39\D39.xlsx")
# data = pd.read_excel(io="D:\Baidukeyword\huishi2.xlsx")
#
# for ele in data.values:  # data.values二维数组形式
#     print(ele[0], ele[1], ele[2])


uaList = [
    #360
    # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    #chrome
    # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
    #"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
    # "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",

    #firefox
    #"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    #"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0",

    #ie11
    #"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    #ie8
    #"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; 4399Box.1357; 4399Box.1253; 4399Box.1357)",

    #2345王牌
    #"Chrome/39.0.2171.99 Safari/537.36 2345Explorer/6.5.0.11018",

    #搜狗
    #"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    #opera
    #"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"


    # "safariiOS4.33–iPhone：User-Agent:Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5"
    # ,"AndroidN1：User-Agent:Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1"
    # ,"safariiOS4.33–iPodTouch：User-Agent:Mozilla/5.0(iPod;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5"
    # ,"AndroidOperaMobile：User-Agent:Opera/9.80(Android2.3.4;Linux;OperaMobi/build-1107180945;U;en-GB)Presto/2.8.149Version/11.10"
    "Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3"
]

#自带浏览器
desired_caps ={
    "platformName":"Android",
    "deviceName":"ZTE_BV0800",
    "platformVersion":"7.0",
    "appPackage":"com.ume.browser",
    "appActivity":"com.ume.browser.MainActivity",
    "noReset":True,
    "newCommandTimeout":600,
    # "chromeOptions":{"androidProcess": "com.huawei.browser"},
    # "browser": "Chrome",
    # "setWebContentsDebuggingEnabled":True
    # "chromedriverExecutableDir":"D:\mychromedriver\chromedriver228.exe"
}

##qq浏览器
desired_caps1 ={
    "platformName":"Android",
    "deviceName":"ZTE_BV0800",
    "platformVersion":"7.0",
    "appPackage":"com.tencent.mtt",
    "appActivity":"com.tencent.mtt.SplashActivity",
    "noReset":True,
    "newCommandTimeout":600,
    # "chromeOptions":{"androidProcess": "com.huawei.browser"},
    # "browser": "Chrome",
    # "setWebContentsDebuggingEnabled":True
    # "chromedriverExecutableDir":"D:\mychromedriver\chromedriver228.exe"
}

keywordList1 = ['胎儿先水肿还是先胎停']
#
# print(keywordList1[0])


browser=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# word = parse.quote('小儿肺结核的早期症状特点')
# browser.get("http://m.baidu.com/s?from=1000539d&word="+word)
# browser.switch_to.context("WEBVIEW_com.android.browser")




#keywordStr = "高危产妇,高危产妇需做哪些检查,高龄高危产妇是多少岁,高危产妇注意事项,高危产妇能顺产吗,孕晚期糖尿病,糖尿病的原因,妊娠期糖尿病诊断标准,妊娠期糖尿病怎么办,糖尿病不能吃什么,糖尿病人能吃西瓜吗,糖尿病人食谱,糖尿病的饮食治疗,糖尿病饮食禁忌,糖尿病人吃什么主食,糖尿病能治好吗,治疗糖尿病的偏方,糖尿病治疗仪,糖尿病足的治疗,中医治疗糖尿病,糖尿病肾病,怎样预防糖尿病,糖尿病会传染吗,糖尿病酮症酸中毒,什么是糖尿病,孕妇糖尿病食谱,糖尿病的危害,糖尿病注意事项,糖尿病肾病分期,糖尿病手术,糖尿病视网膜病变,糖尿病眼病,糖尿病的症状,怀孕晚期,孕晚期肚疼,孕晚期补钙,孕晚期注意事项,孕晚期性生活,孕晚期见红,孕晚期宫缩,孕晚期吃什么好,孕晚期睡姿,孕晚期肚子硬,孕晚期腹痛,孕晚期营养,脐带绕颈一周怎么办,脐带绕颈怎么办,孕晚期食谱,孕晚期饮食,孕晚期喝什么奶粉好,孕晚期产检项目及最佳检查时间,孕晚期产检,如何缓解孕妇烧心,孕妇肥胖怎么办,孕晚期如厕,孕晚期饮食注意事项,孕妇心情不好,大肚子孕妇,怀孕36周,怀孕后期,怀孕后期注意事项"

#keywordList = keywordStr.split(",")

#keywordType = '玻尿酸隆鼻'


index = 1
for row in data.values:  # data.values二维数组形式
#
    if row[0] == '关键词':continue
    # index = int(row[2])
    # if index >10000 :
    #     break
    if index <= 24023:
        index = index +1
        continue

# for kw in keywordList1:

    kw = row[0]
    pcHeat = row[1]
    mobileHeat = row[2]
    keywordType = '外科内科' # row[2]'
    packageType ='关键词数据20230105' #  row[3]




    # if pcHeat==None or math.isnan(pcHeat) or pcHeat =='': pcHeat=0
    # if mobileHeat==None or math.isnan(mobileHeat) or mobileHeat =='': mobileHeat=0

    print("当前索引："+str(index)+";关键词："+str(kw)+";当前分类："+str(keywordType))


    for reqNum in range(0,4):

        try:

            word = parse.quote(kw)
            browser.get("http://m.baidu.com/s?from=1000539d&word="+word)
            print(browser.contexts)


            while browser.contexts==None or len(browser.contexts)==1:
                time.sleep(2)
                print(browser.contexts)


            browser.switch_to.context("WEBVIEW_com.ume.browser")


            time.sleep(0.5)
            pageSource = browser.page_source


            pageText = parse.unquote(pageSource,'utf-8')

            checkStr = '<title>'+kw+' - 百度</title>'
            if pageText.find(checkStr) <0:
                checkStr = checkStr.replace('，',',')
                checkStr = checkStr.replace('？','?')
                if kw.find('  ') >=0 or kw.find('   ') :
                    checkStr = checkStr.replace('   ',' ')
                    checkStr = checkStr.replace('  ',' ')
                if pageText.find(checkStr) <0:
                    print('反爬机制，未检测到当前词')
                    continue

            soup = BeautifulSoup(pageText,'lxml')

            # 获取results
            results = soup.find('div',class_="results")

            if results == None:
                time.sleep(0.5)
                results = soup.find('div',class_="results")
            if results == None:
                time.sleep(0.5)
                results = soup.find('div',class_="results")
            if results == None:
                time.sleep(0.5)
                results = soup.find('div',class_="results")


            # 拿到results里面的 c-result
            cResultList = results.select('.c-result')

            # if cResultList == [] and reqNum==3:
            #     print("cResultList为空")
            #     print("请求"+str(reqNum+1)+"次成功")
            #     sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`heat`,`is_top`,`is_combine`,`combine_num`,`is_expert`,`source`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            #     cursor.execute(sql, [index,kw,heat,0,0,0,0,'',keywordType,packageType])
            #     conn.commit()
            #     success = 1
            #     break

            success = 0


            topFlag=0
            expertTotal = 0
            yjkFlag = 0

            cResultIndex = 0
            for cResult in cResultList:
                articleText = str(cResult.text)

                iiii = articleText.find('\n\n')
                if iiii >0 :
                    articleText = articleText[:iiii]

                # if articleText == None or articleText.find(kw)<0 :
                #     continue

                try:
                    try:
                        article = cResult.article
                    except Exception as ex:
                        print("找不到article")
                        raise Exception("找不到搜索的article")




                    ################################# 开始判断TOP1 #####################################
                    try:
                        if cResultIndex == 0 and articleText!=None:
                            if articleText.find('搜索智能精选')==0:
                                print("是top1")
                                topFlag = 1
                            if topFlag ==0 : print('不含有top1')


                    except Exception as es:
                        print("检测top1异常"+str(es)+"，当做非top1")



                    ################################# 结束判断TOP1 #####################################


                    ################################# 开始寻找专家 #####################################
                    expertFlag=0
                    try:
                        if articleText!=None:
                            # 主任医师、副主任医师、主治医师、住院医师
                            if articleText.find('推荐权威三甲专家') < 0 and articleText.find('免费咨询') <0:
                                if articleText.find('主任医师')>-1 or articleText.find('副主任医师') >-1 or articleText.find('主治医师')>-1 or articleText.find('住院医师')>-1:
                                    expertFlag =1
                                    expertTotal = expertTotal +1
                                    print("含有专家信息，现总计："+str(expertTotal)+"个")

                        if expertFlag ==0:
                            print("不含专家信息")
                    except Exception as ex:
                        print("不含专家信息")
                    ################################# 结束寻找专家 #####################################


                    ################################# 开始寻找悦健康课堂 #####################################

                    if yjkFlag==0 and articleText.find('悦健康课堂') >= 0:
                        print('是悦健康课堂词条')
                        yjkFlag = 1

                    ################################# 开始寻找悦健康课堂 #####################################


                    # continue

                    # print("请求"+str(reqNum+1)+"次成功")
                    # sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`heat`,`is_top`,`is_combine`,`combine_num`,`is_expert`,`source`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    # cursor.execute(sql, [index,kw,heat,topFlag,None,None,expertFlag,None,keywordType,packageType])
                    # conn.commit()
                    # success = 1

                    if expertTotal > 8: break

                    cResultIndex = cResultIndex + 1
                    # break


                except Exception as ex:
                    if reqNum==3:
                        print("出错了,原因:"+str(ex))
                        sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`pc_heat`,`mobile_heat`,`is_top`,`is_expert`,`has_yjk`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql, [index,kw,pcHeat,mobileHeat,topFlag,expertTotal,yjkFlag,keywordType,packageType])
                        conn.commit()
                    cResultIndex = cResultIndex + 1
                    break





            if reqNum >=2:
                print("所有内容cResult无关键词")
                print("请求"+str(reqNum+1)+"次成功")
                sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`pc_heat`,`mobile_heat`,`is_top`,`is_expert`,`has_yjk`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,pcHeat,mobileHeat,topFlag,expertTotal,yjkFlag,keywordType,packageType])
                conn.commit()
                success = 1
                break
            else:
                print(kw+"完成")
                print("请求"+str(reqNum+1)+"次成功")
                sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`pc_heat`,`mobile_heat`,`is_top`,`is_expert`,`has_yjk`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,pcHeat,mobileHeat,topFlag,expertTotal,yjkFlag,keywordType,packageType])
                conn.commit()
                break

        except Exception as ex:
            print(ex)
            time.sleep(1)
            if reqNum==3:
                sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`pc_heat`,`mobile_heat`,`msg`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,pcHeat,mobileHeat,str("搜索出错了，反爬机制"),keywordType,packageType])
                conn.commit()
                print("请求三次最终都出错了,原因:"+str(ex))
                break
    index = index +1
a=1





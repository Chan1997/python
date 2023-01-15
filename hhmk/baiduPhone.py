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


data = pd.read_excel(io="D:\Baidukeyword\d36\D36.xlsx")
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

# keywordList1 = ['剖腹产利弊']
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

    if row[0] == '关键词':continue
    # index = int(row[2])
    # if index >10000 :
    #     break
    if index <= 4307:
        index = index +1
        continue

# for kw in keywordList1:

    kw = row[0]
    heat = row[1]
    keywordType =  row[2]
    packageType =  row[3]

    if heat==None or math.isnan(heat) or heat =='': heat=0

    print("当前索引："+str(index)+";关键词："+str(kw)+";当前分类："+keywordType)


    for reqNum in range(0,4):

        try:
            # kw = '过敏性鼻炎不能吃什么东西'
            # kw = '腹直肌分离的原因'
            # browser.switch_to.context("NATIVE_APP")

            # inputBox = browser.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView[2]')
            # print(browser.page_source)
            # inputBox = browser.find_element(By.ID,'com.ume.browser:id/home_search_input_text_id')
            # TouchAction(browser).tap(inputBox).perform()
            # time.sleep(1)
            # zoomSearchtBox = browser.find_element(By.ID,'com.ume.browser:id/url_bar')
            # zoomSearchtBox.send_keys(kw)
            # clickSearchBox = browser.find_element(By.ID,'com.ume.browser:id/url_go_btn')
            # clickSearchBox.click()


            # print(browser.contexts)
            # print(browser.page_source)
            # browser.switch_to.context("WEBVIEW_com.ume.browser")
            # browser.get("http://m.baidu.com")
            # browser.switch_to.context("WEBVIEW_com.ume.browser")
            #
            # print(browser.page_source)
            #
            # inputBox=browser.find_element(By.ID,'index-kw')
            # submitBox=browser.find_element(By.ID,'index-bn')
            # inputBox.send_keys(kw)
            # submitBox.click()




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
            for cResult in cResultList:
                articleText = str(cResult.text)

                if articleText == None or articleText.find(kw)<0 :
                    continue

                try:
                    try:
                        article = cResult.article
                    except Exception as ex:
                        print("找不到article")
                        raise Exception("找不到搜索的article")

                    topFlag=0
                    aiCombineFlag=0
                    expertFlag=0


                    ################################# 开始判断TOP1 #####################################
                    try:
                        # topList = browser.find_elements(by=By.XPATH,value='//div[contains(@class,"results")]/div[contains(@class,"c-result")][1]//div[contains(@class,"c-kg-header")]')
                        topList = cResultList[0].select('.c-kg-header')

                        # print('找到c-kg-header共'+str(len(topList)))
                        if topList == None or len(topList) <= 0 :
                            raise Exception('')
                        topFlag = 1
                        print('是top1')
                    except Exception as ex:
                        print('不是top1')

                    if topFlag  == 0 :
                        try:
                            isTop = cResultList[0].select('.c-gap-inner-top-lh')

                            if isTop != None:
                                topFlag=1
                                print("是top1")
                        except Exception as ex:
                            print("不是top1")

                    if topFlag ==0:
                        try:
                            topImg =  cResult.article.img
                            if topImg != None:
                                for img in topImg:
                                    bg = img.get('src')
                                    if str(bg).find('top1') >-1:
                                        topFlag=1
                                        print("是top1")
                                        break
                                    print("不是top1")
                                    break
                        except Exception as ex:
                            print("不是top1")
                    ################################# 结束判断TOP1 #####################################




                    ################################# 开始判断智能聚合 #####################################
                    try:
                        for kkkkk in cResultList:
                            combineClass = kkkkk.select('.c-clk-recommend')
                            if combineClass != None and len(combineClass) > 0 :
                                print("含有智能聚合")
                                aiCombineFlag=1
                                break

                        if aiCombineFlag ==0 :print('不含智能聚合')

                    except Exception as ex:
                        print("不含智能聚合")

                    if aiCombineFlag != 1 :
                        try:
                            for kkkkk in cResultList:
                                cText = str(kkkkk.text)
                                if cText!=None:
                                    if cText.find('搜索智能聚合')>-1:
                                        aiCombineFlag =1
                                        print("含有智能聚合")
                                        break
                            if aiCombineFlag != 1:
                                print("不含智能聚合")
                        except Exception as ex:
                            print("不含智能聚合")

                    ################################# 结束判断智能聚合 #####################################


                    ################################# 开始寻找专家 #####################################
                    try:
                        if articleText!=None:
                            if articleText.find('医生')>-1 or articleText.find('医师') >-1 or articleText.find('医院')>-1:
                                expertFlag =1
                                print("含有专家信息")
                        if expertFlag ==0:
                            print("不含专家信息")
                    except Exception as ex:
                        print("不含专家信息")

                    if expertFlag ==0:
                        try:
                            isExpertList = cResult.select('.c-source-new').select('.c-gap-right-middle')
                            expertIndex = 0
                            for expert in isExpertList:
                                if expertIndex >1:break
                                if str(expert.text).find('医')>-1:
                                    expertFlag =1
                                    print("含有专家信息")
                                    break
                                expertIndex= expertIndex+1
                            if expertFlag ==0:print("不含专家信息")
                        except Exception as ex:
                            print("不含专家信息")
                    ################################# 结束寻找专家 #####################################


                    ################################# 开始寻找来源 #####################################
                    source = ''
                    containSource = 0
                    containIndex = 0
                    findSourceList = []
                    # try:
                    #     findSourceList = cResult.find('div',class_='c-line-clamp1 _3cEBX')
                    #
                    #     if findSourceList !=None and len(findSourceList) >0:
                    #
                    #         for i in range(len(findSourceList)):
                    #             if(articleText.find(findSourceList[i].text)>-1):
                    #                 print("含有父来源:"+str(findSourceList[i].text))
                    #                 containSource = 1
                    #                 containIndex = i
                    #             else:
                    #                 break
                    #
                    # except Exception as ex:
                    #     print("不含有父来源")
                    #
                    #
                    # if containSource == 0 :
                    #     containIndex = 0
                    #     try:
                    #         findSourceList = cResult.find('div',class_='c-line-clamp1 _3d8C0')
                    #
                    #         if findSourceList !=None and len(findSourceList) >0:
                    #
                    #             for i in range(len(findSourceList)):
                    #                 if(articleText.find(findSourceList[i].text)>-1):
                    #                     print("含有父来源:"+str(findSourceList[i].text))
                    #                     containSource = 1
                    #                     containIndex = i
                    #         else:
                    #             containSource = 0
                    #
                    #     except Exception as ex:
                    #         print("不含有父来源")
                    # if containSource == 0 :
                    #     containIndex = 0
                    #     try:
                    #
                    #         findSourceList = cResult.find('span',class_='c-color-source')
                    #
                    #         print('c-color-source:'+str(len(findSourceList)))
                    #         if findSourceList !=None and len(findSourceList) >0:
                    #
                    #             for i in range(len(findSourceList)):
                    #                 if(articleText.find(findSourceList[i].text)>-1):
                    #                     print("含有父来源:"+str(findSourceList[i].text))
                    #                     containSource = 1
                    #                     containIndex = i
                    #                     break
                    #                 else:
                    #                     break
                    #         if containSource == 0 : print('不含有父来源')
                    #     except Exception as ex:
                    #         print("不含有父来源")
                    #
                    # if containSource ==0 : print("不含有父来源")
                    # else :
                    #     if str(findSourceList[containIndex].text) == '搜索智能聚合' or str(findSourceList[containIndex].text) == '':
                    #         print('不含有父来源')
                    #         containSource = 0
                    #     else:
                    #         source = str(findSourceList[containIndex].text)
                    #         print("父来源："+source)
                    #
                    #
                    # containSource1 = 0
                    # containIndex1 = 0
                    # findSourceList1 = []
                    #
                    # try:
                    #     try:
                    #         findSourceList1 = cResult.find('div',class_='_393GY')
                    #     except Exception as ex:
                    #         print('')
                    #
                    #     if findSourceList1 == None or len(findSourceList1) <=0 :
                    #         try:
                    #             findSourceList1 = cResult.find('div',class_='_3z4hy')
                    #         except Exception as ex:
                    #             print('')
                    #
                    #     if findSourceList1 !=None and len(findSourceList1) >0:
                    #
                    #         for i in range(len(findSourceList1)):
                    #             if(articleText.find(findSourceList1[i].text)>-1):
                    #                 print("含有子来源:"+str(findSourceList1[i].text))
                    #                 containSource1 = 1
                    #                 containIndex1 = i
                    #             else:
                    #                 break
                    # except Exception as ex:
                    #     print("不含子有来源")
                    #
                    # if containSource1 ==0 : print("不含子有来源")
                    # else :
                    #     if containSource == 1:
                    #         source = source +";"+ str(findSourceList1[containIndex1].text)
                    #     else:
                    #         source = str(findSourceList1[containIndex1].text)
                    #     print("子来源："+str(findSourceList1[containIndex1].text))
                    #
                    # if containSource ==1 or containSource1 ==1 :
                    #     print("含有父子来源，"+source)
                    # else:
                    #     print("不含有任何来源")

                    ################################# 结束寻找来源 #####################################


                    ################################# 开始寻找聚合个数 #####################################


                    combineNum = 0

                    if True:
                        trueHasCombine = 0
                        try:
                            reqCombineCount = 0

                            for reqCombineCount in range(1) :

                                # browser.get("http://m.baidu.com/s?from=1000539d&word="+word)

                                # answerList = browser.find_elements_by_xpath('//div[contains(@class,"results")]//span[contains(@class,"_hg8DT")]')
                                for kkkkk in cResultList:

                                    answerList = kkkkk.select('._1mmq3')

                                    if answerList !=None and len(answerList) >0:
                                        for i in range(len(answerList)):
                                            answerText = str(answerList[i].text)
                                            # print(answerText)
                                            expertAudioIndex = answerText.find('专家回答')
                                            if expertAudioIndex >-1:
                                                trueHasCombine = 1

                                                if len(answerText)-(expertAudioIndex+6) <= 0:
                                                    print('专家回答没显示数量，进行跳转获得大约数量')
                                                    combineNum = 10
                                                    break

                                                filterText = answerText[expertAudioIndex+6:len(answerText)]

                                                expertAudioIndex = filterText.find('条')

                                                expertAudioNum = int(filterText[0:expertAudioIndex])
                                                print("含有专家解答个数："+str(expertAudioNum))

                                                combineNum = expertAudioNum

                                                break
                                    if trueHasCombine == 1: break



                        except Exception as ex:
                            print("寻找专家聚合个数出错了，"+str(ex))
                        if trueHasCombine == 0:
                            print("不含智能聚合")
                            aiCombineFlag = 0

                    ################################# 结束寻找聚合个数 #####################################

                    print("请求"+str(reqNum+1)+"次成功")
                    sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`heat`,`is_top`,`is_combine`,`combine_num`,`is_expert`,`source`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, [index,kw,heat,topFlag,aiCombineFlag,combineNum,expertFlag,source,keywordType,packageType])
                    conn.commit()
                    success = 1
                    break



                except Exception as ex:
                    if reqNum==3:
                        print("出错了,原因:"+str(ex))
                        sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`heat`,`msg`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql, [index,kw,heat,str(ex),keywordType,packageType])
                        conn.commit()
                    break

            if success ==1:
                print(kw+"完成")
                break
            if success == 0 and reqNum ==2:
                print("所有内容cResult无关键词")
                print("请求"+str(reqNum+1)+"次成功")
                sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`heat`,`is_top`,`is_combine`,`combine_num`,`is_expert`,`source`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,heat,0,0,0,0,'',keywordType,packageType])
                conn.commit()
                success = 1
                break

        except Exception as ex:
            print(ex)
            time.sleep(1)
            if reqNum==3:
                sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`heat`,`msg`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,heat,str("搜索出错了，反爬机制"),keywordType,packageType])
                conn.commit()
                print("请求三次最终都出错了,原因:"+str(ex))
                break
    index = index +1
a=1
# webpage = urllib.request.urlopen(req)

# time.sleep(2)
#
# html = webpage.read()
#
# print(str(html))


# etree = lxml.html.etree

# element = etree.HTML(html)
#
#
# find = element.xpath('//div[contains(@class,"c-img-around-mask")]/img')
#
# for f in find:
#     print(f.get_attribute('src'))

# session = requests.session()
#
# resAppHtml = session.get(url=baiduDomain+"?"+reqDataStr, cookies=cookies)
# resAppHtml.encoding='utf-8'

# print(resAppHtml.content.decode('unicode-escape'))


# print(resAppHtml.content.decode('utf-8'))




import pymysql
import urllib.request
import lxml.html
from urllib import parse
from urllib.parse import urlencode
from selenium import webdriver
import time
import requests
import json as Json
import pandas as pd


class Baidu():
    def __init__(self):
        a=0



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


keyword = parse.quote("?????????????????????")

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

f=open('D:\getWechatData\cookie_baidu.txt','r')#??????????????????cookies????????????
cookies={}#?????????cookies????????????
for line in f.read().split(';'): #?????????????????????????????????
    name,value=line.strip().split('=',1)
    cookies[name]=value #?????????cookies????????????

reqDataStr = urlencode(reqData)

browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

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


data = pd.read_excel(io='D:\Answer_1018.xlsx')
#
# for ele in data.values:  # data.values??????????????????
#     print(ele[0], ele[1], ele[2])

 


#keywordStr = "????????????,??????????????????????????????,??????????????????????????????,????????????????????????,????????????????????????,??????????????????,??????????????????,??????????????????????????????,???????????????????????????,????????????????????????,???????????????????????????,??????????????????,????????????????????????,?????????????????????,???????????????????????????,?????????????????????,????????????????????????,??????????????????,?????????????????????,?????????????????????,???????????????,?????????????????????,?????????????????????,????????????????????????,??????????????????,?????????????????????,??????????????????,?????????????????????,?????????????????????,???????????????,????????????????????????,???????????????,??????????????????,????????????,???????????????,???????????????,?????????????????????,??????????????????,???????????????,???????????????,?????????????????????,???????????????,??????????????????,???????????????,???????????????,???????????????????????????,?????????????????????,???????????????,???????????????,???????????????????????????,??????????????????????????????????????????,???????????????,????????????????????????,?????????????????????,???????????????,???????????????????????????,??????????????????,???????????????,??????36???,????????????,????????????????????????"

#keywordList = keywordStr.split(",")

keywordList1 = ['?????????????????????????????????????????????']
index = 1
for row in data.values:  # data.values??????????????????

    # if index >10000 :
    #     break
    if index <= 42153:
        index = index +1
        continue


# for kw in keywordList1:

    kw = row[0]
    heat = row[1]
    #id = row[0]
    #time = row[2]
    print("???????????????"+str(index)+";????????????"+kw)


    for reqNum in range(0,3):

        try:

            browser.get("http://m.baidu.com")
            inputBox=browser.find_element_by_id('index-kw')
            submitBox=browser.find_element_by_id('index-bn')

            inputBox.send_keys(kw)
            submitBox.submit()


        #     ??????results
            results = browser.find_element_by_xpath('//div[contains(@class,"results")]')

            cResultList = results.find_elements_by_xpath('//div[contains(@class,"c-result")]')

            success = 0
            for cResult in cResultList:
                try:


                    try:
                        article = cResult.find_element_by_xpath('//article')
                    except Exception as ex:
                        print("?????????article")
                        raise Exception("??????????????????article")

                    topFlag=0
                    aiCombineFlag=0
                    expertFlag=0

                    ################################# ????????????TOP1 #####################################


                    try:
                        topList = browser.find_elements_by_xpath('//div[contains(@class,"results")]/div[contains(@class,"c-result")][1]//div[contains(@class,"c-kg-header")]')
                        print('??????c-kg-header???'+str(len(topList)))
                        if topList == None or len(topList) <= 0 :
                            raise Exception('')
                        topFlag = 1
                        print('???top1')
                    except Exception as ex:
                        print('??????top1')


                    if topFlag  == 0 :
                        try:
                            isTop = browser.find_element_by_xpath('//div[contains(@class,"results")]/div[contains(@class,"c-result")][1]//div[contains(@class,"c-gap-inner-top-lh")]')


                            if isTop != None:
                                topFlag=1
                                print("???top1")
                        except Exception as ex:
                            print("??????top1")


                    if topFlag ==0:
                        try:
                            topImg =  cResult.find_elements_by_xpath('//article//img')
                            if topImg != None:
                                for img in topImg:
                                    bg = img.get_attribute('src')
                                    if str(bg).find('top1') >-1:
                                        topFlag=1
                                        print("???top1")
                                        break
                                    print("??????top1")
                                    break
                        except Exception as ex:
                            print("??????top1")

                    ################################# ????????????TOP1 #####################################




                    ################################# ???????????????????????? #####################################
                    try:
                        isAudio = cResult.find_element_by_xpath('//div[contains(@class,"audio")]')
                        if isAudio != None:
                            aiCombineFlag=1
                            print("????????????")

                    except Exception as ex:
                        print("????????????")

                    try:
                        if aiCombineFlag !=1:
                            isText = cResult.find_element_by_xpath('//span[contains(@style,"background-position:0 19px;")]')

                            print("?????????")
                            aiCombineFlag=1
                    except Exception as ex:
                        print("????????????")

                    ################################# ???????????????????????? #####################################


                    # try:
                    #     isExpertList = cResult.find_elements_by_xpath('//div[contains(@class,"c-source-new")]//div[contains(@class,"c-gap-right-middle")]')
                    #     expertIndex = 0
                    #     for expert in isExpertList:
                    #         if expertIndex >1:break
                    #         if str(expert.text).find('???')>-1:
                    #             expertFlag =1
                    #             print("??????????????????")
                    #             break
                    #         expertIndex= expertIndex+1
                    #     if expertFlag ==0:print("??????????????????")
                    # except Exception as ex:
                    #     print("??????????????????")
                    #
                    articleText = str(cResult.text)
                    # print(articleText)

                    ################################# ?????????????????? #####################################
                    try:
                        if articleText!=None:
                            if articleText.find('??????')>-1 or articleText.find('??????') >-1 or articleText.find('??????')>-1:
                                expertFlag =1
                                print("??????????????????")
                        if expertFlag ==0:
                            print("??????????????????")
                    except Exception as ex:
                        print("??????????????????")

                    if expertFlag ==0:
                        try:
                            isExpertList = cResult.find_elements_by_xpath('//div[contains(@class,"c-source-new")]//div[contains(@class,"c-gap-right-middle")]')
                            expertIndex = 0
                            for expert in isExpertList:
                                if expertIndex >1:break
                                if str(expert.text).find('???')>-1:
                                    expertFlag =1
                                    print("??????????????????")
                                    break
                                expertIndex= expertIndex+1
                            if expertFlag ==0:print("??????????????????")
                        except Exception as ex:
                            print("??????????????????")

                    ################################# ?????????????????? #####################################


                    ################################# ?????????????????? #####################################
                    source = ''
                    containSource = 0
                    containIndex = 0
                    findSourceList = []
                    try:
                        findSourceList = cResult.find_elements_by_xpath('//div[contains(@class,"c-line-clamp1 _55E1G")]')

                        if findSourceList !=None and len(findSourceList) >0:

                            for i in range(len(findSourceList)):
                                if(articleText.find(findSourceList[i].text)>-1):
                                    print("???????????????:"+str(findSourceList[i].text))
                                    containSource = 1
                                    containIndex = i
                                else:
                                    break

                    except Exception as ex:
                        print("??????????????????")

                    if containSource == 0 :
                        try:

                            findSourceList = browser.find_elements_by_xpath('//div[contains(@class,"results")]/div[contains(@class,"c-result")][1]//span[contains(@class,"c-color-source")]')

                            print('c-color-source:'+str(len(findSourceList)))
                            if findSourceList !=None and len(findSourceList) >0:

                                for i in range(len(findSourceList)):
                                    if(articleText.find(findSourceList[i].text)>-1):
                                        print("???????????????:"+str(findSourceList[i].text))
                                        containSource = 1
                                        containIndex = i
                                        break
                                    else:
                                        break
                            if containSource == 0 : print('??????????????????')
                        except Exception as ex:
                            print("??????????????????")



                    if containSource ==0 : print("??????????????????")
                    else :
                        if str(findSourceList[containIndex].text) == '??????????????????' or str(findSourceList[containIndex].text) == '':
                            print('??????????????????')
                            containSource = 0
                        else:
                            source = str(findSourceList[containIndex].text)
                            print("????????????"+source)


                    containSource1 = 0
                    containIndex1 = 0
                    findSourceList1 = []

                    try:

                        try:

                            findSourceList1 = cResult.find_elements_by_xpath('//div[contains(@class,"_393GY")]')
                        except Exception as ex:
                            print('')

                        if findSourceList1 == None or len(findSourceList1) <=0 :
                            try:
                                findSourceList1 = cResult.find_elements_by_xpath('//div[contains(@class,"_3z4hy")]')
                            except Exception as ex:
                                print('')

                        if findSourceList1 !=None and len(findSourceList1) >0:

                            for i in range(len(findSourceList1)):
                                if(articleText.find(findSourceList1[i].text)>-1):
                                    print("???????????????:"+str(findSourceList1[i].text))
                                    containSource1 = 1
                                    containIndex1 = i
                                else:
                                    break

                    except Exception as ex:
                        print("??????????????????")

                    if containSource1 ==0 : print("??????????????????")
                    else :


                        if containSource == 1:
                            source = source +";"+ str(findSourceList1[containIndex1].text)
                        else:
                            source = str(findSourceList1[containIndex1].text)
                        print("????????????"+str(findSourceList1[containIndex1].text))

                    if containSource ==1 or containSource1 ==1 :
                        print("?????????????????????"+source)
                    else:
                        print("?????????????????????")

                    ################################# ?????????????????? #####################################




                    print("??????"+str(reqNum+1)+"?????????")

                    sql = "INSERT INTO `baidu_keyword3` (`query_id`,`query`,`heat`,`is_top`,`is_combine`,`is_expert`,`source`) values (%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, [index,kw,heat,topFlag,aiCombineFlag,expertFlag,source])
                    conn.commit()
                    success = 1



                    break
                except Exception as ex:
                    if reqNum==2:
                        print("?????????,??????:"+str(ex))
                        sql = "INSERT INTO `baidu_keyword3` (`query_id`,`query`,`heat`,`msg`) values (%s,%s,%s,%s)"
                        cursor.execute(sql, [index,kw,heat,str(ex)])
                        conn.commit()
                    break
            if success ==1:
                break
            print(kw+"??????")
        except Exception as ex:

            if reqNum==2:
                sql = "INSERT INTO `baidu_keyword3` (`query_id`,`query`,`heat`,`msg`) values (%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,heat,str("??????????????????????????????")])
                conn.commit()
                print("??????????????????????????????,??????:"+str(ex))
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




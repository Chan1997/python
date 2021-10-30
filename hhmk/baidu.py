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
# for ele in data.values:  # data.values二维数组形式
#     print(ele[0], ele[1], ele[2])




#keywordStr = "高危产妇,高危产妇需做哪些检查,高龄高危产妇是多少岁,高危产妇注意事项,高危产妇能顺产吗,孕晚期糖尿病,糖尿病的原因,妊娠期糖尿病诊断标准,妊娠期糖尿病怎么办,糖尿病不能吃什么,糖尿病人能吃西瓜吗,糖尿病人食谱,糖尿病的饮食治疗,糖尿病饮食禁忌,糖尿病人吃什么主食,糖尿病能治好吗,治疗糖尿病的偏方,糖尿病治疗仪,糖尿病足的治疗,中医治疗糖尿病,糖尿病肾病,怎样预防糖尿病,糖尿病会传染吗,糖尿病酮症酸中毒,什么是糖尿病,孕妇糖尿病食谱,糖尿病的危害,糖尿病注意事项,糖尿病肾病分期,糖尿病手术,糖尿病视网膜病变,糖尿病眼病,糖尿病的症状,怀孕晚期,孕晚期肚疼,孕晚期补钙,孕晚期注意事项,孕晚期性生活,孕晚期见红,孕晚期宫缩,孕晚期吃什么好,孕晚期睡姿,孕晚期肚子硬,孕晚期腹痛,孕晚期营养,脐带绕颈一周怎么办,脐带绕颈怎么办,孕晚期食谱,孕晚期饮食,孕晚期喝什么奶粉好,孕晚期产检项目及最佳检查时间,孕晚期产检,如何缓解孕妇烧心,孕妇肥胖怎么办,孕晚期如厕,孕晚期饮食注意事项,孕妇心情不好,大肚子孕妇,怀孕36周,怀孕后期,怀孕后期注意事项"

#keywordList = keywordStr.split(",")

keywordList1 = ['宝宝不喝奶粉可以把奶粉放粥里吗']
# index = 1
for row in data.values:  # data.values二维数组形式

    index = int(row[2])
    # if index >10000 :
    #     break
    if index <= 102020:
        # index = index +1
        continue


# for kw in keywordList1:

    kw = row[0]
    heat = row[1]
    #id = row[0]
    #time = row[2]
    print("当前索引："+str(index)+";关键词："+str(kw))


    for reqNum in range(0,3):

        try:

            browser.get("http://m.baidu.com")
            inputBox=browser.find_element_by_id('index-kw')
            submitBox=browser.find_element_by_id('index-bn')

            inputBox.send_keys(kw)
            submitBox.submit()


        #     找到results
            results = browser.find_element_by_xpath('//div[contains(@class,"results")]')

            cResultList = results.find_elements_by_xpath('//div[contains(@class,"c-result")]')

            success = 0
            for cResult in cResultList:
                try:


                    try:
                        article = cResult.find_element_by_xpath('//article')
                    except Exception as ex:
                        print("找不到article")
                        raise Exception("找不到搜索的article")

                    topFlag=0
                    aiCombineFlag=0
                    expertFlag=0

                    ################################# 开始判断TOP1 #####################################


                    try:
                        topList = browser.find_elements_by_xpath('//div[contains(@class,"results")]/div[contains(@class,"c-result")][1]//div[contains(@class,"c-kg-header")]')
                        print('找到c-kg-header共'+str(len(topList)))
                        if topList == None or len(topList) <= 0 :
                            raise Exception('')
                        topFlag = 1
                        print('是top1')
                    except Exception as ex:
                        print('不是top1')


                    if topFlag  == 0 :
                        try:
                            isTop = browser.find_element_by_xpath('//div[contains(@class,"results")]/div[contains(@class,"c-result")][1]//div[contains(@class,"c-gap-inner-top-lh")]')


                            if isTop != None:
                                topFlag=1
                                print("是top1")
                        except Exception as ex:
                            print("不是top1")


                    if topFlag ==0:
                        try:
                            topImg =  cResult.find_elements_by_xpath('//article//img')
                            if topImg != None:
                                for img in topImg:
                                    bg = img.get_attribute('src')
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
                        isAudio = cResult.find_element_by_xpath('//div[contains(@class,"audio")]')
                        if isAudio != None:
                            aiCombineFlag=1
                            print("含有语音")

                    except Exception as ex:
                        print("不含语音")

                    try:
                        if aiCombineFlag !=1:
                            isText = cResult.find_element_by_xpath('//span[contains(@style,"background-position:0 19px;")]')

                            print("含文章")
                            aiCombineFlag=1
                    except Exception as ex:
                        print("不含文章")

                    ################################# 结束判断智能聚合 #####################################


                    # try:
                    #     isExpertList = cResult.find_elements_by_xpath('//div[contains(@class,"c-source-new")]//div[contains(@class,"c-gap-right-middle")]')
                    #     expertIndex = 0
                    #     for expert in isExpertList:
                    #         if expertIndex >1:break
                    #         if str(expert.text).find('医')>-1:
                    #             expertFlag =1
                    #             print("含有专家信息")
                    #             break
                    #         expertIndex= expertIndex+1
                    #     if expertFlag ==0:print("不含专家信息")
                    # except Exception as ex:
                    #     print("不含专家信息")
                    #
                    articleText = str(cResult.text)
                    # print(articleText)

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
                            isExpertList = cResult.find_elements_by_xpath('//div[contains(@class,"c-source-new")]//div[contains(@class,"c-gap-right-middle")]')
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
                    try:
                        findSourceList = cResult.find_elements_by_xpath('//div[contains(@class,"c-line-clamp1 _55E1G")]')

                        if findSourceList !=None and len(findSourceList) >0:

                            for i in range(len(findSourceList)):
                                if(articleText.find(findSourceList[i].text)>-1):
                                    print("含有父来源:"+str(findSourceList[i].text))
                                    containSource = 1
                                    containIndex = i
                                else:
                                    break

                    except Exception as ex:
                        print("不含有父来源")

                    if containSource == 0 :
                        try:

                            findSourceList = browser.find_elements_by_xpath('//div[contains(@class,"results")]/div[contains(@class,"c-result")][1]//span[contains(@class,"c-color-source")]')

                            print('c-color-source:'+str(len(findSourceList)))
                            if findSourceList !=None and len(findSourceList) >0:

                                for i in range(len(findSourceList)):
                                    if(articleText.find(findSourceList[i].text)>-1):
                                        print("含有父来源:"+str(findSourceList[i].text))
                                        containSource = 1
                                        containIndex = i
                                        break
                                    else:
                                        break
                            if containSource == 0 : print('不含有父来源')
                        except Exception as ex:
                            print("不含有父来源")



                    if containSource ==0 : print("不含有父来源")
                    else :
                        if str(findSourceList[containIndex].text) == '搜索智能聚合' or str(findSourceList[containIndex].text) == '':
                            print('不含有父来源')
                            containSource = 0
                        else:
                            source = str(findSourceList[containIndex].text)
                            print("父来源："+source)


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
                                    print("含有子来源:"+str(findSourceList1[i].text))
                                    containSource1 = 1
                                    containIndex1 = i
                                else:
                                    break

                    except Exception as ex:
                        print("不含子有来源")

                    if containSource1 ==0 : print("不含子有来源")
                    else :


                        if containSource == 1:
                            source = source +";"+ str(findSourceList1[containIndex1].text)
                        else:
                            source = str(findSourceList1[containIndex1].text)
                        print("子来源："+str(findSourceList1[containIndex1].text))

                    if containSource ==1 or containSource1 ==1 :
                        print("含有父子来源，"+source)
                    else:
                        print("不含有任何来源")

                    ################################# 结束寻找来源 #####################################




                    print("请求"+str(reqNum+1)+"次成功")

                    sql = "INSERT INTO `baidu_keyword3` (`query_id`,`query`,`heat`,`is_top`,`is_combine`,`is_expert`,`source`) values (%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, [index,kw,heat,topFlag,aiCombineFlag,expertFlag,source])
                    conn.commit()
                    success = 1



                    break
                except Exception as ex:
                    if reqNum==2:
                        print("出错了,原因:"+str(ex))
                        sql = "INSERT INTO `baidu_keyword3` (`query_id`,`query`,`heat`,`msg`) values (%s,%s,%s,%s)"
                        cursor.execute(sql, [index,kw,heat,str(ex)])
                        conn.commit()
                    break
            if success ==1:
                break
            print(kw+"完成")
        except Exception as ex:

            if reqNum==2:
                sql = "INSERT INTO `baidu_keyword3` (`query_id`,`query`,`heat`,`msg`) values (%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,heat,str("搜索出错了，反爬机制")])
                conn.commit()
                print("请求三次最终都出错了,原因:"+str(ex))
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




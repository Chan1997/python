import pymysql
import urllib.request
import lxml.html
from urllib import parse
from urllib.parse import urlencode
import time
import requests
import json as Json
import pandas as pd
import math
from selenium.webdriver.chrome.options import Options
import random
from appium import webdriver
from bs4 import BeautifulSoup
import difflib
import datetime


def calculate_similarity(word1, word2):
    sequence = difflib.SequenceMatcher(None, word1, word2)
    return sequence.ratio()



# mysql
conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")
cursor = conn.cursor()

# excel input
data = pd.read_excel(io="D:\Baidukeyword\d38\D38_1.xlsx")

# phone remote
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
browser=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

keywordList1 = ['早产儿感染的原因']

index = 1
packageName = 'test'
source = '悦健康课堂'
for row in data.values:  # data.values二维数组形式
# for kw in keywordList1:

    # if row[0] == '关键词':continue

    # if index <= 5:
    #     index = index +1
    #     continue

    kw = row[0]
    packageName = row[1]

    print("当前索引："+str(index)+";关键词："+str(kw))

    if kw==None or kw == '':break

    for reqNum in range(0,4):
        try:

            rank = None

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

            cResultList = results.select('.c-result')

            success = 0

            curRankIndex = 0
            for cResult in cResultList:
                if curRankIndex > 10 : break

                articleText = str(cResult.text)

                iiii = articleText.find('\n\n')

                if iiii >0 :
                    articleText = articleText[:iiii]

                # sim = calculate_similarity(kw, articleText)
                # print('相似度：'+str(calculate_similarity(kw, articleText)))

                if articleText.find(source) >= 0:
                    print('是'+source+'词条，排位：'+str(curRankIndex))
                    rank = curRankIndex
                    break
                else:
                    print("非"+source+"词条")

                curRankIndex = curRankIndex + 1

            logMsg = ''
            if rank!=None : logMsg = logMsg +str(rank)
            else: logMsg = logMsg + '未获得'

            print("请求"+str(reqNum+1)+"次成功，排位："+ logMsg)
            # sql = "INSERT INTO `baidu_keyword_rank` (`query_id`,`query`,`package_name`,`rank`,`source`) values (%s,%s,%s,%s,%s)"
            # cursor.execute(sql, [index,kw,packageName,rank,source])

            current_time = datetime.datetime.now()
            updateSql = " update `baidu_keyword_rank` set `new_rank` = %s,`update_time` = %s where `query_id` = %s and `package_name` = %s  "
            cursor.execute(updateSql, [rank,current_time,index,packageName])
            conn.commit()
            success = 1
            break



        except Exception as ex:
            print(ex)
            time.sleep(1)
            if reqNum==3:
                sql = "INSERT INTO `baidu_keyword_rank` (`query_id`,`query`,`msg`,`package_name`) values (%s,%s,%s,%s)"
                cursor.execute(sql, [index,kw,str("搜索出错了，反爬机制"),packageName])

                # current_time = datetime.datetime.now()
                # updateSql = " update `baidu_keyword_rank` set msg = %s,update_time = %s where query_id = %s and package_name = %s  "
                # cursor.execute(updateSql, [str('搜索出错了，反爬机制'),current_time,index,packageName])
                conn.commit()
                print("请求三次最终都出错了,原因:"+str(ex))
                break

    index = index +1

a=1
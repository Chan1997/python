import pymysql
from urllib import parse
from urllib.parse import urlencode
from selenium import webdriver



class BaiduHeat():
    def __init__(self):
        a=0
    def getSearchWord(self,str):
        return str+"?words="+str

baiduHeat = BaiduHeat()

conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")

cursor = conn.cursor()

browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get("https://index.baidu.com/v2/index.html")

f=open('D:\getWechatData\searchBaidu.txt','r')#打开所保存的cookies内容文件

for line in f.read().split(';'): #按照字符：进行划分读取
    name,value=line.strip().split('=',1)
    cookie_dict = {
        "domain": ".baidu.com",  # 火狐浏览器不用填写，谷歌要需要
        'name': name,
        'value': value,
        "expires": "",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False}
    browser.add_cookie(cookie_dict)


baiduDomain= "https://index.baidu.com/v2/main/index.html#/trend/"


querySql = "select * from `baidu_keyword`"
cursor.execute(querySql)

list = cursor.fetchall()

for row in list:
    queryId = row[0]
    keyword = row[1]

    try:

        searchUrl = baiduDomain+baiduHeat.getSearchWord(keyword)

        browser.get(searchUrl)

        a=1

    except Exception as ex:
        print("queryId："+str(queryId)+",keyword："+str(keyword)+"，出错了，原因："+str(ex))






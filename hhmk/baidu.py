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
import math
from selenium.webdriver.chrome.options import Options
import random
# from selenium.webdriver.common.touch_actions import TouchActions
# from appium import webdriver


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


data = pd.read_excel(io="D:\Baidukeyword\d32\D32.xlsx")
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



##old config
mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# chrome_options.add_experimental_option("w3c",False)

browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options=chrome_options)
#
browser.delete_all_cookies()


# desired_caps ={
# 'platformName':'Android',
# 'deviceName':'127.0.0.1:62001',
# 'platformVersion':'7.1.2',
# 'appPackage':'com.android.browser',
# 'appActivity':'com.android.browser.BrowserActivity',
# 'noReset':True
# }
# browser=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)





#keywordStr = "高危产妇,高危产妇需做哪些检查,高龄高危产妇是多少岁,高危产妇注意事项,高危产妇能顺产吗,孕晚期糖尿病,糖尿病的原因,妊娠期糖尿病诊断标准,妊娠期糖尿病怎么办,糖尿病不能吃什么,糖尿病人能吃西瓜吗,糖尿病人食谱,糖尿病的饮食治疗,糖尿病饮食禁忌,糖尿病人吃什么主食,糖尿病能治好吗,治疗糖尿病的偏方,糖尿病治疗仪,糖尿病足的治疗,中医治疗糖尿病,糖尿病肾病,怎样预防糖尿病,糖尿病会传染吗,糖尿病酮症酸中毒,什么是糖尿病,孕妇糖尿病食谱,糖尿病的危害,糖尿病注意事项,糖尿病肾病分期,糖尿病手术,糖尿病视网膜病变,糖尿病眼病,糖尿病的症状,怀孕晚期,孕晚期肚疼,孕晚期补钙,孕晚期注意事项,孕晚期性生活,孕晚期见红,孕晚期宫缩,孕晚期吃什么好,孕晚期睡姿,孕晚期肚子硬,孕晚期腹痛,孕晚期营养,脐带绕颈一周怎么办,脐带绕颈怎么办,孕晚期食谱,孕晚期饮食,孕晚期喝什么奶粉好,孕晚期产检项目及最佳检查时间,孕晚期产检,如何缓解孕妇烧心,孕妇肥胖怎么办,孕晚期如厕,孕晚期饮食注意事项,孕妇心情不好,大肚子孕妇,怀孕36周,怀孕后期,怀孕后期注意事项"

#keywordList = keywordStr.split(",")

#keywordType = '玻尿酸隆鼻'

keywordList1 = ['剖腹产利弊']
index = 1
for row in data.values:  # data.values二维数组形式

    if row[0] == '关键词':continue
    # index = int(row[2])
    # if index >10000 :
    #     break
    # if index <= 4643:
    #     index = index +1
    #     continue

# for kw in keywordList1:

    kw = row[0]
    heat = row[1]
    keywordType =  row[2]
    packageType =  row[3]

    if heat==None or math.isnan(heat) or heat =='': heat=0

    # print(heat)
    # heat = 1
    # keywordType = 'fdsad'
    # packageType = 'das'


    # try:
    #     heat = int(heat)
    # except Exception as ex:
    #     heat = 0


    #id = row[0]
    #time = row[2]
    print("当前索引："+str(index)+";关键词："+str(kw)+";当前分类："+keywordType)


    for reqNum in range(0,3):

        try:
            # user_agent = random.choice(uaList)

            # options = webdriver.ChromeOptions()
            # options.add_argument(f'user-agent={user_agent}')
            # options.add_argument('--ignore-ssl-errors=true')
            # options.add_argument('--load-images=no')
            #options.add_argument('--headless') #无浏览器模式
            # options.add_argument('--ignore-ssl-errors=true')
            # options.add_argument('--ssl-protocol=TLSv1')
            # options.add_argument('--proxy-type=http')

            # mobileEmulation = {"deviceMetrics":{"width":320,"height":640,"pixelRation":3.0},"userAgent":"Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3"}
            # options.add_experimental_option("mobileEmulation",mobileEmulation)

            # url1 = "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=115173&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
            # res=requests.get(url1).json()
            # ip=res['data'][0]['ip']
            # port=res['data'][0]['port']
            # proxies=ip+':'+str(port)
            # options.add_argument('--proxy-server=%s' % proxies)



            # browser.execute_cdp_cmd('Network.setUserAgentOverride',{
            #     "userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123f) NetType/WIFI Language/zh_CN"
            #
            # })

            # kw = '过敏性鼻炎不能吃什么东西'

            word = parse.quote(kw)
            browser.get("http://m.baidu.com/s?from=1000539d&word="+word)


            # reqUrl = 'https://mbd.baidu.com/ug_share/mbox/4a83aa9e65/share?product=search&tk=c86615a69edb69c4f83bb6da25c72b3f&share_url='

            # shareUrl = 'https://m.baidu.com/s?pu=sz@1320_480,cuid@01CFBC7DBE3DF95F8EB83B78F24205D6080BD46F3OSPTAARCGF,cua@1242_2688_iphone_12.6.0.11_0,cut@iPhone13,4_15.4,osname@baiduboxapp,ctv@1,cfrom@1099a,csrc@bdbox_tserch_txt,cud@MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAw&bd_page_type=1&word='+word+'&sa=tkb&network=1_0&t_samp=preload_4_1004&from=1099a&sugid=171923917851573&ant_ct=OiCO/+ZZeNw9Xmp96DYNYmYrD4xKqBGSn+JrRjfnRsQNoCRpcxdk6ybcJsvjS1m2&rsv_sug4=1854&rsv_pq=7268778685873060556&isid=ea55b8ca1f075bb5a55253434ec5b646&oq='+word+'&shared_from_app=1'

            # reqUrl = reqUrl + parse.quote(shareUrl) +'&domain=mbd.baidu.com'

            # browser.get(reqUrl)



            # browser.get("https://mbd.baidu.com/ug_share/mbox/4a83aa9e65/share?product=search&tk=c86615a69edb69c4f83bb6da25c72b3f&share_url=https%3A%2F%2Fm.baidu.com%2Fs%3Fpu%3Dsz%25401320_480%252Ccuid%254001CFBC7DBE3DF95F8EB83B78F24205D6080BD46F3OSPTAARCGF%252Ccua%25401242_2688_iphone_12.6.0.11_0%252Ccut%2540iPhone13%252C4_15.4%252Cosname%2540baiduboxapp%252Cctv%25401%252Ccfrom%25401099a%252Ccsrc%2540bdbox_tserch_txt%252Ccud%2540MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAw%26bd_page_type%3D1%26word%3D%25E9%2598%25B4%25E9%2581%2593%25E5%25B9%25B2%25E6%25B6%25A9%25E5%25A6%2582%25E4%25BD%2595%25E8%25A7%25A3%25E5%2586%25B3%26sa%3Dtkb%26network%3D1_0%26t_samp%3Dpreload_4_1004%26from%3D1099a%26sugid%3D171923917851573%26ant_ct%3DOiCO%252F%252BZZeNw9Xmp96DYNYmYrD4xKqBGSn%252BJrRjfnRsQNoCRpcxdk6ybcJsvjS1m2%26rsv_sug4%3D1854%26rsv_pq%3D7268778685873060556%26isid%3Dea55b8ca1f075bb5a55253434ec5b646%26oq%3D%25E9%2598%25B4%25E9%2581%2593%25E5%25B9%25B2%25E6%25B6%25A9%25E5%2590%2583%25E4%25BB%2580%25E4%25B9%2588%25E8%258D%25AF%26shared_from_app%3D1&domain=mbd.baidu.com")


            # browser.get("https://m.baidu.com/from=1000539d/s?word="+word+"&sa=tb&ts=0&t_kt=0&ie=utf-8&rsv_t=b098MPmgkcnLSiJUKZUArIhphCwIxT8yhA1wastcddQqn%252F%252B2hT5WhF0kU843lCE&rsv_pq=10579816538452659600&ss=")

            # browser.get("https://m.baidu.com/s?pu=sz@1320_480,cuid@01CFBC7DBE3DF95F8EB83B78F24205D6080BD46F3OSPTAARCGF,cua@1242_2688_iphone_12.6.0.11_0,cut@iPhone13,4_15.4,osname@baiduboxapp,ctv@1,cfrom@1099a,csrc@bdbox_tserch_txt,cud@MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAw&bd_page_type=1&word="+word+"&sa=tkb&network=1_0&t_samp=preload_4_1004&from=1099a&oq="+word+"&shared_from_app=1")

            # reqUrl = 'https://mbd.baidu.com/ug_share/mbox/4a83aa9e65/share?product=search&tk=c86615a69edb69c4f83bb6da25c72b3f&share_url=https%3A%2F%2Fm.baidu.com%2Fs%3Fpu%3Dsz%25401320_480%252Ccuid%254001CFBC7DBE3DF95F8EB83B78F24205D6080BD46F3OSPTAARCGF%252Ccua%25401242_2688_iphone_12.6.0.11_0%252Ccut%2540iPhone13%252C4_15.4%252Cosname%2540baiduboxapp%252Cctv%25401%252Ccfrom%25401099a%252Ccsrc%2540bdbox_tserch_txt%252Ccud%2540MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAw%26bd_page_type%3D1%26word%3D%25E9%2598%25B4%25E9%2581%2593%25E5%25B9%25B2%25E6%25B6%25A9%25E5%25A6%2582%25E4%25BD%2595%25E8%25A7%25A3%25E5%2586%25B3%26sa%3Dtkb%26network%3D1_0%26t_samp%3Dpreload_4_1004%26from%3D1099a%26sugid%3D171923917851573%26ant_ct%3DOiCO%252F%252BZZeNw9Xmp96DYNYmYrD4xKqBGSn%252BJrRjfnRsQNoCRpcxdk6ybcJsvjS1m2%26rsv_sug4%3D1854%26rsv_pq%3D7268778685873060556%26isid%3Dea55b8ca1f075bb5a55253434ec5b646%26oq%3D%25E9%2598%25B4%25E9%2581%2593%25E5%25B9%25B2%25E6%25B6%25A9%25E5%2590%2583%25E4%25BB%2580%25E4%25B9%2588%25E8%258D%25AF%26shared_from_app%3D1&domain=mbd.baidu.com'

            # reqUrl = 'https://m.baidu.com/from=1000539d/s?word='+kw+'&sa=tb&ts=9861365&t_kt=0&ie=utf-8&rsv_t=0a95hrC%2B5SCTCUkyGtG%2FykFE%2FqzXw%2FPR8otwabIJgD7Q%2FtBGAmRT9EAKfB5LL5A&rsv_pq=11416320273004577527&ss=&rqlang=zh&oq='+kw

            # reqUrl = 'https://m.baidu.com/s?from=1000539d&word='+word

            # reqUrl = 'https://m.baidu.com/from=1000539d/s?word='+word+'&sa=tb&ts=9340812&t_kt=0&ie=utf-8&rsv_t=1565aAyJmDqW4PBCDZEPm50eEosiL8qHZKiP67L3oRAcBTGTTvsiKIxSsjnVfbk&rsv_pq=12055187561746828880&ss=100&sugid=27351537616859&rqlang=zh&rsv_sug4=7396&inputT=6165&oq=%E5%A5%B6%E7%B2%89%E9%80%9A%E8%B4%A7%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D'

            # encodeUrl = parse.quote(reqUrl)




            # browser.get(reqUrl)
            # inputBox=browser.find_element_by_id('index-kw')
            # submitBox=browser.find_element_by_id('index-bn')
            # https://mbd.baidu.com/ug_share/mbox/4a83aa9e65/share?product=search&tk=c86615a69edb69c4f83bb6da25c72b3f&share_url=https%3A%2F%2Fm.baidu.com%2Fs%3Fpu%3Dsz%25401320_480%252Ccuid%254001CFBC7DBE3DF95F8EB83B78F24205D6080BD46F3OSPTAARCGF%252Ccua%25401242_2688_iphone_12.6.0.11_0%252Ccut%2540iPhone13%252C4_15.4%252Cosname%2540baiduboxapp%252Cctv%25401%252Ccfrom%25401099a%252Ccsrc%2540bdbox_tserch_txt%252Ccud%2540MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAw%26bd_page_type%3D1%26word%3D%25E9%2598%25B4%25E9%2581%2593%25E5%25B9%25B2%25E6%25B6%25A9%25E5%25A6%2582%25E4%25BD%2595%25E8%25A7%25A3%25E5%2586%25B3%26sa%3Dtkb%26network%3D1_0%26t_samp%3Dpreload_4_1004%26from%3D1099a%26sugid%3D171923917851573%26ant_ct%3DOiCO%252F%252BZZeNw9Xmp96DYNYmYrD4xKqBGSn%252BJrRjfnRsQNoCRpcxdk6ybcJsvjS1m2%26rsv_sug4%3D1854%26rsv_pq%3D7268778685873060556%26isid%3Dea55b8ca1f075bb5a55253434ec5b646%26oq%3D%25E9%2598%25B4%25E9%2581%2593%25E5%25B9%25B2%25E6%25B6%25A9%25E5%2590%2583%25E4%25BB%2580%25E4%25B9%2588%25E8%258D%25AF%26shared_from_app%3D1&domain=mbd.baidu.com
            # inputBox.send_keys(kw)
            # submitBox.submit()


            # driver.get('http://m.baidu.com/s?from=1000539d')

            # WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id('se-bn').is_displayed())

            # action = TouchActions(browser)

            # action.tap(browser.find_element_by_id('se-bn').submit()).perform()

            # reSubmitBox = browser.find_element_by_id('se-bn')
            # action.double_tap(reSubmitBox).perform()





            # action.flick_element(reSubmitBox,0,-400,50).perform()

            # browser.execute(Command.SINGLE_TAP,{'element':submitBox.id})

            # reSubmitBox

        #     找到results
            results = browser.find_element_by_xpath('//div[contains(@class,"results")]')

            cResultList = results.find_elements_by_xpath('//div[contains(@class,"c-result")]')

            success = 0
            # aIndex = 0
            for cResult in cResultList:
                articleText = str(cResult.text)

                if articleText == None or articleText.find(kw)<0 :
                    # aIndex = aIndex +1
                    continue
                # aIndex = aIndex +1
                try:

                    # articleText = str(cResult.text)
                    # print(articleText)


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
                    #新判断方法
                    try:
                        combineClass = browser.find_elements_by_xpath('//div[contains(@class,"results")]/div[contains(@class,"c-clk-recommend")]')
                        if combineClass != None and len(combineClass) > 0 :
                            print("含有智能聚合")
                            aiCombineFlag=1
                        else:
                            print("不含智能聚合")

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






                    # try:
                    #     isAudio = cResult.find_element_by_xpath('//div[contains(@class,"audio")]')
                    #     if isAudio != None:
                    #         aiCombineFlag=1
                    #         print("含有语音")
                    #
                    # except Exception as ex:
                    #     print("不含语音")
                    #
                    # try:
                    #     if aiCombineFlag !=1:
                    #         isText = cResult.find_element_by_xpath('//span[contains(@style,"background-position:0 19px;")]')
                    #
                    #         print("含文章")
                    #         aiCombineFlag=1
                    # except Exception as ex:
                    #     print("不含文章")

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
                    # articleText = str(cResult.text)
                    # print(articleText)

                    # if articleText ==None or articleText.strip()=='':
                    #     try:
                    #         firstArticleTextList = cResult.find_elements_by_xpath('//div[contains(@class,"content__3urN- c-line-clamp4")]')
                    #         for firstAricleText in firstArticleTextList:
                    #             articleText = str(firstAricleText.text)
                    #             print(articleText)
                    #             break
                    #
                    #
                    #     except Exception as ex:
                    #         print("没找到top1的文本")




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
                        findSourceList = cResult.find_elements_by_xpath('//div[contains(@class,"c-line-clamp1 _3cEBX")]')

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
                        containIndex = 0
                        try:
                            findSourceList = cResult.find_elements_by_xpath('//div[contains(@class,"c-line-clamp1 _3d8C0")]')

                            if findSourceList !=None and len(findSourceList) >0:

                                for i in range(len(findSourceList)):
                                    if(articleText.find(findSourceList[i].text)>-1):
                                        print("含有父来源:"+str(findSourceList[i].text))
                                        containSource = 1
                                        containIndex = i
                            else:
                                containSource = 0
                                break

                        except Exception as ex:
                            print("不含有父来源")


                    if containSource == 0 :
                        containIndex = 0
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





                    ################################# 开始寻找聚合个数 #####################################

                    combineNum = 0
                    # if aiCombineFlag !=None and aiCombineFlag == 1:
                    if True:

                        trueHasCombine = 0


                        try:
                            # answerList = browser.find_elements_by_xpath('//div[contains(@class,"results")]//span[contains(@class,"_hg8DT")]')
                            reqCombineCount = 0

                            for reqCombineCount in range(3) :

                                # browser.get("http://m.baidu.com/s?from=1000539d&word="+word)

                                answerList = browser.find_elements_by_xpath('//div[contains(@class,"results")]//span[contains(@class,"_hg8DT")]')

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

                                                try:

                                                    combineNumUrl = 'https://m.baidu.com/sf?openapi=0&dspName=iphone&from_sf=1&pd=wenda_kg&resource_id=5243&srcid=5243&word='+word+'&dsp=iphone&title='+word+'&aptstamp=1650769854&top={%22sfhs%22:11}&frsrcid=235&atn=index&lid=11723748461556533071&referlid=11723748461556533071&ms=1&frorder=5'

                                                    # combineNumUrl = 'https://m.baidu.com/sf?openapi=0&dspName=iphone&from_sf=1&pd=wenda_kg&resource_id=5243&srcid=5243&word='+kw+'&dsp=iphone&title='+kw+'&aptstamp=1650694236&top=%7B%22sfhs%22%3A11%7D&frsrcid=235&atn=index'
                                                    browser.get(combineNumUrl)

                                                    time.sleep(1)


                                                    combineResults = browser.find_elements_by_xpath('//div[contains(@class,"c-infinite-scroll")]/div')

                                                    for kk in range(len(combineResults)):
                                                        comText = str(combineResults[kk].text)
                                                        if comText.find('广告')>-1:continue
                                                        if comText.find('医院')<0 and comText.find('医生') <0 and comText.find('医师') <0:continue
                                                        combineNum = combineNum + 1


                                                    aaaaa=3
                                                except Exception as ex:
                                                    print("跳转寻找专家回答个数出错了，"+str(ex))















                                                break;

                                            filterText = answerText[expertAudioIndex+6:len(answerText)]

                                            expertAudioIndex = filterText.find('条')

                                            expertAudioNum = int(filterText[0:expertAudioIndex])
                                            print("含有专家解答个数："+str(expertAudioNum))

                                            combineNum = expertAudioNum

                                            break

                                break
                                # if trueHasCombine == 1: break
                                # browser.get("http://m.baidu.com/s?from=1000539d&word="+word)

                                # action = webdriver.TouchActions(browser)

                                # action.tap(browser.find_element_by_id('se-bn').submit()).perform()

                                # reSubmitBox = browser.find_element_by_id('se-bn')
                                # action.tap(reSubmitBox).perform()

                                # reSubmitBox.submit()
                                # time.sleep(0.5)

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
                    if reqNum==2:
                        print("出错了,原因:"+str(ex))
                        sql = "INSERT INTO `baidu_keyword_standard` (`query_id`,`query`,`heat`,`msg`,`keyword_type`,`package_type`) values (%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql, [index,kw,heat,str(ex),keywordType,packageType])
                        conn.commit()
                    break
            if success ==1:
                break
            print(kw+"完成")
        except Exception as ex:

            if reqNum==2:
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




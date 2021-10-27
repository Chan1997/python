import pymysql
from selenium import webdriver



conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")

cursor = conn.cursor()


browser = webdriver.Chrome()


browser.add_cookie({
    "acw_tc":"0ed7ac9816139602472732069e7ebb1f301daf66ee41b372ec95c202d9",

})



href="https://v.youku.com/v_show/id_XMjI2NTgzMTY0.html"

browser.get(href)

list1=browser.find_elements_by_xpath('//div[contains(@class,"drama-list")]/div[contains(@class,"drama-tab")]/dt/span/a')

insert=0

dramalistnum=0

#单集
list2=browser.find_elements_by_xpath('//div[contains(@class,"drama-list")]/div[contains(@class,"drama-content")]/div[1]//a')
for ll in list2:
    ahref=str(ll.get_attribute('href'))
    # title=aa.get_attribute('title')
    # print(title)
    try:
        end=ahref.index("html")
        ahref=ahref[0:end+4]
    except:
        print("链接截取失败")
        continue


    try:
        insert=insert+1
        sql="INSERT INTO `video_episodes` (`v_id`, `episode_num`, `href_id`) VALUES (%s,%s,%s)"
        cursor.execute(sql, [1412,insert,ahref])
        conn.commit()
    except:
        print("插入失败")


#多集
for a in list1:

    try:
      a.click()
      browser.implicitly_wait(5)
      print("打开"+a.text)
      dramalistnum=dramalistnum+1
      print(dramalistnum)
      dramalist=browser.find_elements_by_xpath('//div[contains(@class,"drama-list")]/div[contains(@class,"drama-content")]/div[@id="listitem_page'+str(dramalistnum)+'"]//a')
    except:
        break
    for aa in dramalist:
        ahref=str(aa.get_attribute('href'))
        # title=aa.get_attribute('title')
        # print(title)
        try:
            end=ahref.index("html")
            ahref=ahref[0:end+4]
        except:
            print("链接截取失败")
            continue


        try:
            insert=insert+1
            sql="INSERT INTO `video_episodes` (`v_id`, `episode_num`, `href_id`) VALUES (%s,%s,%s)"
            cursor.execute(sql, [1412,insert,ahref])
            conn.commit()
        except:
            print("插入失败")



try:
    expand=browser.find_element_by_xpath('//div[contains(@class,"drama-list")]/div[contains(@class,"drama-tab")]/dt/span[last()]')
    expand.click()
    print("展开按钮")

    dnum=browser.find_elements_by_xpath('//div[contains(@class,"drama-list")]/div[contains(@class,"drama-tab")]/dd/span')



    for num in range(1,len(dnum)+1):

        dbutton=browser.find_element_by_xpath('//div[contains(@class,"drama-list")]/div[contains(@class,"drama-tab")]/dd/span['+str(num)+']/a')

        dbutton.click()
        browser.implicitly_wait(5)
        print("打开第"+dbutton.text+"按钮")
        dramalistnum=dramalistnum+1
        print(dramalistnum)
        dramalist=browser.find_elements_by_xpath('//div[contains(@class,"drama-list")]/div[contains(@class,"drama-content")]/div[@id="listitem_page'+str(dramalistnum)+'"]//a')

        for aa in dramalist:
            ahref=str(aa.get_attribute('href'))
            # title=aa.get_attribute('title')
            # print(title)
            try:
              end=ahref.index("html")
              ahref=ahref[0:end+4]
            except:
               print("链接截取失败")
               continue


            try:
              insert=insert+1
              sql="INSERT INTO `video_episodes` (`v_id`, `episode_num`, `href_id`) VALUES (%s,%s,%s)"
              cursor.execute(sql, [1412,insert,ahref])
              conn.commit()
            except:
              print("插入失败")

        expand.click()




except:
    print("按钮展开失败")


print("共插入"+str(insert))

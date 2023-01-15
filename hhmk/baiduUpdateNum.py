from urllib import parse
from urllib.parse import urlencode
from selenium import webdriver
import pymysql




conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")

cursor = conn.cursor()

browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

querySql = "select * from `baidu_keyword_standard` where combine_num is null order by create_time "
cursor.execute(querySql)

list = cursor.fetchall()

index = 1
goFlag = 0
for row in list:

    # if index <=2 :
    #     index = index +1
    #     continue

    queryId = row[0]
    kw = row[1]

    isCombine = row[4]
    keywordType = row[11]


    print("当前索引："+str(index)+";关键词："+kw+";当前分类："+keywordType)

    for reqNum in range(0,3):

        try:

            browser.get("http://m.baidu.com")
            inputBox=browser.find_element_by_id('index-kw')
            submitBox=browser.find_element_by_id('index-bn')

            inputBox.send_keys(kw)
            submitBox.submit()

            results = browser.find_element_by_xpath('//div[contains(@class,"results")]')
            cResultList = results.find_elements_by_xpath('//div[contains(@class,"c-result")]')

            success = 0

            combineNum = 0

            for cResult in cResultList:
                try:

                    try:
                        article = cResult.find_element_by_xpath('//article')
                    except Exception as ex:
                        print("找不到article")
                        raise Exception("找不到搜索的article")

                    ################################# 开始寻找语音聚合个数 #####################################



                    errorMsg = None
                    if isCombine !=None and isCombine == 1:
                        try:
                            answerList = browser.find_elements_by_xpath('//div[contains(@class,"results")]//span[contains(@class,"_eqzF7")]')

                            if answerList !=None and len(answerList) >0:
                                for i in range(len(answerList)):
                                    answerText = str(answerList[i].text)
                                    # print(answerText)
                                    expertAudioIndex = answerText.find('专家回答')
                                    if expertAudioIndex >-1:

                                        filterText = answerText[expertAudioIndex+6:len(answerText)]

                                        expertAudioIndex = filterText.find('条')

                                        expertAudioNum = int(filterText[0:expertAudioIndex])
                                        print("含有专家解答个数："+str(expertAudioNum))

                                        combineNum = expertAudioNum

                                        break
                        except Exception as ex:
                            errorMsg = str(ex)
                            print("寻找专家聚合个数出错了，"+str(ex))


                    print("请求"+str(reqNum+1)+"次成功")

                    sql = "UPDATE `baidu_keyword_standard` SET `msg` = %s,`update_time` = SYSDATE(),`combine_num` = %s where `query_id` = %s  and `keyword_type` = %s "
                    cursor.execute(sql,[errorMsg, combineNum,queryId,keywordType])
                    conn.commit()


                    success = 1
                    break
                except Exception as ex:
                    print(str(ex))
                    if reqNum==2:
                        print("出错了,原因:"+str(ex))
                        sql = "UPDATE `baidu_keyword_standard` SET `msg` = %s,`update_time` = SYSDATE() where `query_id` = %s  and `keyword_type` = %s "
                        cursor.execute(sql,[str(ex), queryId,keywordType])
                        conn.commit()
                    break






            if success ==1 :
                print(kw+"完成")
                break
            print(kw+"失败"+str(reqNum+1)+"次")
        except Exception as ex:
            if reqNum==2:
                sql = "UPDATE `baidu_keyword_standard` SET `msg` = %s,`update_time` = SYSDATE() where `query_id` = %s and `keyword_type` = %s "
                cursor.execute(sql,[str(ex), queryId,keywordType])
                conn.commit()
                print("请求三次最终都出错了,原因:"+str(ex))

    index = index +1
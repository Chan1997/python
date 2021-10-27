
# import urllib
import pymysql

from selenium import webdriver as web

from urllib.parse import quote

class getEpisode:

    def __init__(self):
        a=0

    def getlist(title,v_id,sum):

        conn = pymysql.connect(host="127.0.0.1",port=3307, user="root",password="123456",database="myblog")

        cursor = conn.cursor()

        title1=quote(title)

        # print(title1)






        browser = web.Chrome()



        newhref="https://so.youku.com/search_video/q_"+title1



        browser.get(newhref)

        # browser.find_element_by_class_name()

        try:
            skmod=browser.find_elements_by_xpath('//div[contains(@class,"sk-result-list")]/div')


            modindex=1
            for mod in skmod:
                modclass=mod.get_attribute('class')

                if modclass!="sk-mod":
                    modindex=modindex+1
                    print("不是需要的skmod")
                else:

                    strmodindex=str(modindex)

                    insert=0
                    try:
                      # ul=browser.find_elements_by_xpath('//div[contains(@class,"sk-result-list")]/div['+modindex+']//ul')

                      # ulnum=len(ul)
                      try:
                          lanbutton=browser.find_elements_by_xpath('//div[contains(@class,"sk-result-list")]/div['+strmodindex+']//div[contains(@class,"tab-lang-wrap")]/ul/li/a')
                          if len(lanbutton)<=0:
                              print("未找到语种选择")

                          for button in lanbutton:
                             if button.text=="粤语":
                                button.click()
                                print("选择粤语")
                                break

                      except:
                          print("未找到语种选择")


                      try:
                          clicka=browser.find_element_by_xpath('//div[contains(@class,"sk-result-list")]/div['+strmodindex+']//ul[1]/li[contains(@class,"item-expand")]')
                          clicka.click()
                          print("展开集数")


                      except:
                          print("未找到展开按钮")

                      try:

                        tabnav=browser.find_elements_by_xpath('//div[contains(@class,"sk-result-list")]/div['+strmodindex+']//div[contains(@class,"slider-content")]//ul/li/a')

                        for tabs in tabnav:

                            print("打开翻页按钮")
                            tabs.click()

                            itemss=browser.find_elements_by_xpath('//div[contains(@class,"sk-result-list")]/div['+strmodindex+']//ul/li/a')

                            for ite in itemss:
                                href=str(ite.get_attribute('href'))

                                try:
                                    end=href.index("html")
                                    href=href[0:end+4]
                                except:
                                    print("链接截取失败")
                                    continue

                                try:
                                    sql="INSERT INTO `video_episodes` (`v_id`, `episode_num`, `href_id`) VALUES (%s,%s,%s)"

                                    cursor.execute(sql, [v_id,int(ite.text),href])

                                    conn.commit()

                                    insert=insert+1
                                except:
                                    conn.rollback()



                        if len(itemss)>0:
                            if insert==0:
                               modindex=modindex+1
                               print("插入为0继续搜索下一个mod")
                               continue


                            browser.close()

                            print("更新到"+str(sum)+"集,插入成功"+str(insert))

                            return
                      except:
                          print("未找到翻页集数按钮")


                      items=browser.find_elements_by_xpath('//div[contains(@class,"sk-result-list")]/div['+strmodindex+']//ul/li/a')

                      for it in items:
                              href=str(it.get_attribute('href'))

                              try:
                                  end=href.index("html")
                                  href=href[0:end+4]
                              except:
                                  print("链接截取失败")
                                  continue

                              try:
                                  sql="INSERT INTO `video_episodes` (`v_id`, `episode_num`, `href_id`) VALUES (%s,%s,%s)"

                                  cursor.execute(sql, [v_id,int(it.text),href])

                                  conn.commit()

                                  insert=insert+1
                              except:
                                  conn.rollback()




                    except:
                        print("")


                    if insert==0:
                        modindex=modindex+1
                        print("插入为0继续搜索下一个mod")
                        continue

                    browser.close()

                    print("更新到"+str(sum)+"集,插入成功"+str(insert))

                    return



        except:
            print("未找到匹配")


        browser.close()

        # headers = {
        #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        # }
        #
        #
        # req = urllib.request.Request("https://so.youku.com/search_video/q_"+title1,headers=headers)
        #
        # webpage = urllib.request.urlopen(req)
        #
        # html = webpage.read()
        #
        # html=html.decode('utf-8')
        #
        # element=etree.HTML(html)
        #
        # print(html)



        # items=element.xpath('//div[contains(@class,"sk-result-list")]/div[1]//ul/li/a/@title')

        # try:
        #  items=browser.find_elements_by_xpath('//div[contains(@class,"sk-result-list")]/div[1]//ul')
        #
        #  insert=0
        #
        #  # preview=0
        #
        #  # print(len(items))
        #
        #   for ul in items :
        #
        #
        #
        #
        #  try:
        #      clicka=browser.find_element_by_xpath('//div[contains(@class,"sk-result-list")]/div[1]//ul/li[contains(@class,"item-expand")]')
        #      clicka.click()
        #      print("展开所有集数")
        #  except:
        #      print("未找到展开按钮")
        #
        #
        #  for it in items354:
        #      href=str(it.get_attribute('href'))
        #      try:
        #         end=href.index("html?")
        #
        #         href=href[0:end+4]
        #      except:
        #         print("链接截取失败")
        #         continue
        #
        #
        #
        #
        #
        #
        #
        #      try:
        #          sql="INSERT INTO `video_episodes` (`v_id`, `episode_num`, `href_id`) VALUES (%s,%s,%s)"
        #
        #
        #          end=href.index("")
        #
        #          cursor.execute(sql, [v_id,int(it.text),href])
        #          conn.commit()
        #          insert=insert+1
        #      except:
        #          conn.rollback()
        #
        #      # print("集数"+it.text+"链接:"+it.get_attribute('href'))
        # except:
        #
        #     print("error")

            # href=browser.xpath('//div[contains(@class,"sk-result-list")]/div[1]//ul/li/a[@title="'+it+'"]/@href')

            # epi=browser.xpath('//div[contains(@class,"sk-result-list")]/div[1]//ul/li/a[@title="'+it+'"]/text()')

            # print("集数:"+epi+"链接"+href)


            # print(it)

            # icon=element.xpath('//div[contains(@class,"drama-content")]/div/div[@item-id="'+it+'"]//span[contains(@class,"label-preview")]')
            #
            # if icon:
            #     preview=preview+1
            # else:
            #     epi=element.xpath('//div[contains(@class,"drama-content")]/div/div[@item-id="'+it+'"]/@seq')
            #     print(it+"集数:"+epi[0])
            #     insert=insert+1


            # icon=it.xpath('//span[contains(@class,"label-preview")]')
            #
            # print(icon)
            #
            # if icon:
            #     print("预告共"+str(preview))
            #     preview=preview+1
            # else:
            #     episode=it.xpath('/@seq')
            #
            #     print("aaa")
            #     # episode=int(episode)
            #
            #     hrefid=it.xpath('/@item-id')
            #
            #     hrefid=str(hrefid)
            #
            #     hrefid=hrefid[5:len(hrefid)]
            #
            #     sql="INSERT INTO `video_episodes` (`v_id`, `episode_num`, `href_id`) VALUES (%s,%s,%s)"
            #
            #     try:
            #         cursor.execute(sql, [v_id,episode,hrefid])
            #
            #         conn.commit()
            #
            #         insert=insert+1
            #     except:
            #         conn.rollback()









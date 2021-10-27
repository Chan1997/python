import pymysql
import json as Json


import requests

class YiTong():


    def __init__(self):
        a=0


    def getCookie(self,name,value):
        return {
            'domain': '.drcuiyutao.com',
            'name': name,
            'value': value,
            'path': '/',
            'expires': None,
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False,
        }

    def getPostHeader(self):

        return {
            "Host": "api.etmcn.com",
            "Connection": "keep-alive",
            "Content-Length": "185",
            # "Access-Control-Request-Method":"POST",
            "Origin": "https://mos.etmcn.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
            "Authorization":"97d941448d304ea88a85b69629c6cf28",
            "etm-organization-id":"e793aa886341c29dd33fcb03aa8b0340",
            "Content-Type":"application/json;charset=UTF-8",
            "Accept":"application/json, text/plain, */* ",
            "Referer":"https://mos.etmcn.com/cm_evaluation/",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
        }

    def getHeader(a):
        return {
            "Host": "api.etmcn.com",
            "Connection": "keep-alive",
            "Accept":"application/json, text/plain, */* ",
            "Origin": "https://mos.etmcn.com",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
            "Authorization" : "97d941448d304ea88a85b69629c6cf28",
            "etm-organization-id":"e793aa886341c29dd33fcb03aa8b0340",
            "Referer":"https://mos.etmcn.com/cm_evaluation/",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
        }

postHeader ={
    "Host": "api.etmcn.com",
    "Connection": "keep-alive",
    "Content-Length": "185",
    # "Access-Control-Request-Method":"POST",
    "Origin": "https://mos.etmcn.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
    "Authorization":"bd6f06a902864064945b41579b58efc2",#此值会过期 要更新
    "etm-organization-id":"e793aa886341c29dd33fcb03aa8b0340",
    "Content-Type":"application/json;charset=UTF-8",
    "Accept":"application/json, text/plain, */* ",
    "Referer":"https://mos.etmcn.com/cm_evaluation/",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
}

editPostHeader = {
    "Host": "api.etmcn.com",
    "Connection": "keep-alive",
    "Content-Length": "210",
    # "Access-Control-Request-Method":"POST",
    "Origin": "https://mos.etmcn.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
    "Authorization":"bd6f06a902864064945b41579b58efc2",#此值会过期 要更新
    "etm-organization-id":"e793aa886341c29dd33fcb03aa8b0340",
    "Content-Type":"application/json;charset=UTF-8",
    "Referer":"https://mos.etmcn.com/cm_evaluation/",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
}


header={
    "Host": "api.etmcn.com",
    "Connection": "keep-alive",
    "Accept":"application/json, text/plain, */* ",
    "Origin": "https://mos.etmcn.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
    "Authorization" : "bd6f06a902864064945b41579b58efc2",
    "etm-organization-id":"e793aa886341c29dd33fcb03aa8b0340",
    "Referer":"https://mos.etmcn.com/cm_evaluation/",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
}

y = YiTong()

conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")


cursor = conn.cursor()


#带上session

getQuestionUrl = "https://api.etmcn.com/evaluation/client/question?birthday=" #GET请求  2021-01-05

postScoreUrl = "https://api.etmcn.com/evaluation/client/evaluation" #POST请求

postScoreObject =[{
        "ability": "FINE_ACTION",
        "score": 5
    }, {
        "ability": "ADAPTABILITY",
        "score": 5
    }, {
        "ability": "LANGUAGE",
        "score": 5
    }, {
        "ability": "SOCIAL_INTERCOURSE",
        "score": 5
    }, {
        "ability": "BIG_ACTION",
        "score": 5
    }]

# 返回json：{"data":"{\"id\":321,"age" }"}  此id为报告id

editSourceUrl = "https://api.etmcn.com/evaluation/client/child_and_customer"

editSourceObject = {
    "avatar": None,
    "name": "小宝",
    "gender": "FEMALE",
    "birthday": "2021-01-01",
    "birthWay": "SPONTANEOUS_LABOR",
    "height": 65,
    "weight": 20,
    "areaId": "440105",
    "address": None,
    "customerName": "董",
    "relationshipName": "FATHER"
}



getReportUrl = "https://api.etmcn.com/evaluation/client/evaluation/"  #带报告ID

#0岁1月         2015-2021
#year = 2020
errMsg = ''
currentYear = -1



for year in range (2015,2022):

  currentYear= currentYear +1


  for month in range(1,12):
    monthStr = str(month)
    if month<10:
        monthStr="0"+monthStr
    birthday = str(year)+"-"+monthStr+"-"+"01"
    # preDate = str(currentYear)+"岁"+str(month)+"月"

    #更改生日资料
    editSourceObject['birthday'] = birthday
    sourceJson = Json.dumps(editSourceObject)
    requests.put(url=editSourceUrl,data=sourceJson,headers=editPostHeader)

    editHtml = requests.request('GET',url=editSourceUrl,headers=header)
    editJson = Json.loads(editHtml.content)
    preDate = editJson['data']['age']



    try:

        print("当前宝宝生日："+birthday)

        html = requests.request('GET',url=getQuestionUrl+birthday,headers=header)

        if html == None:
            print("返回值为空")
            raise Exception('返回值为空')


        print(html.content)

        myJson = Json.loads(html.content)


        #错误码
        code = myJson['code']

        if code !=0:
            if(code==401):
              print("响应出错了，无权限或权限验证码失效了")
              raise Exception('响应出错了，无权限或权限验证码失效了')
            else:
              print("出错了，错误响应码："+code+"，原因："+myJson['message'])
              raise Exception("出错了，错误响应码："+code+"，原因："+myJson['message'])


        #返回数据
        jsonData = myJson['data']

        if(jsonData == None):
           print("返回数据为空，生日："+birthday)
           raise Exception("返回数据为空，生日："+birthday)


        tools = jsonData['tools']
        toolStr = ''
        if tools != None:
            for t in tools:
                toolStr += t+","

        questionList = jsonData['evaluationQuestionList']
        #遍历问题
        for question in questionList:
            ability = question['ability']
            insideQuestions = question['questions']
            for inquestion in insideQuestions:
                content= inquestion['content']
                image = inquestion['image']
                score = inquestion['score']

                sql = "INSERT INTO `yi_tong` (`birthday`,`pre_date`,`content`,`image`,`score`,`ability`,`tools`) values (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, [birthday,preDate,content,image,score,ability,toolStr])
                conn.commit()

        #存完问题后，提交分数并获取报告id post请求

        # postScoreJson = Json.JSONEncoder().encode(postScoreObject)
        postScoreJson = "[{\"ability\":\"FINE_ACTION\",\"score\":5},{\"ability\":\"ADAPTABILITY\",\"score\":5},{\"ability\":\"LANGUAGE\",\"score\":5},{\"ability\":\"SOCIAL_INTERCOURSE\",\"score\":5},{\"ability\":\"BIG_ACTION\",\"score\":5}]"
        response = requests.post(url=postScoreUrl,data=postScoreJson,headers=postHeader)


        print("reponse:"+str(response.content))
        responseJson = Json.loads(response.content)
        if responseJson['code'] != 0:
            raise Exception("获取报告id出错，原因："+responseJson['message'])

        responseData = responseJson['data']
        reportId = responseData['id']
        heightDevelopment = Json.loads(responseData['heightDevelopmentSnapshot'])
        weightDevelopment = Json.loads((responseData['weightDevelopmentSnapshot']))
        heightDevelopmentStr = ''
        weightDevelopmentStr = ''

        for hd in heightDevelopment:
            lowerLimit = hd['lowerLimit']
            standard = hd['standard']
            upperLimit = hd['upperLimit']
            hdMonth = hd['month']
            heightDevelopmentStr += "月份："+str(hdMonth)+"-最低高度："+str(lowerLimit)+"-标准高度："+str(standard)+"-最大高度："+str(upperLimit)+"；"
        for wd in weightDevelopment:
            wdMonth = wd['month']
            lowerWeight = wd['lowerBodyWeight']
            weightLimit = wd['weightLimit']
            weightStandard = wd['weightStandard']
            weightDevelopmentStr +="月份："+str(wdMonth)+"-最低重量："+str(lowerWeight)+"-标准重量："+str(weightStandard)+"-最大重量："+str(weightLimit)+"；"

        reportHtml = requests.request('GET',url=getReportUrl+str(reportId),headers=header)

        print("reportHtml:"+str(reportHtml.content))

        resultJson = Json.loads(reportHtml.content)

        if resultJson['code'] != 0:
            raise Exception("获取最终结果出错，原因："+resultJson['message'])

        resultData = resultJson['data']
        resultAge = resultData['age']
        resultRating = resultData['rating']
        evaluatedParts = resultData['evaluatedParts']
        resultFineAction=''
        resultAdaptability = ''
        resultLanguage = ''
        resultSocial = ''
        resultBigAction = ''
        for part in evaluatedParts:
            partAbilityName = part['abilityName']
            if partAbilityName == 'FINE_ACTION':
                resultFineAction = part['report']
            if partAbilityName == 'ADAPTABILITY':
                resultAdaptability = part['report']
            if partAbilityName == 'LANGUAGE':
                resultLanguage = part['report']
            if partAbilityName == 'SOCIAL_INTERCOURSE':
                resultSocial = part['report']
            if partAbilityName == 'BIG_ACTION':
                resultBigAction = part['report']

        resultSql = "INSERT INTO `yi_tong_result` (`birthday`,`pre_date`,`age`,`weight_development`,`height_development`,`fine_action`,`adaptability`,`language`,`social_intercourse`,`big_action`,`rating`,`report_id`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  "
        cursor.execute(resultSql, [birthday,preDate,resultAge,weightDevelopmentStr,heightDevelopmentStr,resultFineAction,resultAdaptability,resultLanguage,resultSocial,resultBigAction,resultRating,reportId])
        conn.commit()


























    except Exception as ex:
        print("出错了，生日："+birthday+" ,原因:"+str(ex))





















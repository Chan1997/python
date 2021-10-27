import pymysql
import json as Json


import requests

header={
    "Host": "api.etmcn.com",
    "Connection": "keep-alive",
    "Accept":"application/json, text/plain, */* ",
    "Origin": "https://mos.etmcn.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat",
    "Authorization" : "dfd631ab459347b6a31bd2f33fd32f95",
    "etm-organization-id":"e793aa886341c29dd33fcb03aa8b0340",
    "Referer":"https://mos.etmcn.com/cm_evaluation/",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
}

conn = pymysql.connect(host="127.0.0.1",port=3306, user="root",password="123456",database="myblog")


cursor = conn.cursor()

proReportUrl = "https://api.etmcn.com/evaluation/client/evaluation/paid/"


searchSql = " select * from `yi_tong_result` "

cursor.execute(searchSql)

list = cursor.fetchall()

for report in list:
    print(report[len(report)-1])
    reportId = report[len(report)-1]
    birthday = report[1]
    preDate =  report[2]

    html = requests.request('GET',url=proReportUrl+str(reportId),headers=header)
    myJson = Json.loads(html.content)
    jsonData = myJson['data']


    avgScore = jsonData['averageScore']

    developmentGrade =jsonData['developmentalGrade']

    developmentGradeStr = '描述：'+developmentGrade['developmentalGradeDescription']+"；状态："+developmentGrade['developmentalStatus']+"；偏移量："+str(developmentGrade['percentDeviation'])







    evaluatedParts = jsonData['evaluatedParts']
    familyDiet = jsonData['familyDiet']
    heightDevelopment = jsonData['heightDevelopments']
    weightDevelopment = jsonData['weightDevelopments']
    reminder = jsonData['reminder']

    heightDevelopmentStr = ''
    weightDevelopmentStr = ''

    for hd in heightDevelopment:
        lowerLimit = hd['lowerLimit']
        standard = hd['standard']
        upperLimit = hd['upperLimit']
        hdMonth = hd['month']
        heightDevelopmentStr += "宝宝月份："+str(hdMonth)+"-最低高度："+str(lowerLimit)+"-标准高度："+str(standard)+"-最大高度："+str(upperLimit)+"；"
    for wd in weightDevelopment:
        wdMonth = wd['month']
        lowerWeight = wd['lowerBodyWeight']
        weightLimit = wd['weightLimit']
        weightStandard = wd['weightStandard']
        weightDevelopmentStr += "宝宝月份："+str(wdMonth)+"-最低重量："+str(lowerWeight)+"-标准重量："+str(weightStandard)+"-最大重量："+str(weightLimit)+"；"




    resultFineAction=''
    resultAdaptability = ''
    resultLanguage = ''
    resultSocial = ''
    resultBigAction = ''

    fineActionTrain = ''
    adaptabilityTrain = ''
    languageTrain = ''
    socialTrain = ''
    bigActionTrain = ''


    for part in evaluatedParts:
        partAbilityName = part['abilityName']
        list1 = part['reports']
        list2 = part['trainingPrograms']
        if partAbilityName == 'FINE_ACTION':
            for r in list1:
                resultFineAction += r
            for t in list2:
                fineActionTrain += t
        if partAbilityName == 'ADAPTABILITY':
            for r in list1:
                resultAdaptability += r
            for t in list2:
                adaptabilityTrain += t
        if partAbilityName == 'LANGUAGE':
            for r in list1:
                resultLanguage += r
            for t in list2:
                languageTrain += t
        if partAbilityName == 'SOCIAL_INTERCOURSE':
            for r in list1:
                resultSocial += r
            for t in list2:
                socialTrain += t
        if partAbilityName == 'BIG_ACTION':
            for r in list1:
                resultBigAction += r
            for t in list2:
                bigActionTrain += t

    proReportSql = "INSERT INTO `yi_tong_result_pro` (`report_id`,`birthday`,`pre_date`,`development_grade`,`fine_action_report`,`fine_action_train`,`adaptability_report`,`adaptability_train`,`language_report`,`language_train`,`social_intercourse_report`,`social_intercourse_train`,`big_action_report`,`big_action_train`,`weight_development`,`height_development`,`family_diet`,`reminder`,`average_score`) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


    cursor.execute(proReportSql, [reportId,birthday,preDate,developmentGradeStr,resultFineAction,fineActionTrain,resultAdaptability,adaptabilityTrain,resultLanguage,languageTrain,resultSocial,socialTrain,resultBigAction,bigActionTrain,weightDevelopmentStr,heightDevelopmentStr,familyDiet,reminder,avgScore])
    conn.commit()











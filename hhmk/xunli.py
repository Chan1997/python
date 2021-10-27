# 国庆寻鲤记游戏
import requests
from urllib import parse
import time

header={
    "Host": "datareport.fkw.com",
    "Connection": "keep-alive",
    "Accept":"image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
    "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.14(0x18000e26) NetType/WIFI Language/zh_CN",
    "Referer":"https://19668951-291.hd.faisco.cn/19668951/TU-KZnst6iKVpRmHOISapQ/hxdzz.html?isOfficialLianjie=false&canalOldOld=-1&shareDeep=8&eleUid=&_origin=3&flyerfid=&_source=3&from=singlemessage&notP4Share=false&jumpFlag=true&canalOld=-1&canal=-1",
    "Accept-Encoding":"br, gzip, deflate",
}

reportUrl = "https://datareport.fkw.com/js/report?source_type=1&source_opt_type=10002"

reportUrl = reportUrl + "&source_content="+parse.quote('{"title":"进入了游戏活动"}')

reportUrl = reportUrl + "&viewer_fai_openid=oosnVwgeEO9PxeiHwAxqQ0Vu6pMo&viewer_fai_unionid=oosnVwgeEO9PxeiHwAxqQ0Vu6pMo"

reportUrl = reportUrl + "&head_img_url="+parse.quote('https://thirdwx.qlogo.cn/mmopen/vi_32/jqA6aIULoDMlqV1uLbz0r2rc6NZLMWsQBf90qUNoVSxbFicBz3UGYh7OX6TGeDxmMk0fbXSaA6YhBB95gaNcsVw/132')

reportUrl = reportUrl +"&nickname="+parse.quote('宇文')

reportUrl = reportUrl + "&client_net=&app_type=5&client_device=iphone&source_biz=1"

reportUrl = reportUrl + "&recordTicket=" +""

reportUrl = reportUrl + "&is_outside_visit=false&report_type=2&b_rt=10& "



ticket1 = "4Q059Hi/ZinD3gj4t1f3r03EQFXc/cK7rocP5s1X2JWr0LjsmUg3pBZP//RpsIkQ1G3neY6Mjuyh2TuEfBWXxdP2Ldq7vjFhWZOIusqZR5Y64uUpvVe9FUabFs9MwypBEymIm/dGvfweeyvQ6OiY0Us5HK8XdVp7V6CVCQ0S5Etgui4sAAvWpsx4dGTMBS1nUD2gBJq7FmVckFX50qyxdE4CUoLibLVaGOW556lwWkc="


for i in range(0,100):



    html = requests.request('GET',url=reportUrl,headers=header)

    time.sleep(0.5)



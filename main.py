import time
import json
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

from aip import AipOcr


#BEGIN
APP_ID = '25087602'
API_KEY = 'GmkAjvG9HLYy2F2RUNM0h8pW'
SECRET_KEY = 'HM4efodMjqKgFqqtSuoBaPVyUfigTlYB'
#END
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


URLs = OrderedDict({
    '招财学长': 'https://www.zhihu.com/people/cyy-7-36-42',
    '老罗养基笔记': 'https://www.zhihu.com/people/lao-luo-yang-ji-bi-ji',
    '韭哥有话说': 'https://www.zhihu.com/people/zhi-zi-24-19',
    'Jerry': 'https://www.zhihu.com/people/ke-ai-de-ting-ting-60',
    '端王府': 'https://www.zhihu.com/people/gong-zi-ban-hua',
    '唐之夭夭': 'https://www.zhihu.com/people/jontang',
    '扬海复利玩基金': 'https://www.zhihu.com/people/xie-liang-jie-huo',
    '搬砖小浪哥': 'https://www.zhihu.com/people/zhuang-gui-jun-50',
})

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Cookie': 'SESSIONID=diyd3HF2nmWHaIbjQuCckMhtSAD2Oh0bvVN4QR3bePW; JOID=U1gRAkKYXnMEAsPnWZm3qYm0p8VI6jYPOTi4mR3bZ05EfrKzErqzyWULxuZU1-GFa3OfemaLndox8blto_GINbI=; osd=UVkcAU-aX34HD8HmVJq6q4i5pMhK6zsMNDq5lB7WZU9Jfb-xE7ewxGcKy-VZ1eCIaH6de2uIkNgw_LpgofCFNr8=; _zap=75f1af63-bc17-4f19-8e49-82afdcf3e823; d_c0="AKCQfsZWKxSPTg0OeyBoL8G40KoOIpD6Z6w=|1639285812"; _xsrf=ldl8QAxDKXbttGqNF2FubeECOLGB6oAP; captcha_session_v2="2|1:0|10:1639289450|18:captcha_session_v2|88:NHQ4bzJLdXpMdzVtL1ovdThaeVdEUDJ5KzRkQ2Q2WEhOY053WC92WUIvVWw1OWJrb1o0ZWQ0V0xmcll2NWxTUQ==|a08973aa579c5c9ac6d77f5bb3fc28ef5a4de8f03f868d73b604ff15f15b8e55"; __snaker__id=a5VdY3CoZzmgSXIA; _9755xjdesxxd_=32; gdxidpyhxdE=XyckzQRX5ocTuD0fzjjOuiEg%2B%2FSSvVpfTC9jzRNykbhR8NmnGMGSdMSv88ICX3e%2FABovltIMARxTteJiMTKd6lJyz3YR7yKJodI8%2BTOJPRh95fMxfSxSGai2tlWsjM545SpazrIN%5CDIUrX4NR4crkhGwYEcTQi5qS1Tpxj5%2Fv%2FH9SN%2Fh%3A1639290351202; YD00517437729195%3AWM_NI=MZYVslqxT1e3pyPK9%2Fnigas63B%2Fq8nzeLIyGMnxAmGbwiKcMSVNSTajMDEdNQTrSnfq1LqrtWho%2BstrGqaQlhB%2FCoFwQqV%2Bh7sNPZxVLr9POwuxG%2FTC7HWYGkPOr2cj6eVg%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb3db638defa7bbc740a3b48fb7d14a869e8b85b680b4b3a3bad13db689bad8ee2af0fea7c3b92a8f8697b7f268b3a89cd2e839b4a7a0acbc25aeb7a982f23ef19ee192bb66babb84aafc4d8fb2b8a2f04da2a9a7ace247918a82b4d76baa938ca6e746938cbeb4ed6eb3ef8492f18095b8a1ccf280b299bf82d468ac9ee1a4ee4eb58fbfb7aa64f5ad82b1d9749694bedad345b5abb8a8ae6081e988b8dc4da9908193b169aaeaabb7e637e2a3; YD00517437729195%3AWM_TID=KDkuhlmKFFdFRFEVVEYrtsnmdFrvTvrs; z_c0="2|1:0|10:1639289469|4:z_c0|92:Mi4xanVOREJRQUFBQUFBb0pCLXhsWXJGQ2NBQUFDRUFsVk5mQl9kWVFBMGluTU5sNUNiYk16YnZ4WEZ4T0xmOXRxUENR|411009678cff040369198b2969b3f251da349904ae0b817e73ebbe2733b2ce0c"; NOT_UNREGISTER_WAITING=1; SESSIONID=sly52zzAK89EtyUOtBHnH3YoS2AicvWo16thKv5bPAJ; JOID=Ul0QC0o6QesDWdz1TTOlMYLmsNpcTC2fP2qjjwFwfNJLJKSlAhSmWGpd2fhJak1bwK5L_UsfKxj7FuRYEkzhLQo=; osd=UlsWBEo6R-0MWdzzSzylMYTgv9pcSiuQP2qliQ5wfNRNK6SlBBKpWGpb3_dJaktdz65L-00QKxj9EOtYEkrnIgo=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1639380347,1639381436,1639442983,1639443686; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1639443837; KLBRSID=e42bab774ac0012482937540873c03cf|1639443836|1639442977',
}
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}
client.setProxies(proxies)
ctime = time.localtime()

Result = {}
for name, URL in URLs.items():
    print('正在处理：', name)
    response = requests.get(URL, headers=headers, proxies=proxies)
    main_section = BeautifulSoup(response.text, 'html.parser').find_all(
        'div', attrs={'class': 'ListShortcut'})[0]
    for post in main_section.find_all('div', attrs={'class': 'List-item'}):
        post_time = post.find_all(
            'div', attrs={'class': 'ActivityItem-meta'})[0].find_all('span', limit=2)[-1].text
        if not (post_time.split('-')[2].split(' ')[0] == f"{ctime.tm_mday}"):
            continue
        title = post.find_all(
            'div', attrs={'class': 'ContentItem ArticleItem'})[0]
        post_link = title.next.next.get('href')

        post_response = requests.get(f'https:{post_link}', headers={
            'Cookie': 'SESSIONID=kiF6xEjW3LY4znMDsj84BFLLqx2EaYL8dzF1JulL1wy; JOID=VV4TBEiQ7hamIDCPTZELyCueVKFY4oJulxZL9Q3f1y_iUE3bArAapMclMY5IJmeyQsGHXV3lLEAEyXOLaYJjZXs=; osd=Wl0QB0Of7RWlKz-MTpIAxyidV6pX4YFtnBlI9g7U2CzhU0bUAbMZr8gmMo1DKWSxQcqIXl7mJ08HynCAZoFgZnA=; _zap=75f1af63-bc17-4f19-8e49-82afdcf3e823; d_c0="AKCQfsZWKxSPTg0OeyBoL8G40KoOIpD6Z6w=|1639285812"; _xsrf=ldl8QAxDKXbttGqNF2FubeECOLGB6oAP; captcha_session_v2="2|1:0|10:1639289450|18:captcha_session_v2|88:NHQ4bzJLdXpMdzVtL1ovdThaeVdEUDJ5KzRkQ2Q2WEhOY053WC92WUIvVWw1OWJrb1o0ZWQ0V0xmcll2NWxTUQ==|a08973aa579c5c9ac6d77f5bb3fc28ef5a4de8f03f868d73b604ff15f15b8e55"; z_c0="2|1:0|10:1639289469|4:z_c0|92:Mi4xanVOREJRQUFBQUFBb0pCLXhsWXJGQ2NBQUFDRUFsVk5mQl9kWVFBMGluTU5sNUNiYk16YnZ4WEZ4T0xmOXRxUENR|411009678cff040369198b2969b3f251da349904ae0b817e73ebbe2733b2ce0c"; NOT_UNREGISTER_WAITING=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1639380347,1639381436,1639442983,1639443686; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1639445792|1639443189; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1639445794',
            'User-Agent': headers['User-Agent'],
        }, proxies=proxies)
        contents = BeautifulSoup(post_response.text, 'html.parser').find_all(
            'div', attrs={'class': 'Post-RichTextContainer'})[0]
        _e_list = []
        for e in contents.find_all(['p', 'figure']):
            if e.attrs.get('data-pid'):  # p字段
                if e.text == "":
                    continue
                else:  # 是文本
                    _e_list.append(f"- {e.text}")
            elif e.attrs.get('data-size'):  # figure字段
                img_url = e.next.next.attrs['data-original']
                _e_list.append(f"![img]({img_url})")
        Result[f"{name} {post_time}"] = "\n".join(_e_list)
        break

print('全部提取完成，正在保存文件')
with open(f"{ctime.tm_mon}-{ctime.tm_mday}.md", 'w', encoding='utf-8') as fp:
    for name, content in Result.items():
        fp.writelines(f"### {name} ")
        fp.writelines(content + '\n')
        fp.writelines('\n' * 3)


_data = open(f"{ctime.tm_mon}-{ctime.tm_mday}.txt",
             'r', encoding='utf-8').readlines()
#BEGIN
push_url = 'http://www.pushplus.plus/send/e52fff7187b1400e870233aee67651d4'
#END
r_myself = requests.post(
    url=push_url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps({
        'title': f"{ctime.tm_mon}-{ctime.tm_mday}日tzrb",
        'content': "".join(_data),
        'topic': 'jijin',
        'template': 'markdown',
    }).encode(encoding='utf-8')
)
if r_myself:
    print('推送消息成功.')

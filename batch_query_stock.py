"""
批量查询股票代码
"""
import asyncio
import looter as lt
import re
from operator import itemgetter

stockListStr = '1宇通重工。2中旗新材。3河化股份。4深圳华强。5创维数字'

stockList = [re.search(r"\D+", item).group(0) for item in stockListStr.split('。')]
domain = 'https://www.baidu.com/'
total = []
# https://github.com/monperrus/crawler-user-agents/blob/master/crawler-user-agents.json
headers = {
    'Host':
    'index.baidu.com',
    'Connection':
    'keep-alive',
    'X-Requested-With':
    'XMLHttpRequest',
    'User-Agent':
    'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Cookie':
    'BIDUPSID=49DBDD154335E67AA2154B2E4EEDFFBA; PSTM=1702695641; BAIDUID=49DBDD154335E67ABAC7E6624DD8A3D9:FG=1; BD_UPN=12314753; BDUSS=Yya2w5eDNLc0pTWmZsMS1yQmhDV3h1QmhBelpEM1NLeXBWNlJ0ZWw2blREOVpsSVFBQUFBJCQAAAAAAAAAAAEAAABBGFGnsOvU2MH39fwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANOCrmXTgq5lal; BDUSS_BFESS=Yya2w5eDNLc0pTWmZsMS1yQmhDV3h1QmhBelpEM1NLeXBWNlJ0ZWw2blREOVpsSVFBQUFBJCQAAAAAAAAAAAEAAABBGFGnsOvU2MH39fwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANOCrmXTgq5lal; MCITY=-224%3A; newlogin=1; H_WISE_SIDS=60568_60574_60598_60623_60628; H_WISE_SIDS_BFESS=60568_60574_60598_60623_60628; COOKIE_SESSION=96215_0_9_9_4_16_1_0_9_9_1_0_647113_0_0_0_1722864176_0_1723604809%7C9%230_0_1724217611%7C1%7C1; BAIDUID_BFESS=49DBDD154335E67ABAC7E6624DD8A3D9:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDU_WISE_UID=wapp_1724395626680_303; ZFY=h:BC5HA2ZffxZgVt38JhIfkUKqGJTzSMHOlGU9ohux2E:C; RT="z=1&dm=baidu.com&si=7c03b9d3-a425-406b-9843-a5a229b79299&ss=m06r6pic&sl=c&tt=jgr&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=6ck2&ul=6dz0&hd=6e06"; BA_HECTOR=0k002l0k0lakal8l85002h8h9q3msb1jcijb41v; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=60598_60607_60623_60663_60677; delPer=0; BD_CK_SAM=1; PSINO=5; H_PS_645EC=e44bZwHO%2FZoXRsEwiiegDJZtgg3p53n9O4x9WpkODQnPw6XMuqIMlR8iBRAhLL22NSz6; BDSVRTM=457; ispeed_lsm=0'
}

async def crawl(url, keyword, i):
    tree = await lt.async_fetch(url, headers=headers)
    item = tree.css(".cosc-title span.cosc-title-slot::text").re_first(r"\[\S+\]A股实时行情")
    if item:
        item = item.replace("A股实时行情", "")
    else:
        item = "没搜到"
    data = {}
    data["id"] = i + 1
    data["keyword"] = keyword
    data["result"] = item
    total.append(data)


if __name__ == '__main__':
    tasklist = [f'{domain}s?wd={n}' for n in stockList]
    loop = asyncio.get_event_loop()
    # result = [crawl(task) for task in tasklist]
    result = [loop.create_task(crawl(task, stockList[i], i)) for (i, task) in enumerate(tasklist)]
    loop.run_until_complete(asyncio.wait(result))
    total = sorted(total, key=itemgetter('id'))
    total = [f"{item['id']}.{item['keyword']} {item['result']}" for item in total]
    total = "\n".join(total)
    print(total)

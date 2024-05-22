"""
批量查询股票代码
"""
import asyncio
import looter as lt
import re
from operator import itemgetter

stockListStr = '1中远海能，2创业黑马，3锦鸡股份，4弘业电子，5旋极信息，6聚飞光电，7华鲲振宇，8华胜天成，9江洲智能，10完美世界，11智度股份，12科兰软件'

stockList = [re.search(r"\D+", item).group(0) for item in stockListStr.split('，')]
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
    'BIDUPSID=4750090B3AD513D0145CE6E0B4C5435F; PSTM=1684283781; BDUSS=G1kZG0xZFRuWE0wdlNpbG5Pb2JxQ2c2Y003eVZZTnE2ejFjTlFRSVZNc2d-NHRrSVFBQUFBJCQAAAAAAAAAAAEAAABBGFGnsOvU2MH39fwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACByZGQgcmRke; BDUSS_BFESS=G1kZG0xZFRuWE0wdlNpbG5Pb2JxQ2c2Y003eVZZTnE2ejFjTlFRSVZNc2d-NHRrSVFBQUFBJCQAAAAAAAAAAAEAAABBGFGnsOvU2MH39fwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACByZGQgcmRke; H_WISE_SIDS=219946_234020_131861_216854_213348_214805_219942_213034_230180_204912_110085_236308_243879_244476_244717_245412_245599_248174_247147_250889_252640_249893_240590_253426_256083_255661_256739_251973_254317_257080_254075_257289_257823_257586_255230_258244_257994_258373_258371_258724_258728_258938_258982_258958_258698_230288_259048_257016_259067_107316_252256_259191_259193_256222_259288_256999_259558_259652_259704_258773_259753_234207_234295_259080_259642_260038_254300_257302_259240_260290_256230_260358_259728_260364_260227_259186_253022_255212_260060_258081_260335_251786_260804_259408_259422_259584_260721_259032_261055_259308_261028_261117_261374_253900_261519_261575_260465_261715_261459_261863_261861_261980_261996_262050_262052_261275_262063_255910_262184_260441_8000073_8000123_8000141_8000143_8000156_8000163_8000165_8000168_8000177_8000180_8000187; H_WISE_SIDS_BFESS=219946_234020_131861_216854_213348_214805_219942_213034_230180_204912_110085_236308_243879_244476_244717_245412_245599_248174_247147_250889_252640_249893_240590_253426_256083_255661_256739_251973_254317_257080_254075_257289_257823_257586_255230_258244_257994_258373_258371_258724_258728_258938_258982_258958_258698_230288_259048_257016_259067_107316_252256_259191_259193_256222_259288_256999_259558_259652_259704_258773_259753_234207_234295_259080_259642_260038_254300_257302_259240_260290_256230_260358_259728_260364_260227_259186_253022_255212_260060_258081_260335_251786_260804_259408_259422_259584_260721_259032_261055_259308_261028_261117_261374_253900_261519_261575_260465_261715_261459_261863_261861_261980_261996_262050_262052_261275_262063_255910_262184_260441_8000073_8000123_8000141_8000143_8000156_8000163_8000165_8000168_8000177_8000180_8000187; BD_UPN=12314753; H_PS_PSSID=39671_39664_39676_39713_39766_39675_39780_39790_39704_39681_39679_39818; BAIDUID=60BBE36E280C829D372D9DD3C77AB106:FG=1; BAIDUID_BFESS=60BBE36E280C829D372D9DD3C77AB106:FG=1; B64_BOT=1; BA_HECTOR=0104258h8ga5al25010la52n1im3nji1q; ZFY=UjotX6lABh1ClHpXm97anbYqzEHv1UiKYyJ0M8uQFlg:C; delPer=0; BD_CK_SAM=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; baikeVisitId=8b6e071b-56f6-423a-a0a2-0edca089bab3; ab_sr=1.0.1_ZTgxNGRlYTJmYzgyNTFjODU3OWFiOGJjMDUzMzk3MWVlNzA5NTg5YzYyNTliOWY0NWY4NmE1MzgyZThlNDg5MDZiNjBjYWQ2MDZhMTQ1MTUwMWM3YmRjMDU1ZDlmYzIxOTE0NzFjZjZmNjdhODY3NjIxM2Y1YjMwZDkxODBmNzUwMDk3ZGJjM2YyOGY1YTllNGU2Mjk5YmM0MGFlN2RiZA==; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; H_PS_645EC=eb44QYQSZMeHQAIr96Yw4EhYOcYq1ZsEnWt2R0T%2BOr%2B85REI6STzEXbF96d%2BMP3LulTV; BDSVRTM=333; COOKIE_SESSION=1516_0_9_8_5_14_1_0_9_8_2_1_962535_0_7_0_1700911233_0_1700911226%7C9%230_0_1700914596%7C1%7C1'
}

async def crawl(url, keyword, i):
    tree = await lt.async_fetch(url, headers=headers)
    item = tree.css(".c-title a::text").re_first(r"\[\S+\]A股实时行情")
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

import requests
from Picture import Picture

import re



def getpage(page=13,tag='ブルーアーカイブ 10000user'):
    headers = {
        'authority': 'www.pixiv.net',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
        'accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50',
        'x-user-id': '32972594',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'first_visit_datetime_pc=2020-07-31+23%3A23%3A19; p_ab_id=2; p_ab_id_2=4; p_ab_d_id=1689055057; yuid_b=IyeFl3E; __utma=235335808.670337424.1612613231.1612613231.1612613231.1; __utmv=235335808.|2=login%20ever=no=1^9=p_ab_id=2=1^10=p_ab_id_2=4=1^11=lang=zh=1; _ga=GA1.2.670337424.1612613231; a_type=0; b_type=0; ki_r=; login_ever=yes; ki_s=214027%3A0.0.0.0.0%3B214908%3A0.0.0.0.2%3B214994%3A0.0.0.0.2%3B215190%3A0.0.0.0.2%3B215821%3A0.0.0.0.2; ki_t=1614773911903%3B1621141037204%3B1621141052908%3B8%3B91; privacy_policy_notification=0; privacy_policy_agreement=3; _fbp=fb.1.1642574492056.46983175; PHPSESSID=32972594_I9ILCuyB59OtZ9MSgu1LTRzEdIU0ZbSG; device_token=ec67e1fcb3a8db3000802baccb5b7bd1; c_type=22; p_b_type=1; _gcl_au=1.1.1504472295.1644825735; user_language=zh; _gid=GA1.2.416994660.1644828903; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:39; __cf_bm=8uS.U93AwZCD65aTTlvL6nf.aQzXeLqqfbE5ziTUTfw-1644837254-0-AfL/M7kGoGoHi7fBL9EeQnHs6n/EHPVS/+K4jSpFv8yIYHTrsdezMc8met9fHlv49mwIwGQ+yobtT0iEWIVMNmtKLvrFxIEkOHLC8tA5Fx7+; tag_view_ranking=zIv0cf5VVk~Ce-EdaHA-3~m3EJRa33xU~O0WKFZuVbs~4QveACRzn3~XpYOJt3r5W~RTJMXD26Ak~0xsDLqCEW6~XRDAPK8u1R~CrFcrMFJzz~uusOs0ipBx~GxEzX1Shma~Lt-oEicbBr~mt8DCj4YUo~jhuUT0OJva~nQRrj5c6w_~AVEc3LeUs5~05XvkINl3k~sKs0aPaW87~qkC-JF_MXY~yAS_jNMXYB~BSkdEJ73Ii~2pZ4K1syEF~emE8W9nsA-~sOBG5_rfE2~WQMRPz3l59~WdKNu4p5bE~aY9er0y-Jk~jH0uD88V6F~azESOjmQSV~ETjPkL0e6r~Q959js6mBM~LJo91uBPz4~pzzjRSV6ZO~tIqkVZurKP~zXUuIJGfCn~_pwIgrV8TB~_EOd7bsGyl~9ODMAZ0ebV~t2ErccCFR9~1LN8nwTqf_~OCvRKdT9WZ~Ie2c51_4Sp~5OXRF8yfCA~JS8xw3QO3J~5oPIfUbtd6~37dsYFfqRK~-IrOV3901X~xgA3yCXKWS~BEa426Zwwo~klhaD7RvNc~fzr98o2pGl~ziiAzr_h04~SIBtn3ZiUT~cFYMvUloX0~qtVr8SCFs5~A3wgamEIOQ~Jxg8TkZQdK~rAZbDO2PXT~Oa9b6mEc1T~MhieHQxNXo~Fq4K_8PGib~8XX2eqWqNX~A-gn05u21h~C9_ZtBtMWU~6RcLf9BQ-w~k3AcsamkCa~r1vRjXa1Om~2QTW_H5tVX~BU9SQkS-zU~1vzZ2WkV1C~j0QoKstmJz~3RFI-y8rjT~xjugMnaG8D~M1CHwyFSXN~9LC16ImleM~mHukPa9Swj~Ed_W9RQRe_~jHRM-Uqq9q~PN0n94PqNP~Owa1zsZ4xr~KEsY86vTGd~Pl6ic44EAB~Yw6zHqltKg~75zhzbk0bS~eVxus64GZU~rELYgW0qN3~qz6SsESFCr~qpeZSmEVVP~mqf4KYn6Dx~kez5fmgQrG~G5npvsVTMr~OEHogw1GmU~3cT9FM3R6t~zyKU3Q5L4C~XHzMG_8vr_~dqSObM91AS~qc3_0F0xbS~Ltq1hgLZe3~Bd2L9ZBE8q',
    }

    params = (
        ('order', 'date_d'),
        ('mode', 'all'),
        ('p', f'{page}'),
        ('s_mode', 's_tag'),
        ('type', 'all'),
        ('lang', 'zh'),
    )

    response = requests.get(f'https://www.pixiv.net/ajax/search/artworks/{tag}', headers=headers, params=params)
    resjson=response.json()['body']['illustManga']['data']
    picobjtlist=[]
    for orpic in resjson:
        # pattern = '/'.join(re.findall('img.(\d+).(\d+).(\d+).(\d+).(\d+).(\d+).(\d+)', orpic['url'])[0])
        picobj=Picture(orpic['id'],orpic['title'],orpic['pageCount'])
        picobjtlist.append(picobj)


    # for orurl in resjson:
    #     type=asyncio.run(typejudge(orurl['id']))
    #     pattern ='/'.join(re.findall('img.(\d+).(\d+).(\d+).(\d+).(\d+).(\d+).(\d+)',orurl['url'])[0])
    #     picdict={'url':pattern,'title':orurl['title'],'id':orurl['id'],'pageCount':orurl['pageCount'],'type':type}
    #     picdictlist.append(picdict)
    return picobjtlist,tag
if __name__ == '__main__':
    print(getpage())
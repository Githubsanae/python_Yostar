import asyncio
import time
import aiohttp
import re
import os
import requests
import glob
from getpage import getpage

async def getpic(session,picobj,tag):
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
        'referer': 'https://www.pixiv.net/artworks/96255419',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'first_visit_datetime_pc=2020-07-31+23%3A23%3A19; p_ab_id=2; p_ab_id_2=4; p_ab_d_id=1689055057; yuid_b=IyeFl3E; __utma=235335808.670337424.1612613231.1612613231.1612613231.1; __utmv=235335808.|2=login%20ever=no=1^9=p_ab_id=2=1^10=p_ab_id_2=4=1^11=lang=zh=1; _ga=GA1.2.670337424.1612613231; a_type=0; b_type=0; ki_r=; login_ever=yes; ki_s=214027%3A0.0.0.0.0%3B214908%3A0.0.0.0.2%3B214994%3A0.0.0.0.2%3B215190%3A0.0.0.0.2%3B215821%3A0.0.0.0.2; ki_t=1614773911903%3B1621141037204%3B1621141052908%3B8%3B91; privacy_policy_notification=0; privacy_policy_agreement=3; _fbp=fb.1.1642574492056.46983175; PHPSESSID=32972594_I9ILCuyB59OtZ9MSgu1LTRzEdIU0ZbSG; device_token=ec67e1fcb3a8db3000802baccb5b7bd1; c_type=22; p_b_type=1; _gcl_au=1.1.1504472295.1644825735; user_language=zh; _gid=GA1.2.416994660.1644828903; tag_view_ranking=zIv0cf5VVk~Ce-EdaHA-3~m3EJRa33xU~4QveACRzn3~RTJMXD26Ak~O0WKFZuVbs~0xsDLqCEW6~XpYOJt3r5W~Lt-oEicbBr~XRDAPK8u1R~CrFcrMFJzz~GxEzX1Shma~mt8DCj4YUo~uusOs0ipBx~yAS_jNMXYB~sOBG5_rfE2~WQMRPz3l59~jhuUT0OJva~LJo91uBPz4~pzzjRSV6ZO~tIqkVZurKP~zXUuIJGfCn~_pwIgrV8TB~qkC-JF_MXY~BSkdEJ73Ii~AVEc3LeUs5~sKs0aPaW87~J4CKtTRNKQ~2pZ4K1syEF~nQRrj5c6w_~fzr98o2pGl~aY9er0y-Jk~jH0uD88V6F~azESOjmQSV~05XvkINl3k~emE8W9nsA-~Q959js6mBM~_EOd7bsGyl~WdKNu4p5bE~9ODMAZ0ebV~t2ErccCFR9~1LN8nwTqf_~OCvRKdT9WZ~Ie2c51_4Sp~5oPIfUbtd6~37dsYFfqRK~-IrOV3901X~BEa426Zwwo~q303ip6Ui5~-9rgXgT7C4~MlNfacUAf8~D6TnwR9Jia~0APtr_pGV6~jfnUZgnpFl~ziiAzr_h04~SIBtn3ZiUT~cFYMvUloX0~qtVr8SCFs5~A3wgamEIOQ~Jxg8TkZQdK~rAZbDO2PXT~Oa9b6mEc1T~5OXRF8yfCA~JS8xw3QO3J~xgA3yCXKWS~ETjPkL0e6r~8XX2eqWqNX~seCRZ2Z69P~GAjJy9iizy~QwHd7UP4v7~r03_OODiJd~C9_ZtBtMWU~6RcLf9BQ-w~k3AcsamkCa~r1vRjXa1Om~2QTW_H5tVX~BU9SQkS-zU~1vzZ2WkV1C~j0QoKstmJz~3RFI-y8rjT~xjugMnaG8D~M1CHwyFSXN~9LC16ImleM~mHukPa9Swj~Ed_W9RQRe_~jHRM-Uqq9q~PN0n94PqNP~Owa1zsZ4xr~KEsY86vTGd~Pl6ic44EAB~Yw6zHqltKg~75zhzbk0bS~eVxus64GZU~rELYgW0qN3~qz6SsESFCr~qpeZSmEVVP~mqf4KYn6Dx~kez5fmgQrG~G5npvsVTMr~OEHogw1GmU; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:50; __cf_bm=I5eZuGfhwgkO.OyDoOm5KC8jf9vv7_z48aCv7vFOO.E-1644845700-0-ATQzhaFndobI21xaXNfmvDWJdAS0pkr9YdUzzh7DlRVxRkY95a4V+aCbChS2Btw9y3X3gXaRy9n9wxmh/vx2FrkUr/m9C1kVZMK6qxglTPvc',
    }
    #获取pic类
    id= picobj.id
    title= picobj.title
    #文件名判断
    if re.search('[\\\ \/ \* \? \" \: \< \> \|]', title) != None:
        title = re.sub('[\\\ \/ \* \? \" \: \< \> \|]', '', title)
    #文件夹名判断
    if re.search('[\\\ \/ \* \? \" \: \< \> \|]', tag) != None:
        tag = re.sub('[\\\ \/ \* \? \" \: \< \> \|]', '', tag)
    if not os.path.exists('img\\' + tag):
        os.mkdir('img\\' + tag)
    pageCount= picobj.pageCount
    #type判断
    picurl=f'https://www.pixiv.net/artworks/{id}'
    async with session.get(picurl,headers=headers) as typejudge:
        jtext = await typejudge.text()
        result = re.findall(r'"original":"(.+?)"', jtext)[-1]
        if '.jpg' in result:
            type = 'jpg'
        if '.png' in result:
            type = 'png'
        #写入类型
        # 获取图片
        #判断图片是否分P

        if pageCount == 1:
            fileName = f'{title}_{id}_P{pageCount-1}.{type}'
            file = f'{tag}\\'
            judgepath = 'img\\' + file + fileName
            if not os.path.exists(judgepath):
                async with session.get(result,headers=headers) as picture:
                    if picture.status != 200:
                        print('连结错误')
                    content = await picture.read()
                    with open(judgepath, mode='wb') as f:
                        f.write(content)
                        print(f'Download:{title}')
        else:
            for i in range(pageCount):
                fileName = f'{title}_{id}_P{i}.{type}'
                file = f'{tag}\\'
                judgepath = 'img\\' + file + fileName
                purl=re.sub('_p0',f'_p{i}',result)
                if not os.path.exists(judgepath):
                    async with session.get(purl,headers=headers) as picture:
                        if picture.status != 200:
                            print('连结错误')
                    # picture = requests.get(purl, headers=headers)
                    # content = picture.content
                        content = await picture.read()
                        with open(judgepath, mode='wb') as f:
                            f.write(content)
                            print(f'Download:{title}')
async def main(page,tag):
    async with aiohttp.TCPConnector(limit=5) as conn:
        async with aiohttp.ClientSession(connector=conn) as session:
            list,tag=getpage(page,tag)
            if list != []:
                print('列表已经到手啦')
                tasks = [asyncio.create_task(getpic(session,picobj,tag))for picobj in list]
                await asyncio.wait(tasks)
            else:
                return 1

if __name__ == '__main__':
    tag=input('请输入标签名:')
    page=1
    while True:
        print(f'正在下载第{page}页')
        str=asyncio.run(main(page,tag))
        if str==1:
            print('已经执行完毕咯')
            break
        print(f'第{page}页下载完成')
        page +=1
        time.sleep(1)

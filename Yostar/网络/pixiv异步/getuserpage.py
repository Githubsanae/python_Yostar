
from Picture import Picture
import requests

def getuserpage(uid):
    headers = {
        'authority': 'www.pixiv.net',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
        'accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        'x-user-id': '32972594',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pixiv.net/users/453788/artworks',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'first_visit_datetime_pc=2020-07-31+23%3A23%3A19; p_ab_id=2; p_ab_id_2=4; p_ab_d_id=1689055057; yuid_b=IyeFl3E; __utma=235335808.670337424.1612613231.1612613231.1612613231.1; __utmv=235335808.|2=login%20ever=no=1^9=p_ab_id=2=1^10=p_ab_id_2=4=1^11=lang=zh=1; _ga=GA1.2.670337424.1612613231; a_type=0; b_type=0; ki_r=; login_ever=yes; ki_s=214027%3A0.0.0.0.0%3B214908%3A0.0.0.0.2%3B214994%3A0.0.0.0.2%3B215190%3A0.0.0.0.2%3B215821%3A0.0.0.0.2; ki_t=1614773911903%3B1621141037204%3B1621141052908%3B8%3B91; privacy_policy_notification=0; privacy_policy_agreement=3; _fbp=fb.1.1642574492056.46983175; PHPSESSID=32972594_I9ILCuyB59OtZ9MSgu1LTRzEdIU0ZbSG; c_type=22; _gcl_au=1.1.1504472295.1644825735; p_b_type=1; trdipcktrffcext=1; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:72; _gid=GA1.2.47044577.1645702373; tag_view_ranking=zIv0cf5VVk~Ce-EdaHA-3~4QveACRzn3~m3EJRa33xU~Lt-oEicbBr~RTJMXD26Ak~0xsDLqCEW6~XRDAPK8u1R~XpYOJt3r5W~CrFcrMFJzz~GxEzX1Shma~fzr98o2pGl~mt8DCj4YUo~BSkdEJ73Ii~uusOs0ipBx~seCRZ2Z69P~J4CKtTRNKQ~jhuUT0OJva~5oPIfUbtd6~yAS_jNMXYB~pzzjRSV6ZO~qkC-JF_MXY~sOBG5_rfE2~WQMRPz3l59~2pZ4K1syEF~LJo91uBPz4~tIqkVZurKP~zXUuIJGfCn~_pwIgrV8TB~sKs0aPaW87~jH0uD88V6F~RcahSSzeRf~GAjJy9iizy~QwHd7UP4v7~r03_OODiJd~AVEc3LeUs5~t2ErccCFR9~9ODMAZ0ebV~X_1kwTzaXt~aY9er0y-Jk~05XvkINl3k~6RcLf9BQ-w~tgP8r-gOe_~D0nMcn6oGk~75zhzbk0bS~SIBtn3ZiUT~_EOd7bsGyl~1LN8nwTqf_~OCvRKdT9WZ~Ie2c51_4Sp~azESOjmQSV~-IrOV3901X~BEa426Zwwo~KOnmT1ndWG~q303ip6Ui5~-9rgXgT7C4~MlNfacUAf8~D6TnwR9Jia~0APtr_pGV6~jfnUZgnpFl~ziiAzr_h04~WdKNu4p5bE~cFYMvUloX0~qtVr8SCFs5~A3wgamEIOQ~O0WKFZuVbs~JS8xw3QO3J~xgA3yCXKWS~emE8W9nsA-~Q959js6mBM~wKl4cqK7Gl~4gzX-RNalt~MA6EUZYaNt~ZMdJr3joTD~1tmjpDQFOy~QL2G1t5h_V~edF4CoWy9T~q3eUobDMJW~n39RQWfHku~_IharlAfPe~QW_eEuYnK9~aKhT3n4RHZ~C9_ZtBtMWU~k3AcsamkCa~r1vRjXa1Om~2QTW_H5tVX~BU9SQkS-zU~1vzZ2WkV1C~j0QoKstmJz~3RFI-y8rjT~xjugMnaG8D~M1CHwyFSXN~9LC16ImleM~mHukPa9Swj~Ed_W9RQRe_~jHRM-Uqq9q~PN0n94PqNP~Owa1zsZ4xr~KEsY86vTGd~Pl6ic44EAB; __cf_bm=bu10GhQSQjWP7cMNJ0AMdeX6MGBmne_8JqIM_NGuMD4-1645702523-0-AVS8z3SDOn1yV1+w/8yTIJ/kBe7u+63bD0GegfiFbyuQ7MF1pKOx/U0236bOpIBny7rbVCh7XRYkwHx8c1AqVOQlZUbD6efQbz4Bgh2k9+55hLg4xhA0O2Yo68xfNfod4T+JPTs7NQw3Nwe1bch1XaAI+aVyQTClXAlLW2/PFWJwPslCnKncUUDITLejyAIk2Q==',
    }
    params = (
        ('lang', 'zh'),
    )
    response = requests.get(f'https://www.pixiv.net/ajax/user/{uid}/profile/all', headers=headers,params=params)
    tag = response.json()['body']['pickup'][0]['userName']
    rejson=response.json()['body']['illusts']

    picidlist = []
    for key in rejson:
        picidlist.append(key)
    return picidlist,tag
if __name__ == '__main__':
    a,tag=getuserpage(453788)
    print(a,tag)
import requests
import json


def get_bky():
    r = requests.get('https://www.cnblogs.com/yoyoketang')
    print(r.text)


def get_bky_02():
    data = {'Keywords': 'yoyoketang'}

    r = requests.get('http://zzk.cnblogs.com/s/blogpost', data=data)
    print(r.status_code)
    print(r.text)


def post_boky_01():
    header = {
        "Host": "recomm.cnblogs.com",
        "Connection": "keep-alive",
        "Content-Length": "72",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "https://www.cnblogs.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    data = {"itemId":6828424,"itemTitle":"python接口自动化2-发送post请求"}
    r = requests.post('https://recomm.cnblogs.com/api/v1/recomm/blogpost/reco', json=data, headers=header)
    result = json.loads(r.content.decode('utf-8'))
    print(result)

def session_bky():

    # 先打开登录首页，获取部分cookie
    url = "https://passport.cnblogs.com/user/signin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
    }

    s = requests.session()
    r = s.get(url, headers=headers, verify=False)
    print(s.cookies)

    # 添加登录需要的两个cookie
    c = requests.cookies.RequestsCookieJar()

    c.set('.CNBlogsCookie', '3D3E29C92F61753D40DDF9FC6511F8075E05EBC35F5203F5D224CC3647B9E2350209375F0FA4C2763C026DF29D2711AEF49DC52E86255BA22A06DA2CB1FE321E0A21254FFA03D9FFB054367EADD6847676AF3350')  # 填上面抓包内容
    c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8KlpyPucjmhMuZTmH8oiYTMWn5tKfcGa5O6DchoDTSx4KJY34CoY2NyFY0yejS6ZD36r1QjKhJTuFXyBra9vI4ASG9AkF1ipb681iCPZq-K4i69jf126qAiMBGa3dRGuPypV0B2fXJh2O6vOQx8hlQeDJMO-qVjpUPBGfwp2XiTWfLekpG_5soQ-LoIB31QkN5CrB4LJZZTt5gNZ_jbpU9axTZOz3uIDsUZn9qQz6ZRFztAG2NT3k7S9Vyg1K1jnNFNO5tADL-M2m0_vY4LVUeBdG7yKeVVKCMRTePCSVOvsvONoTQAhqVcqN98wPdJGrg')  # 填上面抓包内容
    c.set('AlwaysCreateItemsAsActive', "True")
    c.set('AdminCookieAlwaysExpandAdvanced', "True")
    s.cookies.update(c)
    print(s.cookies)

    # 登录成功后保存编辑内容
    r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)

    # 保存草稿箱
    url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    body = {"__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR": "FE27D343",
            "Editor$Edit$txbTitle": "这是3111",
            "Editor$Edit$EditorBody": "<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
            "Editor$Edit$Advanced$ckbPublished": "on",
            "Editor$Edit$Advanced$chkDisplayHomePage": "on",
            "Editor$Edit$Advanced$chkComments": "on",
            "Editor$Edit$Advanced$chkMainSyndication": "on",
            "Editor$Edit$Advanced$txbEntryName": "",
            "Editor$Edit$Advanced$txbExcerpt": "",
            "Editor$Edit$Advanced$tbEnryPassword": "",
            "Editor$Edit$lkbDraft": "存为草稿",
            }
    r2 = s.post(url2, data=body, verify=False)
    print(r.content)





if __name__ == '__main__':
    post_boky_01()
    # session_bky()
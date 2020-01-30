from urllib import request, parse


def jh_crawl():
    appkey = "2a10c12685246be59e3610b674e0e51d"

    url = "http://v.juhe.cn/weather/index"

    parameter = {
        "cityname": "湛江",
        "key": "2a10c12685246be59e3610b674e0e51d"
    }

    data = parse.urlencode(parameter)
    full_url = url + "?" + data
    # print(full_url)
    response = request.urlopen(full_url)
    # print(response.getheader("content-type"))
    # print(response.read().decode("utf-8"))


def baidu_crawl():
    baidu_url = "https://www.baidu.com"
    baidu_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
        # "Accept-Language": "zh-cn",
        # "Accept-Encoding": "br, gzip, deflate",
        "Cookie": "H_PS_PSSID=1446_21122_26350; ORIGIN=0; bdime=0; sug=0; sugstore=0; BD_HOME=1; BD_UPN=143254; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=6; delPer=0; BD_CK_SAM=1; H_PS_645EC=7773QThKMFUHPeLEz70YTI2CROeT0r%2Fz9Sp3FuaJ4Eo7uP8mIXKVmhA9MnMVSfA3l1HC; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; BDSFRCVID=hFAOJeC62xeTkw7uaz62Um_4ICfwUDJTH6aVokWBHg5F0D0eGIfmEG0Pof8g0KAbN-JkogKK3gOTHlkF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJke_C0-JCK3jtcYMbo_q4tehHR30fo9WDTm_Doy5xbOfI3G-JC-DlLDBNOA3-5fQmnZ-pPKKxQojU3ty-thQ68vDMoxB45L3mkjbn7Dfn02OpjPXCckMP4syP4eKMRnWIJWKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCcjqR8ZD6_2jjoP; BDUSS=VNTWZiS0J0Tml3elJXZn40eDl3SkJ2YTRQaGpFRElKT0NYS29SeVBabVZYU3BlSVFBQUFBJCQAAAAAAAAAAAEAAABsZsU0ucDf7bW9SwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJXQAl6V0AJeRm; MCITY=-%3A; BAIDUID=548461CCE708E92BCEF52A2BD6A9D32D:FG=1; BIDUPSID=548461CCE708E92BCEF52A2BD6A9D32D; PSTM=1514184878"
    }

    req = request.Request(url=baidu_url, headers=baidu_headers)
    resp = request.urlopen(req)
    print(resp.getcode())
    print(resp.getheader("content-type"))
    print(resp.read().decode("utf-8"))

    with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(resp.read().decode("utf-8"))


def qb_crawl():
    url = "http://113.106.98.52/system/pictures/12266/122667776/small/PIP3HC2P93N96N1V.webp"

    req = request.Request(url, headers={
        "User-Agent": "QiuBai/15 CFNetwork/974.2.1 Darwin/18.0.0",
        "Accept": "image/webp,image/*;q=0.8"
    })
    resp = request.urlopen(req)
    print(resp.getcode())


qb_crawl()

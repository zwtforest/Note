import requests

r = requests.get("https://qzone.qq.com/")
try:
    if r.status_code == 200:
        r.encoding = r.apparent_encoding
        if open("htmlText.txt",'w').write(r.text):
            print("downloading html successful")
        else:
            print("build new file error")
except:
    print("error")


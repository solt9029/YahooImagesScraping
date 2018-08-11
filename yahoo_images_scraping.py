# yahoo画像検索から200枚画像を取得するプログラム

from pyquery import PyQuery
import urllib.error
import urllib.request
import sys

keyword = sys.argv[1]

def download_image(url, dst_path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

img_index = 0

for i in range(10):
    pq = PyQuery(url='https://search.yahoo.co.jp/image/search?p=' + keyword + '&b=' + str(i * 20 + 1))
    for img in pq("div.gridmodule")("div.SeR")("p.tb")("a")("img"):
        print(img.get("src"))
        url = img.get("src")
        dst_path = "./data/" + str(img_index) + ".png"
        download_image(url, dst_path)
        img_index = img_index + 1

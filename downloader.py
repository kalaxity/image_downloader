import requests


# === 設定 ===

# URLリストのファイル名を指定
#   URLリストは改行区切りでURLを列挙したtxtファイルのことです
url_list_name = "url_list.txt"

# === 設定ここまで ===


with open(url_list_name) as f:
    urls = f.readlines()

for i, url in enumerate(urls):
    url = url.strip()
    imgdata = requests.get(url).content
    filename = "./image/" + str(i+1) + ".jpg"
    with open(filename, mode="wb") as f:
        f.write(imgdata)


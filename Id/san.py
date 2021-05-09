import json
import requests
import html_to_json
from bs4 import BeautifulSoup


class Bruteforce:
    def __init__(self, username="", api_key="", url=""):
        donmains = {"danbooru": "danbooru.donmai.us",
                    "safebooru": "safebooru.donmai.us",
                    "sankaku": "chan.sankakucomplex.com",
                    "gelbooru": "gelbooru.com",
                    "hentaicloud": "www.hentaicloud.com",
                    "devianart": "www.deviantart.com",
                    "zerochan": "www.zerochan.net",
                    "konachan": "konachan.com",
                    "e-shuushuu": "e-shuushuu.net",
                    "pinterest": "pinterest.com",
                    "yandere": "yande.re",
                    "rule34": "rule34.xxx",
                    "direct_link": ["s.sankakucomplex.com",
                                    "i.pinimg.com",
                                    "64.media.tumblr.com",
                                    "static.zerochan.net",
                                    "files.yande.re",
                                    "images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com",
                                    "img3.gelbooru.com",
                                    "wimg.rule34.xxx"]}
        download = {"danbooru": self.danbooru,
                    "safebooru": self.safebooru,
                    "sankaku": self.sankaku,
                    "gelbooru": self.gelbooru,
                    "hentaicloud": self.hentaicloud,
                    "devianart": self.devianart,
                    "zerochan": self.zerochan,
                    "konachan": self.konachan,
                    "e-shuushuu": self.e_shuushuu,
                    "pinterest": self.pinterest,
                    "yandere": self.yandere,
                    "rule34": self.rule34,
                    "direct_link": self.dir_link}
        exts = ["jpg", "png", "jpeg", "webp", "gif"]
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'}
        self.url = url
        self.exts = exts
        self.header = header
        self.api_key = api_key
        self.username = username
        self.download = download
        self.donmains = donmains


    def gelbooru(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        li = soup.find_all(attrs={"href": "javascript:;"})
        lispl = li[3].get("onclick").split("'")
        link = lispl[7]
        return link

    def hentaicloud(self, url):
        post_id = url.split("/")[4]
        link = f"https://www.hentaicloud.com/media/photos/{post_id}.jpg"
        return link

    def tumblr(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        img = soup.find_all("img")
        src_img = img[-1].get("srcset")
        split_src = [i.strip() for i in src_img.split(",")]
        split_size = split_src[-1].split(" ")
        link = split_size[0]
        return link

    def devianart(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        img = [i.get('src') for i in soup.find_all(attrs={"class": "_1izoQ"}) if i != None]
        return img[0]

    def zerochan(self, url):
        split_url = url.split("/")
        if split_url[3] == "full":
            full = url
        else:
            full = f"https://www.zerochan.net/full/{split_url[3]}"
        r = requests.get(full)
        soup = BeautifulSoup(r.content, "html.parser")
        div = soup.find_all(attrs={"id": "fullsize"})
        link = div[0].img.get("src")
        return link

    def sankaku(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        img = soup.find("a", attrs={"id": "highres"}).get("href")
        link = f"https:{img}"
        return link

    def e_shuushuu(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        img = soup.find("a", attrs={"class": "thumb_image"})
        link = f"https://e-shuushuu.net{img.get('href')}"
        return link

    def pinterest(self, url):
        r = requests.get(url).text
        img = r.split("image")
        print(img[0].split('"')[-3])

    def yandere(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        try:
            link = soup.find("a", attrs={"id": "png"}).get("href")
        except AttributeError:
            link = soup.find("a", attrs={"id": "highres"}).get("href")
        return link

    def danbooru(self, url, info=False):
        if len(self.api_key) > 0:
            base = f"{url}.json?login={self.username}&api_key={self.api_key}"
        elif isinstance(self.api_key, str):
            base = f"{url}.json"
        r = requests.get(base).content
        post_decode = r.decode("utf-8")
        post_info = json.loads(post_decode)
        try:
            post_info["success"]
            post_info = "Tu username o api_key es incorrecto"
        except KeyError:
            pass
        if info:
            post = post_info
        else:
            post = post_info["file_url"]
        return post

    def safebooru(self, url, info=False):
        if len(self.api_key) > 0:
            base = f"{url}.json?login={self.username}&api_key={self.api_key}"
        elif isinstance(self.api_key, str):
            base = f"{url}.json"
        r = requests.get(base).content
        post_decode = r.decode("utf-8")
        post_info = json.loads(post_decode)
        try:
            post_info["success"]
            post_info = "Tu username o api_key es incorrecto"
        except KeyError:
            pass
        if info:
            post = post_info
        else:
            post = post_info["file_url"]
        return post

    def konachan(self, url, info=False):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        json_ = html_to_json.convert(r.text)
        infodic = dict()
        infodic["id"] = url.split("/")[5]
        infodic["tags"] = json_["html"][0]["head"][0]["link"][2]["meta"][0]["meta"][0]["meta"][3]["_attributes"][
            "content"]
        infodic["tag_split"] = infodic["tags"].split(" ")
        try:
            prbl = json_["html"][0]["body"][0]["div"][6]["div"][0]["div"][2]["a"]
            listparent = []
            for pr in prbl[1:]:
                listparent.append(pr["_value"])
            infodic["parent_id"] = listparent
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            url = soup.find_all(attrs={"class": "original-file-unchanged"})[0].get("href")
        except:
            url = soup.find_all(attrs={"class": "original-file-changed"})[0].get("href")
        infodic["file_ext"] = url[-3:]
        infodic["file_url"] = url
        if info:
            post = infodic
        else:
            post = infodic["file_url"]
        return post

    def rule34(self, url):
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        stats = soup.find(attrs={"class": "link-list"})
        ahrf = [a.a.get("href") for a in stats.find_all("li")]
        for h in ahrf:
            try:
                ahrf.remove("#")
            except:
                break
        return ahrf[0]

    def site_recognize(self, url=""):
        key = ""
        if len(url) > 0:
            url = url
        else:
            url = self.url
        split_url = url.split("/")
        donmai = split_url[2]
        try:
            for ki, values in self.donmains.items():
                if donmai == values:
                    key = ki
                    break
                elif isinstance(values, list):
                    values.index(donmai)
                    key = ki
                    break
                elif donmai.split(".")[1] == "tumblr":
                    key = "tumblr"
                else:
                    pass
        except:
            key = False
            print("El sitio no se reconoce o no es soportado")
        return key

    def dir_link(self, url):
        image = url
        return image

    def download_image(self, url="", out="", force=False):
        if len(self.url) > 0:
            url = self.url
        else:
            url = url
        if force:
            valor = url
        elif not force:
            sr = self.site_recognize(url)
            down = self.download
            valor = down[sr](url)
        us = [link for link in valor.split("?")][0].split("/")[-1]
        try:
            vext = self.exts.index(us.split(".")[-1])
            force_jpg = False
        except:
            vext = 0
            force_jpg = True
            print("Se forzarzara la descarga en .jpg")
        if vext == 0:
            ext = "jpg"
        elif vext == 1:
            ext = "png"
        elif vext == 2:
            ext = "jpeg"
        elif vext == 3:
            ext = "webp"
        elif vext == 4:
            ext = "gif"

        if len(out) > 0:
            image = f"{out}.{ext}"
        elif force_jpg == True:
            image = f"{us}.{ext}"
        else:
            image = us
        with open(image, "wb") as img:
            img.write(requests.get(valor, headers=self.header).content)
        return image


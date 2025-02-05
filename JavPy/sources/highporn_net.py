from JavPy.sources.BaseSource import ISearchByCode
import requests
import bs4
from JavPy.functions.datastructure import AV


class HighPornNet(ISearchByCode):
    @classmethod
    def search_by_code(cls, code):
        url = "https://highporn.net/search/videos?search_query=" + code.lower()
        rsp = requests.get(url)
        if "No Videos Found." in rsp.text:
            return None
        bs = bs4.BeautifulSoup(rsp.text, "lxml")
        div = bs.select(".well-sm")[0]
        av = AV()
        av.code = code
        av.preview_img_url = div.find(name='img').attrs['src']
        if not av.preview_img_url.startswith("http"):
            av.preview_img_url = "http:" + av.preview_img_url
        av.video_url = div.a.attrs['href']
        return av

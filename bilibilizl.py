import importlib, sys

importlib.reload(sys)
from lxml import etree
import requests  # 导入requests包

if __name__ == '__main__':

    url = 'https://www.bilibili.com/read/cv4234425?from=category_0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    # li_list = tree.xpath('/html/body/div[2]/div[5]//text()')
    li_list = tree.xpath('//div[@class="article-holder"]//text()')
    #//div[@id="main"]
    # print(li_list)
    for li in li_list:
        print(li)

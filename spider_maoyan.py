import requests
import re
import io
import sys
from requests.exceptions import RequestException

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_page_one(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers)
        return response.text
    except RequestException as e:
        return e


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name.*?<a.*?>(.*?)</a>.*?star">(.*?)</p>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'actor': item[2].strip()
        }


def main():
    url = 'https://maoyan.com/board/4'
    html = get_page_one(url)
    result = parse_one_page(html)
    i = 0
    for item in result:
        print(item)
        i=i+1
        print(i)
if __name__ == '__main__':
    main()

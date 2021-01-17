import requests
import json
from urllib.parse import urlencode
from requests.exceptions import RequestException


def get_page_one():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36\
x-csrftoken: 3672930e587f199dfed3b6e747e1709c"}
    data = {
        "category": "gallery_photograthy",
        "max_behot_time": "1605927222",
        "utm_source": "toutiao",
        "_signature": "02B4Z6wo00f019Jc5IwAAIBDapqa0EtlsVvSWeAAAKs6zY2gmvCu0bUpRM8sx270VHDRA2EYdgTT-0b0VIVwXOEFx5JrfRJ.keX4NN4dO4UfrDxSlZjI6Ej6gV9YMEE3oYBLpeIdkk3oWZgV78"
    }
    url = 'https://www.toutiao.com/api/pc/feed/?' + urlencode(data)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        print('请求页面出错')
        return None


def parse_one_page(url):
    data = json.loads(url)
    print(data)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            if 'middle_image' in item.keys():
                yield {
                    'title': item.get('title'),
                    'middle_image': item.get('middle_image'),
                    'image_list': item.get('image_list')
                }


def main():
    response = get_page_one()
    for result in parse_one_page(response):
        print(result)


if __name__ == '__main__':
    main()

import requests
import re
import json


def request_from_web(url):
    try:
        headers = {
            'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return ""


def parse_result(html):

    # We will be using findAll and () grouping
    pattern = re.compile(r"<li>.*?list_num.*?(\d+).</div>.*?<img src=\"(.*?)\".*?class=\"name\".*?title=\"(.*?)\">.*?class=\"star\">.*?class=\"tuijian\">(.*?)</span>.*?class=\"publisher_info\">.*?target=\"_blank\">(.*?)</a>.*?class=\"biaosheng\">.*?<span>(.*?)</span></div>.*?<p><span class=\"price_n\">&yen;(.*?)</span>.*?</li>", re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }

def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page)
    html = request_from_web(url)
    items = parse_result(html)
    for item in items:
        print(item)

if __name__ == "__main__":
    main(1)
'''
range
image
title
recommend
author
times
price
'''


# request_from_web("http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1")

# try:
#     print("esfsf" + 2)
# except IOError:
#     print("hmm?" + 2)
# except:
#     print("hmm?>")

#Homework
# Look at previous code,
# Grab the html content from a website
# Print the html code
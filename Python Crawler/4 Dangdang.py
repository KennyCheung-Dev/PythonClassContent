import requests
import re
import json

def request_from_web(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.text)
            return response.text
    except requests.RequestException:
        return ""


def parse_result(html):
    # re.S will treat multiple lines as a whole and match patterns across lines. Without re.S, re can't match pattern on different lines. 
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield { # 'yield' is similar to 'return' except the current loop will not be stopped. Instead, the loop will go on and keep returning results. 
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def write_item_to_file(item):
    print('Writing data to file ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f: # 'a' is the mode adding new text to file. 'w' will overite file and not approriate here. 
        f.write(json.dumps(item, ensure_ascii=False) + '\n') # set to False to avoid text being processed under ascII --> output as-is.
        f.close()


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_from_web(url)
    items = parse_result(html) # only keep information we need.
    for item in items:
        write_item_to_file(item)


if __name__ == "__main__":
    # for i in range(1,26):
    #     main(i)
    main(1)

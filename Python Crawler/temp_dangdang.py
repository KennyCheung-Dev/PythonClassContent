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
            print(response.text)
            return response.text
    except requests.RequestException:
        return ""
request_from_web("http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1")

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
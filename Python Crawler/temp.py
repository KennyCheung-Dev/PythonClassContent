import urllib.request
import urllib.parse

data = {"q":"HelloWorld"}
data = urllib.parse.urlencode(data)
ourOwnMacintoshHeader = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
req = urllib.request.Request('https://www.google.com/search?' + data,
                             headers=ourOwnMacintoshHeader)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))


# data = {"q":"HelloWorld"}
# data = urllib.parse.urlencode(data)
# req = urllib.request.Request('https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html')
# with urllib.request.urlopen(req) as response:
#     print(response.read().decode('utf-8'))


# GET
# POSTimport urllib.request
# import urllib.parse
#
# data = {"q":"HelloWorld"}
# data = urllib.parse.urlencode(data)
# ourOwnMacintoshHeader = {
#     "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
# }
# req = urllib.request.Request('https://www.google.com/search?' + data,
#                              headers=ourOwnMacintoshHeader)
# with urllib.request.urlopen(req) as response:
#     print(response.read().decode('utf-8'))
#
#
# # data = {"q":"HelloWorld"}
# # data = urllib.parse.urlencode(data)
# # req = urllib.request.Request('https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html')
# # with urllib.request.urlopen(req) as response:
# #     print(response.read().decode('utf-8'))
#
#
# # GET
# # POST
#
#
# # My website: https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html
#
# # req = urllib.request.Request('https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html')
# # with urllib.request.urlopen(req) as response:
# #     the_page = response.read()
# #     print(the_page.decode('utf-8'))
#
#
# # data = {'q':'HelloWorld'}
# # data = urllib.parse.urlencode(data)
# # req = urllib.request.Request('https://www.google.com/search?' + data)
# # with urllib.request.urlopen(req) as response:
# #     the_page = response.read()
# #     print(the_page.decode('utf-8'))
#
#
# # Homework this week:
# # Get familiar with request types and their usage in https://reqres.in/
# # Try out some of the GET Request with our code here


# My website: https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html

# req = urllib.request.Request('https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html')
# with urllib.request.urlopen(req) as response:
#     the_page = response.read()
#     print(the_page.decode('utf-8'))


# data = {'q':'HelloWorld'}
# data = urllib.parse.urlencode(data)
# req = urllib.request.Request('https://www.google.com/search?' + data)
# with urllib.request.urlopen(req) as response:
#     the_page = response.read()
#     print(the_page.decode('utf-8'))


# Homework this week:
# Get familiar with request types and their usage in https://reqres.in/
# Try out some of the GET Request with our code here
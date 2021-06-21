import urllib.request
import urllib.parse

#Simple open page
# response = urllib.request.urlopen("http://google.com")
# print(response.read())

# Attempt with data
# data = {"q":"HelloWorld"}
# data = urllib.parse.urlencode(data).encode()
# req = urllib.request.Request('https://www.google.com/search', data=data)
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
#    print(the_page.decode('utf-8'))


# Success!
# header = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36"}
# data = {'q':'HelloWorld'}
# data = urllib.parse.urlencode(data)
# req = urllib.request.Request('https://www.google.com/search?' + data,
#                              headers=header,
#                              method="GET")
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
#    print(the_page.decode('utf-8'))


header = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36"}
data = {'email' : 'eve.holt@reqres.in',
        'password' : 'cityslica'}
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request('https://reqres.in/api/login',
                             headers=header,
                             data = data)
response = urllib.request.urlopen(req)
print(response.getcode())
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   print(the_page.decode('utf-8'))

import requests

def basics():
    r = requests.get(url='https://hsv.de')
    print('Statuscode: ' + str(r.status_code))
    print('Success: ' + str(r.ok))
    print('Headers: ' + str(r.headers))

def download():
    # downloads a image from the URL
    r1 = requests.get(url='https://images-eu.ssl-images-amazon.com/images/I/11YLlf69uLL.png')
    with open('picture.png', 'wb') as f1:
        f1.write(r1.content)
    print(r1.status_code)

    # downloads the html code from the URL
    r2 = requests.get(url='https://hsv.de')
    with open('htmlcode.txt', 'wb') as f2:
        f2.write(r2.text.encode())
    print(r2.status_code)

def get_request():
    payload = {'firstname': 'Til', 'lastname': 'Cordes'}
    r = requests.get(url='https://httpbin.org/get', params=payload)
    print(r.json())
    print('\n')
    print(r.text)

def post_request():
    payload = {'username': 'Til', 'password': 'Cordes'}
    r = requests.post(url='https://httpbin.org/post', data=payload)
    print(r.json())
    print('\n')
    print(r.text)

def timeouts(timeout):
    try:
        r = requests.get(url='https://httpbin.org/delay/' + str(timeout), timeout=5)
        print(r)
    except:
        print('Timeouterror: Page took to long to load!')

def proxy_request():
    proxy = {'http': '52.157.215.147:3128', 'https': '52.157.215.147:3128'}

    r = requests.get(url='https://httpbin.org/ip', proxies=proxy)
    print(r.content)
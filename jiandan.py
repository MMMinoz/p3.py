import urllib.request
import os
import base64
import random

def url_open(url):

    req=urllib.request.Request(req)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36')

    iplist = ['52.221.208.181:80']
    proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})

    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    response=urllib.request.urlopen(url)
    html=response.read()


    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]

  
def find_imgs(url):
    html=url_open(url).decode('utf-8')
    img_addrs=[]

    a=html.find('img src=')
    
    while a!=-1:
        b=html.find('.jpg',a,a+255)

        if b!=-1:
            img_addrs.append("http:"+html[a+9:b+4])
        else:
            b=a+9
    
        a=html.find('img src=',b)

    return img_addrs


def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]

        with open(filename,'wb') as f:
            img=url_open(each)
            f.write(img)


def download_mm(folder='mm',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'https://jandan.net/ooxx/'
    page_num=int(get_page(url))

    for i in range(pages):
        page_num-=1
        s_page = '20210119-' + str(page_num)
        base_page = base64.b64encode(s_page.encode('utf-8'))
        str_page = str(base_page, 'utf-8')
        page_url=url+str_page+"#comments"
        img_addrs=find_imgs(page_url)
        
        save_imgs(folder,img_addrs)
        

def download_mm(folder='mm', pages=10):
    os.mkdir(folder)
    os.chdir(folder)
 
    url = 'https://jandan.net/ooxx/'
    page_num = int(get_page(url))
 
    for i in range(pages):
        page_num -= 1
        str_page = '20201025-' + str(page_num)
        str_page = base64.b64encode(str_page.encode('utf-8'))
        str_page = str(str_page, 'utf-8')
        page_url = url + str_page + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__=='__main__':
    download_mm()

print(html)
sleep(2)
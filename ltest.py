import urllib.request
import os
import random
referer=['https://www.mzitu.com/223090','https://www.mzitu.com/19465','https://www.mzitu.com/205668']
def get_page(url):
    html=url_open(url).decode('utf-8')
    a=html.find('data-original=')+50
    b=html.find('.jpg',a)-4
    return html[a:b]
    
def url_open(url):
    
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    head['Referer'] = '{}'.format(random.choice (referer))
    req = urllib.request.Request(url,headers=head)
    response=urllib.request.urlopen(req)
    html = response.read()
    
    return html
def find_imgs(  page=''):
    html=url_open('https://www.mzitu.com/xinggan/'+page).decode('utf-8')
    img_addrs=[ ]
    a=html.find('data-original=')

    while a !=-1:
        b=html.find('.jpg',a)
        if b!=-1:
            img_addrs.append(html[a+15:b+4])
        else:
            b=a+15
        a=html.find('data-original=',b)
    return img_addrs
def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
      
        with open(filename,'wb+') as f:
            img=url_open(each)
            
            f.write(img)
            print('正在下载。。。')
    return filename
def download_mm(folder='heihei'):
    os.mkdir(folder)
    os.chdir(folder)
    
    img_addrs=find_imgs( )
    for i in img_addrs:
        print(i)  
    save_imgs(folder,img_addrs)
    for i in [2,3,4,5]:
        n=input('需要下载第'+str(i)+'页吗？ 我还顶的住（Y） 够了够了，顶不住了（N）')
        if n=='Y'or n=='y':
            img_addrs1=find_imgs( 'page/'+str(i)+'/')
            for i in img_addrs:
                print(i)  
            save_imgs(folder,img_addrs1)
        elif n=='N'or n=='n':
            break
        else:
            print('输入Y或N哦')
  


if __name__ == '__main__':
    download_mm()
    print('大功告成')

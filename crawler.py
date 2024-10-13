import requests
import urllib.request
import urllib.parse

if __name__ == '__main__':
    # 爬取搜狗首页
    # step1 指定URL
    url = 'https://www.cnipa.gov.cn/art/2020/11/23/art_97_155167.html'
    # step2 发起请求
    response = requests.get(url=url)    # get会返回响应对象
    # step3 响应数据 .text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # step4 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！！！')


    # 网页采集器
    '''url = 'https://www.sogou.com/web'
    # 处理url携带的参数： 封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定url发起请求，对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param)
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')
'''

    # 使用urllib获取百度首页源码
    '''import urllib.request

    # 1.定义url
    url = 'http://www.baidu.com'
    # 2.模拟浏览器向浏览器发送请求
    response = urllib.request.urlopen(url)  # 这是HTTPResponse类型
    # 3.获取响应中的页面的源码
    content = response.read().decode('utf-8')  # read方法返回的是字节形式的二进制数据， 需要将二进制转换为字符串（解码） decode（’编码格式‘）
    # 4.打印数据
    # print(content)
    # 返回状态码
    print(response.getcode())
    # 返回url地址
    print(response.geturl())
    # 获取状态信息
    print(response.getheaders())
'''

    # url下载
    '''import urllib.request

    # 下载网页
    # url_page = 'http://www.baidu.com/'
    #
    # urllib.request.urlretrieve(url_page, 'baidu.html')  # url代表下载的路径，filename代表的是文件的名字

    # 下载图片
    # url_img = 'https://img1.baidu.com/it/u=3693778510,2897036897&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=621'
    # urllib.request.urlretrieve(url_img, 'lisa.jpg')

    # 下载视频
    url_video = 'https://haokan.baidu.com/c45a9395-c4be-4d3e-b810-3b5fd44975ea'
    urllib.request.urlretrieve(url_video, 'pangmao.mp4')
'''

    # 请求对象的定制
    '''url1 = 'https://www.baidu.com'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    # 因为urlopen中不能存放字典，所以headers不能传递进去，需要定制对象
    # 请求对象定制
    request = urllib.request.Request(url=url1, headers=headers)

    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    print(content)'''

    # get请求的quote方法
    '''# 需求: 获取'https://www.baidu.com/s?wd=周杰伦' 的网页源码
    url = 'https://www.baidu.com/s?wd='

    # 将周杰伦转变为unicode编码的格式
    # 需要依赖于urllib.parse
    name = urllib.parse.quote('周杰伦')
    url = url + name

    # 请求对象的定制是为了解决反爬的第一个手段
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    # 请求对象定制
    request = urllib.request.Request(url=url, headers=headers)

    # 模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(request)

    # 获取响应的内容
    content = response.read().decode('utf8')

    # 打印数据
    print(content)
'''

    # get的urlencode方法
    '''# urlencode适用场景：含有多个参数的时候

    # https://www.baidu.com/s?wd=周杰伦&sex=男

    data = {
        'wd': '周杰伦',
        'sex': '男'
    }

    a = urllib.parse.urlencode(data)
    print(a)'''

    # # post请求百度翻译
    # url = 'https://fanyi.baidu.com/sug'
    #
    # # 准备请求数据,伪装
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    # }
    #
    # data = {
    #     'kw': 'spider'
    # }
    #
    # # post请求的data参数需要通过urlencode编码
    # data = urllib.parse.urlencode(data).encode('utf-8')
    #
    # # 请求对象定制
    # request = urllib.request.Request(url=url, headers=headers, data=data)
    #
    # # 模拟浏览器向服务器发送请求
    # response = urllib.request.urlopen(request)
    #
    # # 获取响应的内容
    # content = response.read().decode('utf8')
    #
    # # 打印数据
    # # print(type(content))
    #
    # # 注意：post请求方式的参数，必须是bytes类型，所以需要先编码；参数是放在请求对象的定制的方法中
    # # 而get请求方式的参数，可以直接放到url中，不需要编码
    #
    # # json数据解析
    # import json
    #
    # # 解析json数据
    # obj = json.loads(content)
    #
    # # 打印数据
    # print(obj)

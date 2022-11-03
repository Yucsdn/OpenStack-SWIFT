import os
import time
import requests
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.utils.encoding import escape_uri_path


def login(request):
    return render(request, 'index.html')


def get_token(request):
    username = request.POST['username']
    password = request.POST['password']
    data = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "domain": {
                            "name": "default"
                        },
                        "name": username,
                        "password": password
                    }
                }
            },
            "scope": {
                "project": {
                    "domain": {
                        "name": "default"
                    },
                    "name": username
                }
            }
        }
    }
    url = 'http://192.168.174.10:35357/v3/auth/tokens'
    result = requests.post(url, json=data)
    token = result.headers['X-Subject-Token']
    print('获取的token：', token)
    request.session['token'] = token
    return redirect('/app/home/')


def home(request):
    return render(request, 'home.html')


def size_get(num):
    if num < 1024:
        return str(num) + ' ' + 'B'
    elif 1024 <= num < 1024**2:
        x = round(num/1024, 1)
        return str(x) + ' ' + 'KB'
    else:
        x = round(num/(1024**2), 1)
        return str(x) + ' ' + 'MB'


def time_get(num):
    time_local = time.localtime(num)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return str(dt)


def see_file(request):
    token = request.session.get('token')
    can = 'Object'
    url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can
    headers = {'X-Auth-Token': token}
    param = {'format': 'json'}
    result = requests.get(url, headers=headers, params=param)
    print('查看文件状态码：', result.status_code)
    datas = result.json()
    print(datas)
    dat = []
    for d in datas:
        data = {}
        name = d['name']
        types = d['content_type']
        size = size_get(d['bytes'])
        last_time = d['last_modified']
        data["name"] = name
        data["type"] = types
        data["size"] = size
        data["last_time"] = last_time
        dat.append(data)
    request.session['can'] = can
    request.session['datas'] = datas
    return render(request, 'type.html', {'dat': dat})


def add_file(request):
    token = request.session.get('token')
    can = request.session.get('can')
    file = request.FILES.get('file')
    name = file.name
    s = name.split('.')
    if s[1] == 'png':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'image/png'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'jpeg':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'image/jpeg'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'jpg':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'image/jpeg'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'txt':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'text/plain'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'docx':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'doc':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'application/msword'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'rtf':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'application/rtf'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'pptx':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'xls':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'application/vnd.ms-excel'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'xlsx':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'pdf':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'application/pdf'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'mp3':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'audio/mpeg'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif s[1] == 'mp4':
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + name
        headers = {'X-Auth-Token': token, 'content_type': 'video/mp4'}
        data = open(r'D:\swift\upload\\' + name, 'rb')
        result = requests.put(url, headers=headers, data=data)
        print('添加文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    else:
        print("此文件未在可传输文件范围内！！")
        return redirect('/app/home/see_file/')


def delete_down(request):
    token = request.session.get('token')
    can = request.session.get('can')
    headers = {'X-Auth-Token': token}

    if 'delete' in request.POST:
        file = request.POST['file']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + file
        result = requests.delete(url, headers=headers)
        print('删除文件状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif 'down' in request.POST:
        file = request.POST['file']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + file
        result = requests.get(url, headers=headers)
        with open('D:\\swift\\download\\' + file, 'wb') as f:
            f.write(result.content)
        print('下载文件状态码：', result.status_code)
        fs = open('D:\\swift\\download\\' + file, 'rb')
        response = FileResponse(fs)
        response['content_type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(file))
        return response

    elif 'image_delete' in request.POST:
        image = request.POST['image']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + image
        result = requests.delete(url, headers=headers)
        print('删除图片状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif 'image_down' in request.POST:
        image = request.POST['image']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + image
        result = requests.get(url, headers=headers)
        with open('D:\\swift\\download\\' + image, 'wb') as f:
            f.write(result.content)
        print('下载图片状态码：', result.status_code)
        fs = open('D:\\swift\\download\\' + image, 'rb')
        response = FileResponse(fs)
        response['content_type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(image))
        return response

    elif 'txt_delete' in request.POST:
        txt = request.POST['txt']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + txt
        result = requests.delete(url, headers=headers)
        print('删除文档状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif 'txt_down' in request.POST:
        txt = request.POST['txt']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + txt
        result = requests.get(url, headers=headers)
        with open('D:\\swift\\download\\' + txt, 'wb') as f:
            f.write(result.content)
        print('下载文档状态码：', result.status_code)
        fs = open('D:\\swift\\download\\' + txt, 'rb')
        response = FileResponse(fs)
        response['content_type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(txt))
        return response

    elif 'video_delete' in request.POST:
        video = request.POST['video']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + video
        result = requests.delete(url, headers=headers)
        print('删除音频状态码：', result.status_code)
        return redirect('/app/home/see_file/')
    elif 'video_down' in request.POST:
        video = request.POST['video']
        url = "http://192.168.174.10:8080/v1/AUTH_71cd8dd762de42c683562083704567d4/" + can + '/' + video
        result = requests.get(url, headers=headers)
        with open('D:\\swift\\download\\' + video, 'wb') as f:
            f.write(result.content)
        print('下载音频状态码：', result.status_code)
        fs = open('D:\\swift\\download\\' + video, 'rb')
        response = FileResponse(fs)
        response['content_type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(video))
        return response


def image(request):
    datas = request.session.get('datas')
    image = []
    for d in datas:
        data = {}
        names = d['name']
        s = names.split('.')
        if s[1] == 'png' or s[1] == 'jpg' or s[1] == 'jpeg':
            name = d['name']
            types = d['content_type']
            size = size_get(d['bytes'])
            last_time = d['last_modified']
            data["name"] = name
            data["type"] = types
            data["size"] = size
            data["last_time"] = last_time
            image.append(data)
        else:
            pass
    return render(request, 'image.html', {'image': image})


def txt(request):
    datas = request.session.get('datas')
    txt = []
    for d in datas:
        data = {}
        names = d['name']
        s = names.split('.')
        if s[1] == 'txt' or s[1] == 'docx' or s[1] == 'rtf' or s[1] == 'doc' or s[1] == 'pdf' or s[1] == 'xls' or s[1] == 'ppt' or s[1] == 'pptx' or s[1] == 'xlsx':
            name = d['name']
            types = d['content_type']
            size = size_get(d['bytes'])
            last_time = d['last_modified']
            data["name"] = name
            data["type"] = types
            data["size"] = size
            data["last_time"] = last_time
            txt.append(data)
        else:
            pass
    return render(request, 'txt.html', {'txt': txt})


def video(request):
    datas = request.session.get('datas')
    video = []
    for d in datas:
        data = {}
        names = d['name']
        s = names.split('.')
        if s[1] == 'mp3' or s[1] == 'mp4' or s[1] == 'avi' or s[1] == 'rmvb' or s[1] == 'mov' or s[1] == 'flv':
            name = d['name']
            types = d['content_type']
            size = size_get(d['bytes'])
            last_time = d['last_modified']
            data["name"] = name
            data["type"] = types
            data["size"] = size
            data["last_time"] = last_time
            video.append(data)
        else:
            pass
    return render(request, 'video.html', {'video': video})


def download(request):
    path = "d:\\swift\\download\\"
    files = os.listdir(path)
    os.chdir(path)
    datas = []
    for file in files:
        data = {}
        f = file.split('.')
        times = os.path.getctime(path + file)
        timess = str(times)
        d = timess.split('.')
        x = int(d[0])
        sizes = os.path.getsize(path + file)
        name = file
        types = f[1]
        size = size_get(sizes)
        last_time = time_get(x)
        data["name"] = name
        data["last_time"] = last_time
        data["type"] = types
        data["size"] = size
        datas.append(data)
    return render(request, 'inventory.html', {'datas': datas})


def open_file_path(request):
    os.system("start explorer d:\\swift\\download\\")
    return redirect('/app/home/download/')


def sousuo(request):
    return render(request, 'sousuo.html')
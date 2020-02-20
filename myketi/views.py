'''
首先，不同单位（如洮南市气象局）的课题申报人通过这个系统提交课题申报书，申报人可以通过选项选择课题申报单位、课题分类、提交课题申报书，然后系统管理员根据课题分类直接将课题提交给课题审批人，课题审批人也分（预报、测报、农气、计算机、装备保障、其他）这几种，审批人预览课题后，通过选项选择给出批复意见，同意的直接录入数据库，并设一个修改意见框，不同意的直接删掉，结果返回申报人。
15:50:35
星空撤回了一条消息
15:51:04
星空撤回了一条消息
星空 15:52:04
第二注册过的任何人都可以通过这个系统分类查询或者输入单个字查询预览学习已经审批通过的课题，也可以下载学习
星空 15:53:16
第三 系统管理员可以对所有课题进行增删改查
我整理了一下，咱们这个建两个表就可以了，一个是用户表：包括，id，姓名等基本信息，{申报人，审批人，管理员}三种身份。第二个表是课题表，包括id，课题名称，课题内容，课题类型，申报人，审批人，审批状态和修改意见。
其他的包括审批时间等等也要加上
第二个表还要一个申报单位
'''

from django.shortcuts import render, redirect, HttpResponse
import json
from myketi.models import *
import os, datetime
from django.http import FileResponse
from django.utils.encoding import escape_uri_path
from django.db.models import Q


def regist(request):
    if request.method == 'POST':
        flag = request.POST.get('flag1', None)
        if (flag != "4"):
            # print("1")
            name = request.POST.get('name', None)
            if (name != ""):
                user = User.objects.filter(name=name)
                if len(user) != 0:
                    reg = {"flag": "1"}
                else:
                    reg = {"flag": "0"}
            else:
                reg = {"flag": "0"}
        else:
            name = request.POST.get('name', None)
            password0 = request.POST.get('password', None)
            password1 = request.POST.get('password1', None)
            type = request.POST.get('type', None)
            # print(type)
            if (name != ""):
                user = User.objects.filter(name=name)
                if (len(user) == 0) & (password0 == password1) & (password1 != ""):
                    # print("3")
                    User.objects.create(name=name, password=password0, shenfen=type)
                    reg = {"flag": "1"}
                else:
                    reg = {"flag": "0"}
            else:
                reg = {"flag": "0"}
        response = HttpResponse(json.dumps(reg))
        return response
    return render(request, "regist1.html")


def login(request):
    if request.method == 'POST':
        flag = request.POST.get('flag1', None)
        if (flag == "3"):
            # print("1")
            name = request.POST.get('name', None)
            if (name != ""):
                user = User.objects.filter(name=name).first()
                if len(user) == 0:
                    log = {"flag": "1"}
                else:
                    log = {"flag": "0"}
            else:
                log = {"flag": "0"}
        elif (flag == "4"):
            name = request.POST.get('name', None)
            password = request.POST.get('password', None)
            # print("2")
            if (name != ""):
                user = User.objects.filter(name=name)
                if len(user) == 0:
                    log = {"flag": "0"}
                else:
                    for i in user:
                        if (i.password == password):
                            if i.shenfen == '课题申请者':
                                log = {"flag": "1", 'flag1': "1"}
                                # print(log)
                            elif i.shenfen == '课题审批者':
                                log = {"flag": "1", 'flag1': "2"}
                            else:
                                log = {"flag": "1", 'flag1': "0"}
                            m = User.objects.filter(name=name).first()
                            request.session['member_id'] = m.id
                        else:
                            log = {"flag": "0"}
            else:
                log = {"flag": "2"}
        else:
            password = request.POST.get('password', None)
            name = request.POST.get('name', None)
            if (name != ""):
                user = User.objects.filter(name=name)
                if len(user) == 0:
                    log = {"flag": "0"}
                else:
                    for i in user:
                        if (i.password == password):
                            if i.shenfen == '课题申请者':
                                log = {"flag": "1", 'flag1': "1"}
                                # print(log)
                            elif i.shenfen == '课题审批者':
                                log = {"flag": "1", 'flag1': "2"}
                            else:
                                log = {"flag": "1", 'flag1': "0"}
                        else:
                            log = {"flag": "0"}
            else:
                log = {"flag": "2"}

        # print(log)
        response = HttpResponse(json.dumps(log))
        return response
    return render(request, "login1.html")


def myshenbao(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题申请者':
            if request.POST:
                name = request.POST['name']
                type = request.POST['type']
                danwei = request.POST['danwei']
                search_dict = dict()
                search_dict["projec_tname__contains"] = name
                search_dict["shenqing_ren"] = user[0].id
                if type != '空':
                    search_dict["project_type"] = type
                if danwei != '空':
                    search_dict["shenqing_unit"] = danwei
                response = Project.objects.filter(**search_dict)
                context = {'pro_list': response}
                return render(request, "myshenbao.html", context)
            pro_list = Project.objects.filter(shenqing_ren=user[0])
            return render(request, "myshenbao.html", {'pro_list': pro_list})
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')
    pass


def myshenpi(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题审批者':
            if request.POST:
                name = request.POST['name']
                type = request.POST['type']
                danwei = request.POST['danwei']
                state = request.POST['state']
                # print(state)
                search_dict = dict()
                search_dict["projec_tname__contains"] = name
                search_dict["shenpi_ren"] = user[0].id
                if type != '空':
                    search_dict["project_type"] = type
                if danwei != '空':
                    search_dict["shenqing_unit"] = danwei
                if state != '空':
                    search_dict["state_shenpi"] = state
                response = Project.objects.filter(**search_dict)
                context = {'pro_list': response}
                return render(request, "myshenpi.html", context)
            pro_list = Project.objects.filter(shenpi_ren=user[0])
            return render(request, "myshenpi.html", {'pro_list': pro_list})
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')
    pass


def shenpi(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题审批者':
            if request.method == 'POST':
                type = request.POST.get("fenlei", None)
                danwei = request.POST.get("danwei", None)
                name = request.POST.get("name", None)
                search_dict = dict()
                if name != None:
                    search_dict["projec_tname__contains"] = name
                search_dict["state_shenpi"] = '未审核'
                if type != 'null':
                    search_dict["project_type"] = type
                if danwei != 'null':
                    search_dict["shenqing_unit"] = danwei
                pro_list = Project.objects.filter(**search_dict)
                return render(request, "1.html", {'pro_list': pro_list})
            else:
                pro_list = Project.objects.filter(state_shenpi='未审核')
            return render(request, "shenpi.html", {'pro_list': pro_list})
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')


def edit_shenpi(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题审批者':
            if request.method == 'GET':
                nid = request.GET.get('nid')
                obj = Project.objects.filter(id=nid).first()
                return render(request, 'edit_shenpi.html', {'obj': obj})
            elif request.method == 'POST':
                nid = request.GET.get('nid')
                text = request.POST.get('text')
                select = request.POST.get('select')
                # print(nid,text,select)
                pro = Project.objects.filter(id=nid).first()
                if pro:
                    pro.review = text
                    pro.state_shenpi = select
                    pro.time_shenhe = datetime.datetime.now()
                    pro.shenpi_ren = user[0]
                    pro.save()
                flag = {"flag": "0"}
                response = HttpResponse(json.dumps(flag))
                return response
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')


def shenbao(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题申请者':
            if request.method == 'POST':
                shenbao_id = request.session.get('member_id', default=None)
                name = request.POST.get('name', None)
                danwei = request.POST.get('danwei', None)
                fenlei = request.POST.get('fenlei', None)
                myFile = request.FILES.get("myfile", None)
                project = Project.objects.filter(project_type=fenlei, shenqing_ren=user[0], shenqing_unit=danwei,
                                                 projec_tname=name)
                if project.__len__() != 0:
                    flag = {"flag": "1"}
                    response = HttpResponse(json.dumps(flag))
                    return response
                else:
                    # print(shenbao_id, name, danwei, fenlei, myFile)
                    if myFile is None:
                        return HttpResponse('文件未上传!')
                    path = "file\\" + str(shenbao_id) + '\\' + fenlei + "\\" + name + "\\"
                    if not os.path.exists(path):
                        os.makedirs(path)
                    destination = open(os.path.join(path, myFile.name), 'wb+')
                    for chunk in myFile.chunks():  # 分块写入文件
                        destination.write(chunk)
                    destination.close()
                    Project.objects.create(project_content=myFile.name, projec_tname=name, project_type=fenlei,
                                           shenqing_ren=user[0],
                                           shenqing_unit=danwei, state_shenpi='未审核',
                                           time_shenbao=datetime.datetime.now())
                    flag = {"flag": "0"}
                    response = HttpResponse(json.dumps(flag))
                    return response
            return render(request, "shenbao.html")
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')


def download(request, a, b, c, d):
    # print(a, b, c, d)
    path = 'file/' + a + '/' + b + '/' + c + '/'
    file_name = d
    # print(path + file_name)
    file = open(path + file_name, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response


def del_shenbao(request, nid):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题申请者':
            Project.objects.filter(id=nid).delete()
            return redirect('/myshenbao')
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')


def edit_shenbao(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题申请者':
            if request.method == 'GET':
                nid = request.GET.get('nid')
                obj = Project.objects.filter(id=nid).first()
                return render(request, 'edit_shenbao.html', {'obj': obj})
            elif request.method == 'POST':
                nid = request.GET.get('nid')
                name = request.POST.get('name')
                danwei = request.POST.get('danwei')
                fenlei = request.POST.get('fenlei')
                myFile = request.FILES.get("myfile", None)
                project = Project.objects.filter(project_type=fenlei, shenqing_ren=user[0], shenqing_unit=danwei,
                                                 projec_tname=name)
                if project.__len__() != 0:
                    flag = {"flag": "1"}
                    response = HttpResponse(json.dumps(flag))
                    return response
                else:
                    # print(nid, name, danwei, fenlei, myFile)
                    if myFile is None:
                        return HttpResponse('文件未上传!')
                    path = "file\\" + str(user[0].id) + '\\' + fenlei + "\\" + name + "\\"
                    # print(path)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    destination = open(os.path.join(path, myFile.name), 'wb+')
                    for chunk in myFile.chunks():  # 分块写入文件
                        destination.write(chunk)
                    destination.close()
                    Project.objects.filter(id=nid).update(project_content=myFile.name, projec_tname=name,
                                                          project_type=fenlei, shenqing_ren=user[0],
                                                          shenqing_unit=danwei, state_shenpi='未审核',
                                                          time_shenbao=datetime.datetime.now())
                    flag = {"flag": "0"}
                    response = HttpResponse(json.dumps(flag))
                    return response
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')


def shenhe(request, name, type, text, select):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '课题审批者':
            # print(name, type, text, select)
            pro = Project.objects.filter(projec_tname=name, project_type=type,state_shenpi="未审核").first()
            if pro:
                pro.review = text
                pro.state_shenpi = select
                pro.time_shenhe = datetime.datetime.now()
                pro.shenpi_ren = user[0]
                pro.save()
                reg = {"flag": 1}
            else:
                reg = {"flag": 0}
            response = HttpResponse(json.dumps(reg))
            return response
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您未登陆!')


def review(request):
    type = request.GET.get('fenlei', None)
    name = request.GET.get('name', None)
    pro = Project.objects.filter(projec_tname=name, project_type=type).first()
    reg = {"review": pro.review}
    response = HttpResponse(json.dumps(reg))
    return response


def user(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '管理员':
            if request.POST:
                name = request.POST['name']
                shenfen = request.POST['shenfen']
                search_dict = dict()
                search_dict["name__contains"] = name
                if shenfen != '空':
                    search_dict["shenfen"] = shenfen
                response = User.objects.filter(~Q(id=id), **search_dict)
                context = {'user_list': response}
                return render(request, "user.html", context)
            user_list = User.objects.filter(~Q(id=id))
            return render(request, "user.html", {"user_list": user_list})
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您没有登录!')


def edit_user(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = User.objects.filter(id=nid).first()
        return render(request, 'edit_user.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        password = request.POST.get('password')
    User.objects.filter(id=nid).update( password=password)
    return redirect('/user')


def del_user(request):
    nid = request.GET.get('nid')
    try:
        User.objects.filter(id=nid).delete()
    except:
        pass
    return redirect('/user')


def add_user(request):
    if request.method == "GET":
        dep_list = User.objects.all();
        return render(request, 'add_user.html', {'dep_list': dep_list})
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        shenfen = request.POST.get('shenfen')
        User.objects.create(name=name, shenfen=shenfen, password=password)
        return redirect('/user')


def project(request):
    if request.session.get('member_id', default=None):
        id = request.session.get('member_id', default=None)
        user = User.objects.filter(id=id)
        if user[0].shenfen == '管理员':
            if request.POST:
                name = request.POST['name']
                type = request.POST['type']
                danwei = request.POST['danwei']
                state = request.POST['state']
                year = request.POST['year']
                search_dict = dict()
                search_dict["projec_tname__contains"] = name
                if type != '空':
                    search_dict["project_type"] = type
                if danwei != '空':
                    search_dict["shenqing_unit"] = danwei
                if state != '空':
                    search_dict["state_shenpi"] = state
                if year != '空':
                    search_dict["time_shenbao__year"] = year
                response = Project.objects.filter(**search_dict)
                context = {'project_list': response}
                return render(request, "project.html", context)
            project_list = Project.objects.all()
            return render(request, "project.html", {"project_list": project_list})
        else:
            return HttpResponse('您没有此权限!')
    else:
        return HttpResponse('您没有登录!')


def edit_project(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = Project.objects.filter(id=nid).first()
        return render(request, 'edit_project.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        password = request.POST.get('password')
        shenfen = request.POST.get('shenfen')
    Project.objects.filter(id=nid).update(name=name, shenfen=shenfen, password=password)
    return redirect('/project')


def del_project(request):
    nid = request.GET.get('nid')
    Project.objects.filter(id=nid).delete()
    return redirect('/project')


def add_project(request):
    if request.method == "GET":
        dep_list = Project.objects.all();
        return render(request, 'add_user.html', {'dep_list': dep_list})
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        shenfen = request.POST.get('shenfen')
        Project.objects.create(name=name, shenfen=shenfen, password=password)
        return redirect('/project')


def home(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    if request.method == 'POST':
        # print("post")
        fenlei = request.POST.get("fenlei", None)
        danwei = request.POST.get("danwei", None)
        # print(fenlei, danwei)
        if fenlei != 'null' and danwei != 'null':
            pro_list = Project.objects.filter(project_type=fenlei, shenqing_unit=danwei)
            # print(pro_list.__len__())
            return render(request, "2.html", {'pro_list': pro_list})
        elif fenlei != 'null':
            pro_list = Project.objects.filter(project_type=fenlei)
            return render(request, "2.html", {'pro_list': pro_list})
        elif danwei != 'null':
            pro_list = Project.objects.filter(shenqing_unit=danwei, state_shenpi='未审核')
            return render(request, "2.html", {'pro_list': pro_list})
    pro_list = Project.objects.all()
    return render(request, "home.html", {"project_list": pro_list})

def del_test(request):
    nid=request.GET.get("nid")
    reg = {"flag": "0"}
    user=User.objects.filter(id=nid).first()
    pro=Project.objects.filter(shenpi_ren=user).first()
    if pro:
        reg = {"flag": "1"}
    pro=Project.objects.filter(shenqing_ren=user).first()
    if pro:
        reg = {"flag": "1"}
    response = HttpResponse(json.dumps(reg))
    return response

def edit_test(request):
    nid=request.GET.get("nid")
    reg = {"flag": "0"}
    pro=Project.objects.filter(id=nid).first()
    if pro.state_shenpi=='未审核':
        reg = {"flag": "1"}
    response = HttpResponse(json.dumps(reg))
    return response
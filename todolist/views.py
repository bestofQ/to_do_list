from django.shortcuts import render, redirect

# Create your views here.

# 没有数据库之前 使用列表储存数据
lst = [
    {'待办事项': '遛狗', '已完成': False},
    {'待办事项': '武汉加油', '已完成': True},
]

def home(request):
    #声明全局变量
    global lst
    # 判断是get 还是post
    if request.method == 'POST':
        # request.POST.get('待办事项')
        if request.POST.get('待办事项') == '':
            context = {'清单': lst, '警告':'请输入内容'}
            return render(request, 'todolist/home.html', context)
        else:
            text = request.POST.get('待办事项')
            lst.append({'待办事项': text, '已完成': False})
            # context = {'待办事项': request.POST.get('待办事项')}
            context = {'清单': lst, '信息': '添加成功'}
            return render(request, 'todolist/home.html', context)
    elif request.method == 'GET':
        context = {'清单': lst}
        return render(request, 'todolist/home.html', context)

def delete(request, forloop_counter):
    global lst
    lst.pop(forloop_counter-1)
    # redirect('网址')
    return redirect("todolist:todolist_home")

def about(request):
    return render(request, 'todolist:todolist/about.html')

def edit(request, forloop_counter):
    global lst
    if request.method == 'GET':
        context = {'待修改事项': lst[int(forloop_counter) - 1]['待办事项']}
        return render(request, "todolist/edit.html", context)
    elif request.method == 'POST':
        if request.POST.get('已修改事项') == '':
            return render(request, 'todolist/edit.html', {'警告':'请输入内容'})
        else:
            lst[int(forloop_counter) - 1]['待办事项'] = request.POST.get('已修改事项')
            return redirect("todolist:todolist_home")

def cross(request, forloop_counter):
    global lst
    get_text = request.POST.get('完成状态')
    if get_text == '已完成':
        lst[int(forloop_counter) - 1]['已完成'] = True
    else:
        lst[int(forloop_counter) - 1]['已完成'] = False
    # redirect('网址')
    return redirect("todolist:todolist_home")
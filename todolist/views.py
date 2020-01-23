from django.shortcuts import render

# Create your views here.

def home(request):
	# request.POST.get('待办事项')
	context = {'待办事项': request.POST.get('待办事项')}
	return render(request, 'todolist/home.html', context)

def about(request):
	return render(request, 'todolist/about.html')

def edit(request):
	return render(request, 'todolist/edit.html')
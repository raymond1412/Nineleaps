from django.shortcuts import render,get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.http import Http404,HttpResponseRedirect
# Create your views here.

def home(request):
	return render(request,"home.html")

def add(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = EmployeeForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print(instance.parent)
		try:
			parent_id = Employee.objects.get(name=instance.manager)
			obj = Employee(name=instance.name,designation=instance.designation,manager=instance.manager,parent_id=parent_id.id)
		except Employee.DoesNotExist:
			parent_id = None
			obj = Employee(name=instance.name,designation=instance.designation,manager=instance.manager)
		obj.save()
		messages.success(request,"Successfully Accepted")
		return HttpResponseRedirect('/add')
	context = {
		'form':form
	}
	return render(request,"employee_form.html",context)

def table(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	queryset = Employee.objects.all()
	context = {
		"queryset":queryset,
	}
	return render(request,"table.html",context)

def view(request,id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Employee,id=id)
	context = {
		"instance":instance,
	}
	return render(request,"detail.html",context)

def update(request,id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Employee,id=id)
	form = EmployeeForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		try:
			parent_id = Employee.objects.get(name=instance.manager)
			obj = Employee(name=instance.name,designation=instance.designation,manager=instance.manager,parent_id=parent_id.id)
		except Employee.DoesNotExist:
			parent_id = None
			obj = Employee(name=instance.name,designation=instance.designation,manager=instance.manager)
		obj.save()
		messages.success(request,"Successfully Accepted")
		return HttpResponseRedirect('/view/'+str(id))
	context = {
		"instance":instance,
		"form":form,
	}
	return render(request,"employee_form.html",context)

def listv(request):
	hierarchy = Employee.objects.filter(parent = None)
	context = {
		"hierarchy":hierarchy
	}
	return render(request,"list_view.html",context)
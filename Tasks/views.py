from django.shortcuts import render,redirect
from django.http import HttpResponse
from Tasks.models import *
from Tasks.forms import *
# Create your views here.
def index(request):
    form=TaskForm()
    tasks=Task.objects.all()
    data={'form':form,'tasks':tasks}
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index')
    return render(request,'Tasks/index.html',data)

def edit(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("/index")
    context={'form':form}
    return render(request,'Tasks/edit.html',context)

def delete(request,pk):
    item=Task.objects.get(id=pk)
    context={'item':item}
    if request.method=='POST':
        item.delete()
        return redirect('/index')
    return render(request,'Tasks/delete.html',context)
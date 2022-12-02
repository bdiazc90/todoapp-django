from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Task

# Create your views here.
class IndexView(View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {
            "tasks": tasks
        }
        return render(request, "index.html", context)

    def post(self, request):
        task_name = request.POST['task_name']
        if not task_name == '' and not task_name == None:
            task = Task(name=task_name)
            task.save()
            return redirect("index")
        return HttpResponse("Empty task")

def task_done(request, id):
    task = Task.objects.get(id=id)
    if not task == None:
        task.done()
        return redirect("index")
    return HttpResponse("Empty task")

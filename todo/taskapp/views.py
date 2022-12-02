from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Task

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")    

    def post(self, request):
        task_name = request.POST['task_name']
        if not task_name == '' and not task_name == None:
            task = Task(name=task_name)
            task.save()
            return redirect("index")
        return HttpResponse("Empty task")
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import NewUserForm


# Create your views here.
class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = NewUserForm

    def form_valid(self, form):
        form.save()
        return redirect('login')

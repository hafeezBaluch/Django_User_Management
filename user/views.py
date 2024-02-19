from django.shortcuts import redirect, render
from django.contrib.auth import login,logout
from user.forms import LoginForm,RegistrationForm
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

# Create your views here.
def index(request):
    return render(request,'index.html')

def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page') # go to index.html(home page)
    else:
        form = RegistrationForm()
    return render(request,'form/register.html',{"form":form})
            

def user_login(request):
    if request.method =="POST":
        form = LoginForm(request,data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return render(request,"index.html",{"user":user})
    else:
        form = LoginForm()
    return render(request,"form/login.html",{"form":form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home_page')



class CustomPasswordResetView(PasswordResetView):
    template_name = "form/password_reset.html"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "form/password_reset_done.html"
    


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "form/password_reset_confirm.html"

    def form_valid(self, form):
        uidb64 = self.kwargs["uidb64"]
        token = self.kwargs["token"]
        # Your logic here
        return super().form_valid(form)


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "form/password_reset_complete.html"
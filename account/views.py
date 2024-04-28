from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib.auth.views import LoginView
from . import forms
from django.contrib.auth.forms import SetPasswordForm
from .models import UserAccount
from django.contrib import messages


# Create your views here.
class UserReg(FormView):
    template_name='account/user_reg.html'
    form_class = UserRegForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # print(form.cleaned_data)
        return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     form.add_error(None, "NID is not unique")
    #     return super().form_invalid(form)

    

class UserLoginView(LoginView):
    template_name='account/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
def user_logout(req):
    logout(req)
    return redirect('login')


def editProfile(req):
    if req.method== 'POST':
        print(req)
        edit_form=forms.UserUpdateForm(req.POST, instance=req.user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('profile')
        else:
            print("invalid form")
    else:
        edit_form = forms.UserRegForm(instance=req.user)
    return render(req, 'account/profile.html', {'form': edit_form})

def profileInfo(req):
    user_acc = UserAccount.objects.filter(user=req.user)
    return render(req, 'account/profileInfo.html', {'user_acc':user_acc})

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'account/passchange.html', {'form': form})
    else:
        return redirect('login')
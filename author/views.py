from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# def add_author(request):
#     if request.method =='POST':
#         author_form=forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form=forms.AuthorForm()
#     return render(request,'add_author.html',{'form' : author_form})

def register(request):
    if request.method =='POST':
        register_form=forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created Successfully')
            return redirect('register')
    else:
         register_form=forms.RegistrationForm()
    return render(request,'register.html',{'form' :  register_form,'type':'Register'})

def user_login(request):
    if request.method =='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user  is not None:
                messages.success(request,'Logged in  Successfully')
                login(request,user)
                return redirect('user_login')
            else:
                messages.warning(request,'Login information is incorrect')
                return redirect('profile')
    else:
        form=AuthenticationForm()
    return render(request,'register.html',{'form' : form, 'type':'Login'})

@login_required
def profile(request):
    if request.method =='POST':
        profile_form=forms.UserChangeForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
         profile_form=forms.UserChangeForm(instance=request.user)
    return render(request,'profile.html',{'form' :  profile_form})


def pass_change(request):
    if request.method =='POST':
        pass_change_from=PasswordChangeForm(request.user,data=request.user)
        if pass_change_from.is_valid():
           pass_change_from.save()
           messages.success(request,'password updated Successfully')
           update_session_auth_hash(request,pass_change_from.user)
           return redirect('register')
    else:
          pass_change_from=PasswordChangeForm(user=request.user) 
    return render(request,'pass_change.html',{'form':pass_change_from})




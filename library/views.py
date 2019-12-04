from django.shortcuts import render,redirect
from .forms import loginform1,login
from .models import student,book
from django.http import HttpResponse,HttpResponseRedirect
# from django.db.models import Q
#import csv,reportlab
from django.contrib.auth.models import User
from django.core.mail import send_mail
from random import randint
from django.views.generic import View,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy

def hello(request):
    return render(request,'home.html')


def getloginpage(request):
    form=loginform1()
    if request.method=='POST':    
        form=loginform1(request.POST)
        if form.is_valid():
            global email
            n='app'
            for i in range(0,4):
                n=n+str(randint(0,9))
            reg_id=n
            student_name=form.cleaned_data['student_name']
            username=form.cleaned_data['username'] 
            password=form.cleaned_data['password']
            branch=form.cleaned_data['branch']
            email=form.cleaned_data['email']
            lp=student(reg_id=reg_id,student_name=student_name,username=username,password=password,branch=branch,email=email)
            lp.save()
            reg_id=request.session['id']=lp.reg_id
            sub="registration sucess"
            sender='sandeep96424@yahoo.in'
            msg="Hello Mr/Ms."+request.POST['student_name']+"\n"+"register_id:"+reg_id+"\n"+"Username:"+request.POST['username']+"\n""Password:"+request.POST['password']+"\n"+"Branch:"+request.POST['branch']+"\n"+"your application submited successfully."+"\n"+"- It is auto genrated yahoo mail."+"\n"+"-Thank you for register"+"\n"+"it is auto generated mail"
            to=request.POST['email']
            send_mail(sub,(msg),sender,[to])
            return redirect("/login/")
    return render(request,"register.html",{'form':form})

#for  login

def getlogin(request):
    form=login()
    if request.method=='POST':
        form=login(request.POST) 
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            dbuser=student.objects.get(username=username,password=password)
            if not dbuser:
                return HttpResponse('access denied')
            else:
                return render(request,"search.html",{'username':dbuser.username,'name':dbuser.student_name,
                                                    'branch':dbuser.branch,'email':dbuser.email})        
    return render(request,"login.html",{'form':form})   

def Book(request):
    if request.method=='POST':
        books=request.POST['bk']
        data=book.objects.filter(book_name__icontains=books)
        if data:
            return render(request, 'book.html',{'data':data})
        else:
            return HttpResponse("No book")
    return render(request, 'book.html')

# def branch(request):
#     if request.method=='POST':
#         branch=request.POST['bnch']
#         data=book.objects.filter(branch=branch)
#         if branch== 'ECE':
#             return HttpResponse("ECE Books")
#         if branch== 'EEE' and 'eee':
#             return HttpResponse("EEE Books")
#         if branch == 'CSE' and 'cse':
#             return HttpResponse('CSE Books')
#         else:
#             return HttpResponse('Enter Correct Branch')

def all(request):
    data=book.objects.filter()
    return render(request, 'all.html',{'data':data})

def details(request):
    if request.method=='POST':
        bid=request.POST['id']
        data=book.objects.filter(book_id=bid)
        return render(request,'details.html',{'data':data})
    return render(request,'details.html')  


def forgot(request):
        if request.method=="POST":
            email=request.POST['ema']
            ft=udata.objects.get(email=email)
            if ft:
                to=email
                pwd=ft.password
                name=ft.name
                sub="password reset"
                msg="Hello Mr/Ms:"+name+"\n"+"your password:"+"\n"+pwd
                sender="sandeep96424@yahoo.in"
                send_mail(sub,msg,sender,[to])
                return render(request,'forgot.html',{'msg':'password sent sucessfully to your email'})        
            else:
                return HttpResponse("Enter correct Email id")   
        return render (request,'forgot.html')
# def export_users_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="student.pdf"'

#     writer = csv.writer(response)
#     writer.writerow(['student_name','username','password','branch'])

#     users =student.objects.all().values_list('student_name','username','password','branch')
#     for user in users:
#         writer.writerow(user)

#     return response

# def csv1(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="book.pdf"'

#     writer = csv.writer(response)
#     writer.writerow(['book_id','book_name','author','Image','Documents'])

#     users =book.objects.all().values_list('book_id','book_name','author','Image','Documents')
#     for user in users:
#         writer.writerow(user)

#     return response   


class bookeditView(UpdateView):
    model=book
    fields=['author','branch','book_name']
    template_name='bookedit.html'

class bookdlt(DeleteView):
    model=book
    template_name='delete.html'
    context_object_name="book"
    success_url=reverse_lazy('display_view')

class listv(ListView):
    model=book
    template_name="allb.html"

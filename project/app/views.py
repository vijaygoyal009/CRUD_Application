from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from .forms import StudentRegistrationForm
# Create your views here.
def adddata(request):
    if request.method == 'POST':
        obj = StudentRegistrationForm(request.POST)
        if obj.is_valid():
            nm = obj.cleaned_data['name']
            em = obj.cleaned_data['email']
            pw = obj.cleaned_data['password']
            reg = Student(name=nm, email=em , password=pw)
            reg.save()
            obj = StudentRegistrationForm()
            # obj.save()
    else:
        obj = StudentRegistrationForm()
    return render(request,'add.html',{'form':obj})

def showdata(request):
    stu = Student.objects.all()
    return render(request,'show.html',{'data':stu})


def deletedata(request,id):
    d = Student.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/show/')



def updatedata(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistrationForm(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistrationForm(instance=pi)

    return render(request,'update.html',{'form':fm})


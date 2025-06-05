from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    data={
        'title':'Home new',
        'bdata':'welcome parth',
        'clist':['php','java','python'],
        'number':[],
        'student_details':[
            {'name':'pradeep','phone':9865466432},
            {'name':'testing','phone':9854545432}
        ]
    }

    return render(request,"index.html",data)

def aboutus(request):
    return render(request,"aboutus.html")

def course(request):
    return HttpResponse("welcome to wscube1")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def userForm(request):
     finalans=0
     try:
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         finalans=n1+n2
     except:
        pass
        
     return render(request,"userform.html",{'output':finalans})
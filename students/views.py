from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Views for students
def students_list(request):
    return render(request, 'students/students_list.html')

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request,sid):
    return HttpResponse('<h1>Edit Students %s</h1>' %sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)


#Views for groups
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Group %gid Edit Form</h1>' %gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %gid</h1>' %gid)

# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Views for students
def students_list(request):
    students = (
        {'id':1,
        'first_name':u'Андрій',
        'last_name':u'Корост',
        'ticket':235,
        'image':'img/me.jpeg'},
        {'id':2,
         'first_name':u'Максим',
         'last_name': u'Настенко',
         'ticket': 2123,
         'image':'img/piv.png'},
        {'id':3,
         'first_name': u'Віктор',
         'last_name': u'Конєв',
         'ticket': 156,
         'image':'img/podoba3.jpg'},
    )
    return render(request, 'students/students_list.html', {'students':students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request,sid):
    return HttpResponse('<h1>Edit Students %s</h1>' %sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)


#Views for groups
def groups_list(request):
    groups = ({
        'id':1,
        'groups_name':u'МтМ-21',
        'leader':{'id':1, 'name': u'Корост Андрій'}},
    {
        'id':2,
        'groups_name':u'МтМ-22',
        'leader':{'id':2, 'name': u'Настенко Максим'}},
    {
        'id':3,
        'groups_name':u'МтМ-23',
        'leader':{'id':3, 'name': u'Конєв Віктор'}})
    return render(request, 'students/groups_list.html', {'groups':groups})

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Group %s Edit Form</h1>' %gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s </h1>' %gid)

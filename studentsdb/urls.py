
from django.conf.urls import url
from django.contrib import admin
from students.views import students, groups
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Students urls
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$',students.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$',students.students_delete, name='students_delete'),
    url(r'^admin/', admin.site.urls),

    #groups urls
    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$',groups.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

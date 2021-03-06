
from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index ),
url('courses_view', views.courses_view),
url(r'^course/(\d+)/$', views.course_detail),
url('exercises_view', views.exercises_view),
url(r'^exercise/(\d+)/$', views.exercise_detail),
# url('students_view', views.students_view),
url('sheets_view', views.sheets_view),
url(r'^activities', views.activities,name='activities'),
]
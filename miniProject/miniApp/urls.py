from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/<int:teacher_id>', views.teacherDetails, name='details'),
    path('teachers/form/', views.addTeacherData, name='form'),
    path('teachers/delete/<int:teacher_id>', views.deleteTeacher, name='delete'),
    path('teachers/edit/<int:teacher_id>', views.editTeacher, name='edit'),
]
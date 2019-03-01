from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TeacherForm
from .models import TeacherModel

# root function  for main page shows a list of all teachers
def index(request):
    teacher_list = TeacherModel.objects.all()

    return render(request, 'miniApp/index.html', {'teacher_list': teacher_list})

# assigns teacher_id to the teacher model
def teacherDetails(request, teacher_id):
    return render(request, 'miniApp/teacherDetails.html', {'current_teacher': TeacherModel[teacher_id]})

# function that enables a form to used and posted to eht data base and rendered in browser
def addTeacherData(request):
    new_form = TeacherForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')

    return render(request, 'miniApp/addteacher.html', {'teacherForm': new_form})

# allows the teacher data to edited
def editTeacher(request, teacher_id):
    teacher = get_object_or_404(TeacherModel, pk=teacher_id)
    edit_form = TeacherForm(request.POST or None, instance=teacher)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')

    return render('miniApp/teacherDetails.html', {'teacherform': edit_form})

# allows the teacher data to be deleted
def deleteTeacher(request, teacher_id):
    teacher = get_object_or_404(TeacherModel, pk=teacher_id)
    edit_form = TeacherForm(request.POST or None, instance=teacher)
    if edit_form.is_valid():
        edit_form.delet()
        return redirect('index')

    return render('miniApp/deleteteacher.html', {'selectedTeacher': edit_form})

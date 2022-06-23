from django.shortcuts import render
from .models import School

# Create your views here.

my_school = School("Django School") # create a school instance


def index(request):
    my_data = {"school_name": my_school.name}
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    staff_list = my_school.staff
    data = { 'staff_list': staff_list }
    return render(request, 'pages/staff.html', data)
    
def staff_detail(request, employee_id):
    employee = ""
    for member in my_school.staff:
        if member.employee_id == int(employee_id):
            employee = member
    data = {'employee': employee}
    return render(request, 'pages/detail.html', data)


def list_students(request):
    student_list = my_school.students
    data = { 'student_list': student_list }
    return render(request, 'pages/student.html', data)


def student_detail(request, school_id):
    student = ""
    for member in my_school.students:
        if member.school_id == int(school_id):
            student = member
    data = {'student': student}
    return render(request, 'pages/studentdetail.html', data)
from django.shortcuts import render
from django.db.models import Q
from .models import Student
from .filters import StudentFilter

def index(request):
	data = request.GET
	name = data.get('name')
	father_name = data.get('f_name')
	reg_no = data.get('reg_no')
	s_index = data.get('s_index')

	if reg_no:
		students = Student.objects.filter(regno=reg_no)
	else:
		students = Student.objects.all()
		student_filter = StudentFilter(request.GET, queryset=students)
		students = student_filter.qs

	context = {
		'students': students
	}
	return render(request, 'index.html', context)
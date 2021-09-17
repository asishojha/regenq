from django.shortcuts import render
from django.db.models import Q
from .models import Student
from .filters import StudentFilter

def index(request):
	data = request.GET.copy()
	name = data.get('name', '')
	father_name = data.get('f_name', '')
	reg_no = data.get('reg_no', '')
	s_index = data.get('school__school', '')

	if reg_no:
		students = Student.objects.filter(regno__iexact=reg_no)

	else:
		if s_index != '':
			students = Student.objects.filter(school__school__iexact=s_index)
			if name != '' and father_name != '':
				students = students.filter(Q(name__icontains=name) & Q(f_name__icontains=father_name))
			elif name != '' and father_name == '':
				students = students.filter(name__icontains=name)
			elif name == '' and father_name != '':
				students = students.filter(f_name__icontains=father_name)
		else:
			if name != '' and father_name != '':
				students = Student.objects.filter(Q(name__icontains=name) & Q(f_name__icontains=father_name))
			elif name != '' and father_name == '':
				students = Student.objects.filter(name__icontains=name)
			elif name == '' and father_name != '':
				students = Student.objects.filter(f_name__icontains=father_name)
			else:
				students = Student.objects.none()

	context = {
		'students': students
	}
	return render(request, 'index.html', context)
from .models import Student
import django_filters

class StudentFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
	f_name = django_filters.CharFilter(field_name='f_name', lookup_expr='icontains')
	school__school = django_filters.CharFilter(field_name='school__school', lookup_expr='iexact')


	class Meta:
		model = Student
		fields = ['name', 'f_name', 'school__school']
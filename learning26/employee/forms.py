from django import forms
from .models import Employee,Course,feedback,complaint  

#employee form
#modelForm -->it will create form using model fileds
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'

#normal form
class complaintForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    problem = forms.CharField(widget=forms.Textarea)        
from django import forms
from .models import Attendance_List, Leave_List


class AttListLogin(forms.ModelForm):
    class Meta:
        model = Attendance_List
        fields = ['loginid']

class LeaveListLogin(forms.ModelForm):
    class Meta:
        model = Leave_List
        fields = ['loginid']

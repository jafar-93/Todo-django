from django import forms
from .models import Todo

class TodoCreated(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    date = forms.DateTimeField()


class TodoUpdatedForm(forms.ModelForm):
    class Meta: 
        model = Todo
        fields = ('title','content','date' )
from django import forms

from todo_app.models import todo_model


class todo_form(forms.ModelForm):
    class Meta:
        model=todo_model
        fields=('title','content','date')

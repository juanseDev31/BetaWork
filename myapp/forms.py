from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task Title",max_length=200,widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'input'}), label="Task Description")

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Project Name',max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe un título' }
    ), min_length=10, max_length=200)

    content = forms.CharField(widget=CKEditorWidget)

    pdfFile = forms.FileField(label='Subir Archivo' ,required=False)

    class Meta:
        model = Blog
        fields = ['title','content','pdfFile',]
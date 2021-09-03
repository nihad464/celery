from logging import Filter
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
from user.models import CustomUser
from .tasks import delete_old_files

class FileForm(forms.ModelForm):
    class Meta:
        model=Filemodel
        fields=['name','description','file']





class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields=['content']


class ShareForm(forms.ModelForm):
    class Meta:
        model=ShareModel
        fields=['receiver','see_comments']

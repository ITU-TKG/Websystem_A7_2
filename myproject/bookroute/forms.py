from django.forms import ModelForm
from . models import Page

class PageForm(ModelForm):
    class Meta:
        model=Page
        fields=["title","body","picture"]#ユーザーが入力する項目

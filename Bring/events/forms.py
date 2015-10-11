from django import forms
from .models import Transportation, Item

class DetailForm(forms.Form):
    place = forms.CharField(label="目的地", max_length=64)
    start_date = forms.DateField(label="開始日期")
    end_date = forms.DateField(label="結束日期")
    
    GENDER_CHOICE = (
        ("m", "男"),
        ("f", "女"),
    )
    gender = forms.ChoiceField(label="性別", choices=GENDER_CHOICE, widget=forms.RadioSelect)
    
    transportation = forms.ModelMultipleChoiceField(queryset=Transportation.objects.all(), label="交通方式", widget=forms.CheckboxSelectMultiple)



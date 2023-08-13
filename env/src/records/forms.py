from django import forms

from datetime import datetime

from .models import Record

class RecordCreateForm(forms.ModelForm):
    date_lifted = forms.DateField(widget=forms.SelectDateWidget(years=range(datetime.now().year-100, datetime.now().year+1)), initial=datetime.now().today(), required=True)

    class Meta:
        model = Record
        fields = [
            'lift_name',
            'weight_lifted',
            'repetitions',
            'description',
            'body_weight',
            'date_lifted',
            'video',
        ]

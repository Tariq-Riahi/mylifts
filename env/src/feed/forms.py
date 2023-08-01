from django import forms

from .models import RecordPost
from records.models import Record


class RecordPostCreateForm(forms.ModelForm):
    class Meta:
        model = RecordPost
        fields = [
            'title',
            'description',
            'item',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RecordPostCreateForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['item'].queryset = Record.objects.filter(user=user)

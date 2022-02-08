
from customers.models import Feedback
from django.forms import ModelForm

class FeedbackForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service_feedback'].widget.attrs.update({
            'name':'service_feedback',
            'id':'service_feedback',
            'type':'textarea',
            'class':'form-input',
            'placeholder':'Your Feedback',
            'title':'Write your feedback here',

        })
        self.fields['rating'].widget.attrs.update({
            'min':'1',
            'max':'5',
            'title':'You can give from 1 to 5.',

        })
    class Meta:
        model = Feedback
        fields = ['rating','subject','service_feedback']

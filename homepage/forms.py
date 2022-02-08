from django import forms
from django.forms import ModelForm
from homepage.models import Order

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class OrderForm(ModelForm):
      
      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contact_no'].widget.attrs.update({
            'required':'',
            'name':'contact_no',
            'id':'contact_no',
            'type':'text',
            'class':'form-input',
            'placeholder':'9843060170',
            'max':'10',
            'min':'9',
        })
        self.fields['contact_address'].widget.attrs.update({
            'required':'',
            'name':'contact_address',
            'id':'contact_address',
            'type':'text',
            'class':'form-input',
            'placeholder':'Baluwakhani, Kapan',
            'maxlength':'100',
            'minlength':'2',
        })
        self.fields['date'].widget.attrs.update({
            'required':'',
            'name':'date',
            'id':'date',
            'type':'date',
            'class':'form-input',
            
        })
        self.fields['start_time'].widget.attrs.update({
            'required':'',
            'name':'start_time',
            'id':'start_time',
            'type':'time',
            'class':'form-input',
        })
        self.fields['end_time'].widget.attrs.update({
            'required':'',
            'name':'end_time',
            'id':'end_time',
            'type':'number',
            'class':'form-input',
        })

      class Meta:
        widgets = {'date': DateInput(), 'start_time': TimeInput(), 'end_time': TimeInput()}
        model = Order
        fields = [ 'contact_no', 'contact_address', 'date','start_time','end_time']
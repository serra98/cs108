# quotes/forms.py 

from django import forms 
from .models import Quote 

class CreateQuoteForm(forms.ModelForm):
    '''A form to add new quotes to teh datagbase.'''

    class Meta:
        '''associate this form w Quote model '''
        model = Quote
        fields = ['person','text'] #which fields from model 

class UpdateQuoteForm(forms.ModelForm):
    '''A form to update a quote to the database.'''

    class Meta: 
        '''associate this form with the Quote model.'''
        model = Quote
        fields = ['person','text',] #which fields from model should we use



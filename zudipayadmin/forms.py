from django import forms
from Exchange.models import pricecard
class UpdatePrices(forms.ModelForm):
	price = forms.FloatField(widget = forms.TextInput(
	attrs = {
			'class':'form-control',
			'placeholder':'Write a address...'
		}), label='')
	class Meta:
		model = pricecard
		fields = ('price',)

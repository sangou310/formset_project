from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Order
        fields = ['date', 'code', 'quantity']
        # widgets = {
        #     'date': forms.DateInput(attrs={'type': 'date'}),
        # }


OrderCreateFormset = forms.modelformset_factory(
    Order,
    form=OrderCreateForm,
    extra=3,
    can_delete=True,
)

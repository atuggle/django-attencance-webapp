from django import forms
from django.forms import inlineformset_factory
from .models import EmailTemplate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, ButtonHolder, Fieldset, HTML, Button, Row, Field


class SendEmailForm(forms.Form):
    error_css_class = 'errorlist'

    from_address = forms.CharField(label='From Address', max_length=100)
    email_templates = forms.ChoiceField(label='Email Template', initial='', required=True)

    class Meta:
        model = EmailTemplate

    def __init__(self, *args, **kwargs):
        super(SendEmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_id = 'id-registrationForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'detail'
        self.helper.layout = Layout(
            Div(
                Div('from_address'),
                Div('email_templates'),
                css_class='row'
            ),
        )

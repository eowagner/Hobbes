from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy
from django.contrib.auth.hashers import make_password, is_password_usable, check_password
from django.utils import timezone

from publicgoods.models import Game_Instance, Game_Response

from decimal import Decimal

from gametheory import pseudonym_generator 

class CreateInstanceForm(forms.Form):
    instance_name = forms.CharField(label="Game Name")
    instructor_password = forms.CharField(widget=forms.PasswordInput)
    user_keyword = forms.CharField()
    pot_multiplier = forms.DecimalField(initial=2, min_value=Decimal('0.00'))
    endowment = forms.DecimalField(initial=5, min_value=Decimal('0.00'))
    max_contribution = forms.DecimalField(initial=5, min_value=Decimal('0.00'))

    class Meta:
        model = Game_Instance

    def process(self):
        cd = self.cleaned_data

        pwd = make_password(cd['instructor_password'])

        g = Game_Instance(instance_name=cd['instance_name'],
                time_opened=timezone.now(),
                pot_multiplier=cd['pot_multiplier'],
                endowment=cd['endowment'],
                max_contribution=cd['max_contribution'],
                instructor_password=pwd,
                user_keyword=cd['user_keyword'])
        g.save()

        return g.id

class ParticipateForm(forms.Form):
    name = forms.CharField()
    eid = forms.CharField()
    contribution = forms.DecimalField(min_value=Decimal('0.00'))

    def __init__(self, *args, **kwargs):
        self.max_contribution = kwargs.pop("max_contribution")
        super().__init__(*args, **kwargs)

    def clean_contribution(self):
        data = self.cleaned_data['contribution']

        if (data > self.max_contribution):
            error_text='You cannot contribute more than '+str(self.max_contribution)
            raise ValidationError(ugettext_lazy(error_text))
        else:
            return data

    class Meta:
        model = Game_Response

    def process(self, instance):
        cd = self.cleaned_data

        pseudonym = pseudonym_generator.random_pseudonym()

        r = Game_Response(game=instance, 
                contribution=cd['contribution'], 
                name=cd['name'], 
                eid=cd['eid'], 
                pseudonym=pseudonym)
        r.save()

        return (pseudonym, round(cd['contribution'],2))

class InstructorViewLoginForm(forms.Form):
    instructor_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.pwd = kwargs.pop("instructor_password")
        super().__init__(*args, **kwargs)

    def clean_instructor_password(self):
        data = self.cleaned_data['instructor_password']

        if not check_password(data, self.pwd):
            raise ValidationError(ugettext_lazy("Incorrect Password"))
        else:
            return data

class ParticipateLoginForm(forms.Form):
    user_keyword = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.key = kwargs.pop("user_keyword")
        super().__init__(*args, **kwargs)

    def clean_user_keyword(self):
        data = self.cleaned_data['user_keyword']

        if not data==self.key:
            raise ValidationError(ugettext_lazy("Incorrect Keyword"))
        else:
            return data
    

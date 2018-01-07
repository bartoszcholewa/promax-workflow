from django import forms
from .models import Obieg, Material, Status
from .validators import validate_obieg


class ObiegCreateForm(forms.ModelForm):
    obieg_name = forms.CharField(label='Nazwa obiegu', widget=forms.TextInput(
        attrs={'placeholder': 'PW-000123'}), validators=[validate_obieg])
    obieg_type = "normalny"
    kod_presta = forms.CharField(
        label='Kod Presta', widget=forms.TextInput(attrs={'placeholder': 'JS8SjdV'}))
    material = forms.ModelChoiceField(
        queryset=Material.objects.all(), label='Materiał', initial=0)
    laminacja = forms.BooleanField(label='Laminacja', required=False)
    link_podgladu = forms.URLField(label='Link Podglądu', widget=forms.TextInput(
        attrs={'placeholder': 'https://...'}))
    zamawiajacy = forms.CharField(label='Zamawiający', widget=forms.TextInput(
        attrs={'placeholder': 'Jan Kowalski'}))
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(), label='Status', initial=2)
    uwagi = forms.TextInput()
    #handlowiec = forms.ModelChoiceField(queryset=Handlowiec.objects.all(), label='Handlowiec', initial=0)

    class Meta:
        model = Obieg
        fields = [
            'obieg_name',
            'kod_presta',
            'material',
            'laminacja',
            'link_podgladu',
            'zamawiajacy',
            'status',
            'uwagi',
            #'handlowiec',
        ]

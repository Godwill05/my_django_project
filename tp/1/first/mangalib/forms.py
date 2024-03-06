from django import forms

class SomeForm(forms.Form):
    username = forms.CharField(max_length=45, label="Nom d'utilisateur")
    
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
    bio = forms.CharField(label="Biographie", widget=forms.Textarea)
    

    publicate = forms.CheckboxInput()
    
    
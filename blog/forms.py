from django import forms

#--- forms.Form
class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='검색')
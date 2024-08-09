from django import forms
from .models import Category

class CategorySelectionForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(Category.objects.all())

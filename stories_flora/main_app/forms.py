from .models import Stories, Stories_i18n, Pages, Languages, Categories, Categories_i18n
from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, NumberInput
from django.contrib.postgres.forms import SimpleArrayField


class StoriesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select..."

    class Meta:
        model = Stories  # table
        fields = ['id', 'category', 'hide_in_stories', 'post_priority', 'fresh_after', 'fresh_before',
                  'clients_eligible']  # столбцы fields = '__all__'

        # characteristics for each column
        widgets = {
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Category id'
            }),
            "post_priority": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fresh before date'
            }),
            "fresh_after": DateInput(attrs={
                'class': 'form-control',
                'type': "date",
                'placeholder': 'dd-mm-yyyy'
            }),
            "fresh_before": DateInput(attrs={
                'class': 'form-control',
                'type': "date",
                'placeholder': 'Fresh before date'
            }),
            "clients_eligible": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Clients eligible'
            })
        }


class Stories_i18nForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['story'].empty_label = "Select..."
        self.fields['language'].empty_label = "Select..."

    class Meta:
        model = Stories_i18n
        fields = ['story', 'language', 'title', 'subtitle', 'title_icon', 'title_image']
        widgets = {
            "story": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Story id'
            }),
            "language": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Language id'
            }),
            "title": Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Title'
            }),
            "subtitle": Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Subtitle'
            }),
            "title_icon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title icon'
            }),
            "title_image": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title image'
            })
        }


class PagesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['story_i18n'].empty_label = "Select..."

    class Meta:
        model = Pages
        fields = ['story_i18n', 'image', 'icon', 'headline', 'text', 'deleted']
        widgets = {
            "story_i18n": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Story_i18n id'
            }),
            "image": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Image'
            }),
            "icon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Icon'
            }),
            "headline": Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Headline'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'rows': 16,
                'placeholder': 'Text'
            })
        }

# class CategoryForm(ModelForm):
#     class Meta:
#         model = Pages
#         fields = ['image', 'category_priority']
#         widgets = {
#             "image": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Image'
#             }),
#             "icon": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Icon'
#             }),
#             "headline": Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 6,
#                 'placeholder': 'Headline'
#             }),
#             "text": Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 16,
#                 'placeholder': 'Text'
#             })
#         }




# from django import forms
# from django.contrib.postgres.forms import SimpleArrayField
# class StoriesForm(forms.Form):
#     category_id = forms.ModelChoiceField( empty_label='Choose category', queryset=Categories.objects.all())
#     hide_in_stories = forms.BooleanField(required=False)
#     post_priority = forms.IntegerField(initial=20)
#     fresh_after = forms.DateField(label='FRESH AFTER', widget=forms.DateInput( attrs={"class": "form-control"}) )
#     fresh_before = forms.DateField()
#     clients_eligible = SimpleArrayField(forms.IntegerField(initial=2))

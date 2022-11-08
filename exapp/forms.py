from django import forms
from exapp.models import Course

class SeachForm(forms.Form):
   search  = forms.CharField(label='Поиск', max_length=100)
   text  = forms.CharField(label='Описание содержит', max_length=100,required=False)
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CourseForm(forms.ModelForm):
    class Meta:
        model =Course
        fields = ['name','text','number']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



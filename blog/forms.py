# # from django import forms
# # from blog.models import Comment
# #
# #
# # class CommentForm(forms.ModelForm):
# #     class Meta:
# #         model = Comment
# #         fields = '__all__'
# #         exclude = ['post']
# #
# #     def __init__(self, *args, **kwargs):
# #         super(CommentForm, self).__init__(*args, **kwargs)
# #         for field_name, field in self.fields.items():
# #             field.widget.attrs = {'class': 'form-control'}
# #             field.widget.attrs = {'placeholder': field_name}
#
# # from django import forms
# # from blog.models import Comment
#
# # from django import forms
# # from blog.models import Comment
# #
# #
# # class CommentForm(forms.ModelForm):
# #     class Meta:
# #         model = Comment
# #         fields = '__all__'
# #         exclude = ['post']
# #
# #     def __init__(self, *args, **kwargs):
# #         super(CommentForm, self).__init__(*args, **kwargs)
# #         for field_name, field in self.fields.items():
# #             field.widget.attrs.update({'class': 'form-control', 'placeholder': field_name.capitalize()})
#
from django import forms
from .models import Comment


#
#
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['post']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field_name.capitalize()})

# from django import forms
# from .models import Comment
#
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'email', 'website', 'message']

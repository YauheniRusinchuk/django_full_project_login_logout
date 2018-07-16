from django import forms

class PostForm(forms.Form):
    content = forms.CharField(label="",
        widget = forms.Textarea(attrs={
            'class': 'content',
            'placeholder': 'Текст ...'
        })
    )

    imgfile = forms.FileField(
        label='FILE',
        widget = forms.FileInput(attrs={
            'class' : 'file_img',
        })
    )




class FormComments(forms.Form):
    text = forms.CharField(label="",
        widget = forms.TextInput(attrs={
            'placeholder': 'Введите комментарий...',
            'class': 'text_comment'
        })
    )

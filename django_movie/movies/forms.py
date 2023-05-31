from django import forms
# from captcha.fields import ReCaptchaField
# from captcha.fields import ReCaptchaField

from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    # captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control border'}),
            'email': forms.EmailInput(attrs={'class': 'form_control border'}),
            'text': forms.Textarea(attrs={'class': 'form_control border'})
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star', )

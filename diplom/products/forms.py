from django import forms

from products.models import Review


class ReviewForm(forms.ModelForm):  # Форма для отзывов
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Оценка')

    class Meta:
        model = Review
        fields = ['text', 'rating']
        labels = {
            'text': 'Напишите свой отзыв здесь',
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

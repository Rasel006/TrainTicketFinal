from django import forms
from .models import Train_list
from .models import UserReviews,TrainPurchase

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]  
class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserReviews
        fields = ['rating', 'body']
        widgets = {
            'rating': forms.Select(choices=STAR_CHOICES),
            'body': forms.Textarea(attrs={'rows': 4}),
        }
        
    def __init__(self, *args, **kwargs):
        self.train = kwargs.pop('train', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        user_purchased_or_borrowed = TrainPurchase.objects.filter(user=self.user, train=self.train).exists()

        if not user_purchased_or_borrowed:
            raise forms.ValidationError("You must purchase the Ticket to leave a review.")

        return cleaned_data
class AddTrainForm(forms.ModelForm):
    class Meta:
        model = Train_list
        fields = ['name', 'time', 'station', 'destination','seat_number','price']

class TrainInfoUpdateForm(forms.ModelForm):
    class Meta:
        model= Train_list
        fields = ['name', 'time', 'destination','seat_number','price']

class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = UserReviews
        fields = ['rating', 'body']
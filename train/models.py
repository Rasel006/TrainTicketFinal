from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TIME_SLOT=(
    ('6:00 AM', '6:00 AM'),
    ('12:00 PM', '12:00 PM'),
    ('3:00 PM', '3:00 PM'),
    ('8:00 PM', '8:00 PM'),
    ('9:00 PM','9:00 PM'),
    ('10:00 PM','10:00 PM'),
    ('11:00 PM','11:00 PM'),
    ('5:00 AM','5:00 AM'),
    ('6:00 AM','6:00 AM'),
    ('7:00 AM','7:00 AM'),

)

DESTINATION=(
    ('Sylhet','Sylhet'),
    ('Sunamganj','Sunamganj'),
    ('Dhaka','Dhaka'),
    ('Kamlapur','Kamlapur'),
    ('Chittagong','Chittagong'),
    ('Rajshahi', 'Rajshahi'),
    ('Coxs Bazar','Coxs Bazar'),
    ('Sirajganj','Sirajganj'),
    ('Tangail','Tangail'),
    ('BimanBondor','BimanBondor'),
    ('Joydevpur','Joydevpur'),
    ('Khulna','Khulna'),
    ('Comilla','Comilla'),


)

SEAT_TYPE=(
    ('AC', 'AC'),
    ('NON_AC', 'NON_AC'),
    ('S_CHAIR','S_CHAIR'),
    ('SNIGHDO','SNIGHDO'),
    ('SHOVON','SHOVON'),
)

SEAT_NO=(
    ('A1','A1'),
    ('A2','A2'),
    ('A3','A3'),
    ('A4','A4'),
    ('A5','A5'),
)
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
] 


class Station(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Train_list(models.Model):
    name = models.CharField(max_length=100)
    time= models.CharField(max_length=15, choices=TIME_SLOT, blank=True, null=True)
    seat= models.CharField(max_length=15, choices=SEAT_TYPE, blank=True, null=True)
    station= models.ManyToManyField(Station)
    seat_number = models.CharField(choices=SEAT_NO, max_length=5, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places = 2, blank=True, null=True)
    destination = models.CharField(max_length=200, choices= DESTINATION, blank=True, null=True)

    def __str__(self):
        return self.name
class UserReviews(models.Model):
    train = models.ForeignKey(Train_list, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=5, choices=STAR_CHOICES)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.train.title}"

class TrainPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train_list, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    before_purchase_balance = models.DecimalField(max_digits=10, decimal_places=2)
    after_purchase_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase by {self.user.username} - Ticket: {self.train.title} - Date: {self.purchase_date}"
from django.db import models
from django.contrib.auth.models import User
from account.models import UserAccount
# Create your models here.
TIME_SLOT=(
    ('6:00 AM', '6:00 AM'),
    ('12:00 PM', '12:00 PM'),
    ('3:00 PM', '3:00 PM'),
    ('8:00 PM', '8:00 PM'),
    ('9:00 PM', '9:00 PM'),
    ('11:00 PM', '11:00 PM'),
    ('7:30 PM', '7:30 PM'),
    ('7:00 AM', '7:00 AM'),
    ('8:00 AM', '8:00 AM'),
    ('5:00 PM', '5:00 PM'),

)

DESTINATION=(
    ('Sylhet','Sylhet'),
    ('Kamlapur','Kamlapur'),
    ('BimanBandar','BimanBandar'),
    ('Chattagram','Chattagram'),
    ('CoxsBazar','CoxsBazar'),
    ('Tangail','Tangail'),
    ('Narshingdi','Narshingdi'),
    ('Rajshahi','Rajshahi'),
    ('Joydevpur','Joydevpur'),
     ('Sirajganj','Sirajganj'),

)

SEAT_TYPE=(
    ('AC', 'AC'),
    ('NON-AC', 'NON-AC'),
    ('Snighdha','Snighdha'),
    ('S_Chair','S_Chair'),
)

SEAT_NO=(
    ('A1','A1'),
    ('A2','A2'),
    ('A3','A3'),
    ('A4','A4'),
    ('A5','A5'),
)

class Station(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Seat_formation(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Train_list(models.Model):
    name = models.CharField(max_length=100)
    time= models.CharField(max_length=15, choices=TIME_SLOT, blank=True, null=True)
    seat= models.CharField(max_length=15, choices=SEAT_TYPE, blank=True, null=True)
    station= models.ManyToManyField(Station)
    seat_formation = models.ManyToManyField(Seat_formation)
    seat_number = models.CharField(choices=SEAT_NO, max_length=5, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places = 2, blank=True, null=True)
    destination = models.CharField(max_length=200, choices= DESTINATION, blank=True, null=True)

    def __str__(self):
        return self.name
    
class BorrowedTicket(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank = True)
    train = models.ForeignKey(Train_list, on_delete = models.CASCADE, null=True, blank = True)
    user_acc = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, default=1, blank=True)
    # seats = models.ForeignKey(Seat_formation, on_delete = models.CASCADE, null=True, blank = True)

    def __str__(self) -> str:
        return f"{self.user} - {self.train}"
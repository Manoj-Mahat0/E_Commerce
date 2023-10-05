from django.db import models

# Create your models here.
class slider(models.Model):
    DISCOUNT_DEALS = (
        ('HOT DEALS','HOT DEALS'),
        ('NEW ARRIVAL', 'NEW ARRIVAL'),
        ('NEW DEALS', 'NEW DEALS'),
    )


    Image = models.ImageField(upload_to='media/Slider_img')
    Discount_Deals = models.CharField(choices=DISCOUNT_DEALS,max_length=100)
    Sale = models.IntegerField()
    Brand_Name = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand_Name

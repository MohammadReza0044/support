from django.db import models

class course(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField

    def __str__(self):
        return self.name




class support (models.Model):
    between15to16 = "بین ساعت 15 تا 16"
    between16to17 = "بین ساعت 16 تا 17"
    between18to20 = "بین ساعت 18 تا 20"
    


    TIME_CHOICES = (
        (between15to16, "بین ساعت 15 تا 16"),
        (between16to17, "بین ساعت 16 تا 17"),
        (between18to20, "بین ساعت 18 تا 20"),
        )
    
    full_name= models.CharField(max_length=100)
    clinic_name=models.CharField(max_length=200)
    phone_number=models.IntegerField(null=True)
    support_date =models.DateField(null=True)
    support_time =models.CharField(max_length=100, choices=TIME_CHOICES)


    class Meta:
        db_table = 'support'  

    def __str__(self):
        return self.full_name

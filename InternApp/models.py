from djongo import models

class Pizza(models.Model):
    ptype = models.CharField(max_length = 50)
    size = models.CharField(max_length = 100)
    toppings = models.CharField(max_length = 500)
    objects = models.DjongoManager()

            
        
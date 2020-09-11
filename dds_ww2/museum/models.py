from django.db import models


class ships(models.Model):
    ship_name = models.CharField(max_length=100,primary_key=True)
    class_name = models.CharField(max_length=100)
    launched = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.ship_name


class battle(models.Model):
    battle_name = models.CharField(max_length=100,primary_key=True)
    battle_date = models.CharField(max_length=50)

    def __str__(self):
        return self.battle_name

    
        
class outcomes(models.Model):
    ship_name = models.ForeignKey('ships', on_delete=models.CASCADE)
    battle_name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    
class user(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=50)
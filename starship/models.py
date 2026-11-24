from django.db import models

# Create your models here.
class Starship(models.model):
    # Defining ourdatabase columns (Fields)
    name = models.CharField(max_length=100)
    ship_class = models.CharField(max_length=50)
    crew-size = models.IntegerField()
    is_active = models.BooleanField(default=True)
    commisioned_date = models.DateTimeField(auto_know_add=True)

    # This method ensures the ship display its name in the admin panel
    # instead of an ugly "Starship Object (1)" string.
    def __str__(self):
        return self.name
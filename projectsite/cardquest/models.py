from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    class Trainer(BaseModel):
        name = models.CharField(max_length=100, null=True, blank=True)
        birthdate = models.DateField(null=True, blank=True)
        location = models.CharField(max_length=100, null=True, blank=True)

        def __str__(self):
            return self.name
    
    class PokemonCard(BaseModel):
        RARITY_CHOICES = (
            ('Common', 'Common'),
            ('Uncommon', 'Uncommon'),
            ('Rare', 'Rare'),
        )
        
        CARDTYPE_CHOICES = (
            ('Fire', 'Fire'),
            ('Water', 'Water'),
            ('Grass', 'Grass'),
            ('Electric', 'Electric'),
            ()
        )

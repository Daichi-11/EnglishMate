import random
from django.db import models

class Card_Set(models.Model):                                                     
    topic = models.CharField(max_length = 50, null = False, blank = False) 
    description = models.CharField(max_length = 300, null = False, blank = True)
    is_active = models.BooleanField(default = True) 

    def __str__(self):
        return self.topic


    def get_card_count(self):
        return self.card_set.count()
    get_card_count.short_description = 'Card Count'


    def get_random_card(self):
        random_number = random.randint(0, self.card_set.count() - 1)
        random_card = self.card_set.all()[random_number]
        return random_card


class Card(models.Model):
    parent_card_set = models.ForeignKey(Card_Set, on_delete = models.CASCADE)
    
    word = models.CharField(max_length = 50, null = False, blank = False)        
    definition = models.TextField(max_length = 500, null = False, blank = False) 
    sentences = models.TextField(max_length = 500, null = False, blank = True)
    

    def __str__(self):
        return self.word


    def is_there_previous_card(self):
        first_card_in_set = self.parent_card_set.card_set.first()
        if self == first_card_in_set:
            return False
        else:
            return True


    def get_previous_card(self):
        first_card_in_set = self.parent_card_set.card_set.first()

        if self == first_card_in_set:
            return self.parent_card_set.card_set.last()
        else:
            return self.parent_card_set.card_set.filter(id__lt = self.id).last()


    def is_there_a_next_card(self):
        last_card_in_set = self.parent_card_set.card_set.last()
        if self == last_card_in_set:
            return False
        else:
            return True


    def get_next_card(self):
        last_card_in_set = self.parent_card_set.card_set.last()
        if self == last_card_in_set:
            return self.parent_card_set.card_set.first()
        else:
            return self.parent_card_set.card_set.filter(id__gt = self.id).first()


from django.db import models
import random 

# Create your models here.
class Person(models.Model):
    '''encapsulate the idea of a person'''

    name = models.TextField(blank = False)

    def ___str___(self):
        '''return a string representation of this person.'''
        return self.name 
    
    #get an image at random 
    def get_random_image(self):
        '''return an image of this person, chosen at random.'''

        #get all images of this person 
        images = Image.objects.filter(person=self.pk)

        #then, pick one at random , and return that one 

        i = random.randint(0,len(images)-1)
        return images[i]

    #get all images for this person 
    def get_all_images(self):
        '''return a QuerySet of all images for this person.'''

        # get all images of this person 
        images = Image.objects.filter(person = self.pk)
        return images 

    #get all quotes for this person 
    def get_all_quotes(self):
        '''return a QuerySet of all images for this person.'''

        # get all quotes of this person 
        quotes = Quote.objects.filter(person = self.pk)
        return quotes


class Quote(models.Model):
    '''Encapsulate the idea of a quote.'''

    #data attributes of a quote: 
    text = models.TextField(blank = True)
    person = models.ForeignKey('Person', on_delete="CASCADE")

    def ___str___(self):
        '''return a string representation of this object.'''
        return '"%s" - %s' % (self.text, self.person.name)

class Image(models.Model):
    '''represent an image, which is associated with a person.'''

    image_url = models.URLField(blank = True)
    person = models.ForeignKey('Person', on_delete = "CASCADE")

    def ___str___(self):
        '''return a string representation of this object.'''
        return self.image_url
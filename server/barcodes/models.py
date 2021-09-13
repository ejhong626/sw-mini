from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    carbohydrate = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorie = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
    quantity = models.IntegerField(default=100, null=True, blank=True)

class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='recipe', on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Item)
    # Look into key to reference other Items

class Log(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='log', on_delete=models.CASCADE)
    data = models.ManyToManyField(Item)

#
# class AppUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(
#         'auth.User', related_name='users', on_delete=models.CASCADE)

# from pygments import highlight
# from pygments.lexers import get_all_lexers, get_lexer_by_name
# from pygments.styles import get_all_styles
# from pygments.formatters.html import HtmlFormatter

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# class Barcode(models.Model):
#     created = models.DateTimeField(auto_now_add = True)
#     title = models.CharField(max_length = 100, blank = True, default = '')
#     code = models.TextField()
#     linenos = models.BooleanField(default = False)
#     language = models.CharField(choices = LANGUAGE_CHOICES, default = 'python', max_length = 100)
#     style = models.CharField(choices = STYLE_CHOICES, default = 'friendly', max_length = 100)
#     owner = models.ForeignKey('auth.User', related_name = 'barcodes', on_delete = models.CASCADE)
#     highlighted = models.TextField()
#
#     def save(self, *args, **kwargs):
#         """
#         Use the `pygments` library to create a highlighted HTML
#         representation of the code barcode.
#         """
#         lexer = get_lexer_by_name(self.language)
#         linenos = 'table' if self.linenos else False
#         options = {'title': self.title} if self.title else {}
#         formatter = HtmlFormatter(style = self.style, linenos = linenos,
#                                   full = True, **options)
#         self.highlighted = highlight(self.code, lexer, formatter)
#         super(Barcode, self).save(*args, **kwargs)
#
#     class Meta:
#         ordering = ['created']

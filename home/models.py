from django.db import models

# Create your models here.
# database -----> excel workbook
# table ----------> excel sheet
class Contact(models.Model):
    sno = models.AutoField(primary_key= True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=45)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'Message from '+ self.name + ' - '+self.email
    
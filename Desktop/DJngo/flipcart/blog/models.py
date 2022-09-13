from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=60)
    head1=models.CharField(max_length=50, default="")
    head1_cont=models.CharField(max_length=3000,default="")
    sub_head2=models.CharField(max_length=300,default="")
    shead2_cont=models.CharField(max_length=3000,default="")
    sub_head3=models.CharField(max_length=300,default="")
    shead3_cont=models.CharField(max_length=3000,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

def __str__(self):
    return self.title


from django.db import models

# Create your models here.

class product(models.Model):

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    product_price = models.IntegerField(default=0)
    product_category = models.CharField(max_length=50, default="")
    product_subcategory = models.CharField(max_length=50, default="")
    product_image = models.ImageField(upload_to="shop/images", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name

class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=70, default="")
    user_adddres = models.CharField(max_length=50,)
    user_phone = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.user_name

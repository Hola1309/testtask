from django.db import models

# Create your models here.
# class Datatest(models.Model):
#     field1 = models.TextField(blank=True, null=True)
#     field2 = models.TextField(blank=True, null=True)
#     field3 = models.TextField(blank=True, null=True)
#     field4 = models.TextField(blank=True, null=True)
#     field5 = models.TextField(blank=True, null=True)
#     field6 = models.TextField(blank=True, null=True)
#     field7 = models.TextField(blank=True, null=True)
#     field8 = models.TextField(blank=True, null=True)
#     field9 = models.TextField(blank=True, null=True)
#     field10 = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'datatest'
 # rec = {'code':a[0], 'Name':a[1], 'Lvl1':a[2], 'Lvl2':a[3], 'Lvl3':a[4], 'Cost':a[5], 'CostSP':a[6], 'Count':a[7], 'FieldProp':a[8], 'Purch':a[9], 'Unit':a[10],'Img':a[11], 'Display':a[12],'Desc':a[13]}
class Csv(models.Model):
    
    code = models.TextField(blank=True, null=True)
    Name = models.TextField(blank=True, null=True)
    Lvl1 = models.TextField(blank=True, null=True)
    Lvl2 = models.TextField(blank=True, null=True)
    Lvl3 = models.TextField(blank=True, null=True)
    Cost = models.TextField(blank=True, null=True)
    CostSP = models.TextField(blank=True, null=True)
    Count = models.TextField(blank=True, null=True)
    FieldProp = models.TextField(blank=True, null=True)
    Purch = models.TextField(blank=True, null=True)
    Unit = models.TextField(blank=True, null=True)
    Img = models.TextField(blank=True, null=True)
    Display = models.TextField(blank=True, null=True)
    Desc = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.code
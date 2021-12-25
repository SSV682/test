from django.db import models


# Профиль
class News(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=256,db_index=True, blank=True, null=True)
    date = models.DateField()
    content = models.TextField(blank=True,null=True)


    class Meta:
        ordering=('date',)

    def __str__(self):
        return '{} {}'.format(self.subject)


    


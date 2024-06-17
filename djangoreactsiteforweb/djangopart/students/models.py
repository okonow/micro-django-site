from django.db import models

class Student(models.Model):
    name = models.CharField("Name", max_length=32)
    b_date = models.DateField()
    study_type = models.CharField("StudyType", max_length=16)
    

    def __str__(self):
        return self.name    
from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=20)
    course_duration = models.IntegerField()
    student = models.ManyToManyField('Students')
    mentor = models.ForeignKey('Mentors', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(max_length=25)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Mentors(models.Model):
    fullname = models.CharField(max_length=25)
    experience = models.IntegerField()

    def __str__(self):
        return self.fullname

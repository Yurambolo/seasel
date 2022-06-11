from django.db import models
from authorize.models import MusicSchool, User


class Semester(models.Model):
    music_school = models.ForeignKey(MusicSchool, models.CASCADE)
    number = models.IntegerField(unique=True)
    composition_count = models.IntegerField()
    min_difficulty = models.IntegerField()
    max_difficulty = models.IntegerField()

    def __str__(self):
        return str(self.number)


class Instrument(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Concert(models.Model):
    music_school = models.ForeignKey(MusicSchool, models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)


class Composition(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.ForeignKey(Instrument, models.CASCADE)
    author = models.CharField(max_length=100)
    difficulty = models.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.author, self.name)


class CompositionRepresentation(models.Model):
    composition = models.ForeignKey(Composition, models.CASCADE)
    format = models.CharField(max_length=100)
    sheme = models.JSONField()

    def __str__(self):
        return '{0} {1}'.format(str(self.composition), self.format)


class Course(models.Model):
    student = models.ForeignKey(User, models.CASCADE)
    teacher = models.ForeignKey(User, models.CASCADE, related_name='teacher')
    semester = models.ForeignKey(Semester, models.CASCADE)
    instrument = models.ForeignKey(Instrument, models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(str(self.student), str(self.instrument))


class Program(models.Model):
    concert = models.ForeignKey(Concert, models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)
    semester = models.ForeignKey(Semester, models.CASCADE)
    compositions = models.ManyToManyField(Composition, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(str(self.concert), str(self.course))


class Repetition(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    composition = models.ForeignKey(Composition, models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    mark = models.IntegerField()

    def __str__(self):
        return '{0} {1} {2}'.format(str(self.course), str(self.composition), str(self.datetime))


class Feedback(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    composition = models.ForeignKey(Composition, models.CASCADE)
    mark = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} {1}'.format(str(self.mark), self.comment or '')

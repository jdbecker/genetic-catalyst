from django.db import models


class Creature(models.Model):
    pass


class Gene(models.Model):
    creature = models.ForeignKey(Creature, on_delete=models.CASCADE)


class Allele(models.Model):
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)


class Attribute(models.Model):
    allele = models.ForeignKey(Allele, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.IntegerField()

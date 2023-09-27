from django.db import models


class CreatureModel(models.Model):
    @property
    def genes(self) -> tuple["GeneModel"]:
        """convenience method to access child genes"""
        return tuple(self.genemodel_set.all())  # type: ignore # pylint: disable=no-member


class GeneModel(models.Model):
    creature = models.ForeignKey(CreatureModel, on_delete=models.CASCADE)

    @property
    def alleles(self) -> tuple["AlleleModel", "AlleleModel"]:
        """convenience method to access child alleles"""
        return tuple(self.allelemodel_set.all()[:2])  # type: ignore # pylint: disable=no-member


class AlleleModel(models.Model):
    gene = models.ForeignKey(GeneModel, on_delete=models.CASCADE)

    @property
    def attributes(self) -> set["AttributeModel"]:
        """convenience method to access child attributes"""
        return set(self.attributemodel_set.all())  # type: ignore # pylint: disable=no-member


class AttributeModel(models.Model):
    allele = models.ForeignKey(AlleleModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.IntegerField()

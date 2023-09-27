from django.test import TestCase
from creatures.allele import Allele, allele_from_model
from creatures.attribute import Attribute, attribute_from_model
from creatures.gene import Gene, gene_from_model

from creatures.models import CreatureModel
from creatures.creature import creature_from_model, new_creature


class CreatureModelTests(TestCase):
    def get_model_creature(self) -> CreatureModel:
        creature = new_creature()
        return creature.save()

    def test_saved_attributes_match(self):
        model_creature = self.get_model_creature()
        allele = model_creature.genes[0].alleles[0]
        attribute = Attribute("COOL_ATTR", 77)
        attribute_model = attribute.save(allele)
        self.assertEqual(attribute, attribute_from_model(attribute_model))

    def test_saved_alleles_match(self):
        model_creature = self.get_model_creature()
        gene = model_creature.genes[0]
        allele = Allele({Attribute("COOL_ATTR", 77)})
        allele_model = allele.save(gene)
        self.assertEqual(allele, allele_from_model(allele_model))

    def test_saved_genes_match(self):
        model_creature = self.get_model_creature()
        creature = new_creature()
        gene = Gene(creature.genes[0].alleles[0], creature.genes[0].alleles[1])
        gene_model = gene.save(model_creature)
        self.assertEqual(gene, gene_from_model(gene_model))

    def test_creature_model_saves_correctly(self):
        creature = new_creature()
        creature_model = creature.save()
        creatureFromModel = creature_from_model(creature_model)
        self.assertEqual(creature, creatureFromModel)
        self.assertEqual(creature.strength, creatureFromModel.strength)
        self.assertEqual(creature.intelligence, creatureFromModel.intelligence)
        self.assertEqual(creature.cunning, creatureFromModel.cunning)
        self.assertEqual(creature.bandwidth, creatureFromModel.bandwidth)
        self.assertEqual(creature.perception, creatureFromModel.perception)
        self.assertEqual(creature.harvesting, creatureFromModel.harvesting)
        self.assertEqual(creature.absorption, creatureFromModel.absorption)

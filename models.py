from django.db import models
import os, os.path
import sys
import glob






class WigFile(models.Model):

	

    SPECIES_CHOICES = [('Hs', 'Homo sapiens'), ('Dm','Drosophila melanogaster')]
    MODIFICATION_CHOICES = [('yes', 'Yes'), ('nomodification', 'No modification'), ('h1hesc', 'H1hESC'), ('tier1', 'Tier 1'), ('tier2', 'Tier 2'), ('tier12', 'Tier 1 + Tier 2')]
    KMERS_CHOICES = [('yes', 'Yes'), ('no', 'No')]
    SPECIFIC_TISSUE = [('both', 'Heart + Brain'), ('brain', 'Brain'), ('heart', 'Heart'), ('positives', 'Positives'), ('brain2steps', 'Brain, 2 steps'), ('heart2steps', 'Heart, 2 steps') ]
    DATABASE = [('vista', 'vista'), ('fantom', 'fantom'), ('fly', 'fly')]

    species = models.CharField(max_length=2, choices=SPECIES_CHOICES)

    frame=models.IntegerField(default=0)
    step=models.IntegerField(default=0)
    chr_name=models.CharField(max_length=5, default='chrN')
    kmers = specific_tissue = models.CharField(max_length=15, choices=KMERS_CHOICES, default='no')
    modification=models.CharField(max_length=25, choices=MODIFICATION_CHOICES, default='no')
    specific_tissue = models.CharField(max_length=15, choices=SPECIFIC_TISSUE, default='no')
    database=models.CharField(max_length=15, choices=DATABASE)


    file_path=models.CharField(max_length=200, default='empty')
    file_static_path=models.CharField(max_length=200, default='empty')


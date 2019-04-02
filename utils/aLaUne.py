import random
import os
import sys
import django

sys.path.append("/repertoire_mediation_musique")
os.environ["DJANGO_SETTINGS_MODULE"] = "multimedia.settings"
from django.conf import settings
from bdmultimedia.models import Outil

utilises = [36, 211, 198, 215, 155, 86, 105, 27, 161, 173, 243, 146, 118,
            71, 38, 121, 72, 91, 145, 195, 55, 111, 75, 101, 206, 163, 74,
            189, 85, 128, 13, 217, 176, 106, 177, 73, 63, 122, 115, 88, 19,
            102, 70, 156, 68, 69, 33, 39, 2, 11, 46, 108, 30, 154, 80, 41,
            118, 59, 18, 79, 92, 162, 125, 100]

dispo = []

for i in Outil.objects.all():
    if i not in utilises:
        dispo.append(i.pk)

random.shuffle(dispo)

print(dispo[0])
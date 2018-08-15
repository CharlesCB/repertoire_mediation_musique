# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from bdmultimedia.models import *

# Register your models here.


class OutilAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    search_fields = ['titre']
    # filter_horizontal = ('producteur_type','producteur_nom','support_diffusion','format','forme_narrative','orchestration',
    #                      'structure','language_musical','genre_musical','style_musical', 'experience_musicale',
    #                      'contexte', 'role_evolution', 'sollicitation_musicale', 'sollicitation_generale',
    #                      'evocation_graphique', 'evocation_plastique', 'evocation_autre',
    #                       'exemples_notions_interdisciplinaires', 'role_humain_homme', 'role_humain_femme', 'role_humain_neutre',
    #                      'role_pers_anime_homme', 'role_pers_anime_femme', 'role_pers_anime_neutre',
    #                      'role_animaux_homme', 'role_animaux_femme', 'role_animaux_neutre',
    #                      'role_instr_anime_homme', 'role_instr_anime_femme', 'role_instr_anime_neutre',
    #                      'mode_hebergement', 'mode_consultation', 'narration_langue', 'sous_titre')


# class ContreExempleAdmin(admin.ModelAdmin):
#     list_display = ('titre',)
#     search_fields = ['titre',]


# class CustomTestAdmin(admin.ModelAdmin):
#     list_display = ('date',)
#     search_fields = ['date',]


class ProdTypeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class ProducteurNomAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]
    ordering = ['nom', ]


class SupportDiffusionAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class FormatOutilAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class FormeNarrativeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class ModeHebergementAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class ModeConsultationAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class LangueNarrationAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class SousTitreAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class OrchestrationAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]
    ordering = ['nom']


class StructureAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]
    ordering = ['nom']


class LanguageMusicalAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]
    ordering = ['nom']


class GenreMusicalAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]
    ordering = ['nom']


class StyleMusicalAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]
    ordering = ['nom']


class ExperienceMusicaleAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]
    ordering = ['nom']


class ContexteAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class RoleEvolutionAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class OrganologieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom']


class SollicitationMusicaleAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class SollicitationGeneraleAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class EvocationGraphiqueAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]


class EvocationPlastiqueAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]


class EvocationAutreAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]


class RoleHommeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]


class RoleFemmeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]

class RoleHumainNeutreAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]
    
    
class RolePersAnimHommeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]


class RolePersAnimFemmeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]

class RolePersAnimNeutreAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]
    
    
class RoleAnimauxHommeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]


class RoleAnimauxFemmeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]

class RoleAnimauxNeutreAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]
    
class RoleInstrHommeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]


class RoleInstrFemmeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]

class RoleInstrNeutreAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', ]

class NotionsInterAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]



#admin.site.register(CustomTest, CustomTestAdmin)

admin.site.register(Outil, OutilAdmin)
#admin.site.register(ContreExemple, ContreExempleAdmin)
admin.site.register(ProdType, ProdTypeAdmin)
admin.site.register(SupportDiffusion,SupportDiffusionAdmin)
admin.site.register(ProducteurNom,ProducteurNomAdmin)
admin.site.register(FormatOutil,FormatOutilAdmin)
admin.site.register(FormeNarrative,FormeNarrativeAdmin)
admin.site.register(ModeHebergement,ModeHebergementAdmin)
admin.site.register(ModeConsultation,ModeConsultationAdmin)
admin.site.register(LangueNarration,LangueNarrationAdmin)
admin.site.register(SousTitre, SousTitreAdmin)
admin.site.register(Orchestration, OrchestrationAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(LanguageMusical, LanguageMusicalAdmin)
admin.site.register(GenreMusical, GenreMusicalAdmin)
admin.site.register(StyleMusical,StyleMusicalAdmin)
admin.site.register(ExperienceMusicale, ExperienceMusicaleAdmin)
admin.site.register(Contexte,ContexteAdmin)
admin.site.register(RoleEvolution, RoleEvolutionAdmin)
admin.site.register(Organologie, OrganologieAdmin)
admin.site.register(SollicitationMusicale, SollicitationMusicaleAdmin)
admin.site.register(SollicitationGenerale,SollicitationGeneraleAdmin)
admin.site.register(EvocationGraphique, EvocationGraphiqueAdmin)
admin.site.register(EvocationPlastique, EvocationPlastiqueAdmin)
admin.site.register(EvocationAutre,EvocationAutreAdmin)
admin.site.register(RoleHomme,RoleHommeAdmin)
admin.site.register(RoleFemmes,RoleFemmeAdmin)
admin.site.register(RoleHumainNeutre,RoleHumainNeutreAdmin)
admin.site.register(RolePersAnimHomme,RolePersAnimHommeAdmin)
admin.site.register(RolePersAnimFemmes,RolePersAnimFemmeAdmin)
admin.site.register(RolePersAnimNeutre,RolePersAnimNeutreAdmin)
admin.site.register(RoleAnimauxHomme,RoleAnimauxHommeAdmin)
admin.site.register(RoleAnimauxFemmes,RoleAnimauxFemmeAdmin)
admin.site.register(RoleAnimauxNeutre,RoleAnimauxNeutreAdmin)
admin.site.register(RoleInstrHomme,RoleInstrHommeAdmin)
admin.site.register(RoleInstrFemmes,RoleInstrFemmeAdmin)
admin.site.register(RoleInstrNeutre,RoleInstrNeutreAdmin)

admin.site.register(NotionsInter, NotionsInterAdmin)
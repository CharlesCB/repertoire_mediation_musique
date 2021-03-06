# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0018_auto_20170613_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemmus',
            name='nom',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='elemsocio',
            name='nom',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='expmus',
            name='nom',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='notionsinter',
            name='nom',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='outil',
            name='audiodescription',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ("Ne s'applique pas", "Ne s'applique pas")], max_length=200, verbose_name='Audiodescription (mal voyants)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='duree',
            field=models.CharField(default='00:00:00', max_length=8, verbose_name='Dur\xe9e (hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='elements_socio',
            field=models.CharField(choices=[('Non', 'Non'), ('Vie du compositeur, interpr\xe8te, d\xe9dica\xe7aire, m\xe9c\xe8ne', 'Vie du compositeur, interpr\xe8te, d\xe9dica\xe7aire, m\xe9c\xe8ne'), ('Organologie', 'Organologie'), ('Lutherie', 'Lutherie'), ('\xc9volution de la profession', '\xc9volution de la profession'), ('Conventions', 'Conventions'), ('Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)', 'Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)'), ('Oeuvres (\xe0 titre documentaires)', 'Oeuvres (\xe0 titre documentaires)'), ('Contexte de production', 'Contexte de production'), ('Contexte de r\xe9ception', 'Contexte de r\xe9ception'), ('Contexte de cr\xe9ation (au sens de "la premi\xe8re")', 'Contexte de cr\xe9ation (au sens de "la premi\xe8re")'), ('Autre', 'Autre')], max_length=200, verbose_name='El\xe9ments socioculturels et historiques'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocaion_litteraire',
            field=models.CharField(choices=[('Non', 'Non'), ('Texte oral', 'Texte oral'), ('Texte \xe9crit', 'Texte \xe9crit'), ('Autre', 'Autre')], max_length=200, verbose_name='\xc9vocation litt\xe9raire'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocaion_plastique',
            field=models.CharField(choices=[('Non', 'Non'), ('Sculpture', 'Sculpture'), ('Installation', 'Instalation'), ('Autre', 'Autre')], max_length=200, verbose_name='\xc9vocation plastique'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocation_autre',
            field=models.CharField(choices=[('Aucune', 'Aucune'), ('Litt\xe9rature', 'Litt\xe9rature'), ('Danse', 'Danse'), ('Art plastiques', 'Art plastiques'), ('Th\xe9\xe2tre', 'Th\xe9\xe2tre'), ('Cin\xe9ma', 'Cin\xe9ma'), ('Arts num\xe9riques', 'Arts num\xe9riques'), ('Sports', 'Sports'), ('Neurosciences', 'Neurosciences'), ('Sciences physiques', 'Sciences physiques'), ('Architechture', 'Architechture'), ('Gastronomie', 'Gastronomie'), ('Cirque', 'Cirque'), ('Performance', 'Performance'), ('Anatomie', 'Anatomie'), ('Autre', 'Autre')], max_length=200, verbose_name='Autres disciplines \xe9voqu\xe9es'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocation_graphique',
            field=models.CharField(choices=[('Non', 'Non'), ('Repr\xe9sentation graphique traditionnelle (partition + notes)', 'Repr\xe9sentation graphique traditionnelle (partition + notes)'), ("Repr\xe9sentation graphique traditionnelle augment\xe9e (Ex. les notes s'\xe9clairent quand on les entends", "Repr\xe9sentation graphique traditionnelle augment\xe9e (Ex. les notes s'\xe9clairent quand on les entends"), ('Repr\xe9sentation graphique traditionelle illustr\xe9e (Ex. les notes sont en fait des oiseaux sur les lignes de la port\xe9e)', 'Repr\xe9sentation graphique traditionelle illustr\xe9e (Ex. les notes sont en fait des oiseaux sur les lignes de la port\xe9e)'), ('Repr\xe9sentation graphique sch\xe9matis\xe9e (Ex. il y toujours un port\xe9e mais ce sont des courbes qui figurent la m\xe9lodie)', 'Repr\xe9sentation graphique sch\xe9matis\xe9e (Ex. il y toujours un port\xe9e mais ce sont des courbes qui figurent la m\xe9lodie)'), ('Repr\xe9sentation graphique symbolis\xe9e (Ex. des images anim\xe9es, cf. ratatouille!!)', 'Repr\xe9sentation graphique symbolis\xe9e (Ex. des images anim\xe9es, cf. ratatouille!!)'), ('Autre', 'Autre')], max_length=200, verbose_name='\xc9vocation graphique'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='experiences_musicales',
            field=models.CharField(choices=[('Non', 'Non'), ("Techniques d'\xe9coute", "Techniques d'\xe9coute"), ('Exp\xe9rience v\xe9cue', 'Exp\xe9rience v\xe9cue'), ('Le concert', 'Le concert'), ('Les r\xe9p\xe9titions (g\xe9n\xe9rale, raccord, etc.)', 'Les r\xe9p\xe9titions (g\xe9n\xe9rale, raccord, etc.)'), ('Autre', 'Autre')], max_length=200),
        ),
        migrations.AlterField(
            model_name='outil',
            name='format',
            field=models.CharField(choices=[('Ecrit (texte, dessin)', 'Ecrit (texte, dessin)'), ('Audio', 'Audio'), ('Audiovisuel', 'Audiovisuel'), ('Immersif', 'Immersif'), ('R\xe9alit\xe9 augment\xe9e', 'R\xe9alit\xe9 augment\xe9e'), ('Autre', 'Autre')], max_length=200, verbose_name="Format de l'outil"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='forme_narrative',
            field=models.CharField(choices=[('Entrevue', 'Entrevue'), ('Fiction', 'Fiction'), ("Synopsis (r\xe9cit fid\xe8le au programme de l'oeuvre)", "Synopsis (r\xe9cit fid\xe8le au programme de l'oeuvre)"), ('Web-s\xe9rie (plusieurs occurences qui ont un lien entre elles)', 'Web-s\xe9rie (plusieurs occurences qui ont un lien entre elles)'), ('Animation', 'Animation'), ('Art et essai', 'Art et essai'), ('Vulgarisation', 'Vulgarisation'), ('Creative commons (sur le mod\xe8le wiki)', 'Creative commons (sur le mod\xe8le wiki)'), ('Reportage', 'Reportage'), ('Jeu', 'Jeu'), ('Autre', 'Autre')], max_length=200, verbose_name='Forme narrative g\xe9n\xe9rale'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='interface_type',
            field=models.CharField(choices=[('Collaborative', 'Collaborative'), ('Interactive', 'Interactive'), ('Neutre', 'Neutre')], max_length=200, verbose_name="Type d'interface"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='language_des_signes',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ("Ne s'applique pas", "Ne s'applique pas")], max_length=200, verbose_name='Language des signes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='malentendants',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ("Ne s'applique pas", "Ne s'applique pas")], max_length=200, verbose_name='Sous titrage malentendants'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='materiau_musical',
            field=models.CharField(choices=[('Non', 'Non'), ('Son', 'Son'), ('Structure', 'Structure'), ('Language musical', 'Language musical'), ('Genre (op\xe9ra, symphonique)', 'Genre (op\xe9ra, symphonique)'), ('Style (Classique, Romantique, Contemporain)', 'Style (Classique, Romantique, Contemporain)'), ('Autre', 'Autre')], max_length=200, verbose_name='Mat\xe9riau musical'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='mode_hebergement',
            field=models.CharField(choices=[('Youtube / Vimeo, etc..', 'Youtube / Vimeo, etc..'), ('Portail institutionnel', 'Portail institutionnel'), ('R\xe9seau social', 'R\xe9seau social'), ('Cloud', 'Cloud'), ('Autre', 'Autre')], max_length=200, verbose_name="Mode d'h\xe9bergement sur la toile"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='narration_langue',
            field=models.CharField(choices=[('Fran\xe7ais', 'Fran\xe7ais'), ('Anglais', 'Anglais'), ('Allemand', 'Allemand'), ('Portugais', 'Portugais'), ('Autre', 'Autre')], max_length=200, verbose_name='Langue de la narration'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='notion_concepts',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], max_length=200, verbose_name='Concepts (luminosit\xe9, transparence)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='notion_experiences',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], max_length=200, verbose_name='Exp\xe9rience (\xe9motions)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='notion_pratique',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], max_length=200, verbose_name='Pratique (processus de cr\xe9ation)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='pratique_musicale',
            field=models.CharField(choices=[('Non', 'Non'), ('Techniques instrumentales (mode de production du son)', 'Techniques instrumentales (mode de production du son)'), ("Activit\xe9 du musicien, du compositeur, de l'interpr\xe8te, du luthier etc.", "Activit\xe9 du musicien, du compositeur, de l'interpr\xe8te, du luthier etc."), ('Pratique professionnelle', 'Pratique professionnelle'), ('Pratique amateur', 'Pratique amateur'), ('Autre', 'Autre')], max_length=200, verbose_name='Pratique musicale'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='producteur_nom',
            field=models.CharField(max_length=200, verbose_name='Pr\xe9ciser le nom complet du producteur'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='producteur_type',
            field=models.CharField(choices=[('Particulier', 'Particulier'), ('Organisme de diffusion (OSM, Festival)', 'Organisme de diffusion (OSM, Festival)'), ('Organisme de formation professionnelle (CQM, ARIAM, CFMI)', 'Organisme de formation professionnelle (CQM, ARIAM, CFMI)'), ('Groupe de recherche (P2M, Groupe de recherche sur la m\xe9diation culturelle)', 'Groupe de recherche (P2M, Groupe de recherche sur la m\xe9diation culturelle)'), ('Organismes \xe9ducatif (Ecole de musique, TEDX)', 'Organismes \xe9ducatif (Ecole de musique, TEDX)'), ('Autre', 'Autre')], max_length=200, verbose_name='Producteurs'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_animaux_femme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des animaux femelles'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_animaux_homme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des animaux m\xe2les'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_animaux_neutre',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des animaux neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_humain_femme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des femmes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_humain_homme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des hommes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_humain_neutre',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_instr_anime_femme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des instruments anthropomorphes f\xe9minins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_instr_anime_homme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des instruments anthropomorphes masculins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_instr_anime_neutre',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des instruments anthropomorphes neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_obj_anime_femme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des objets anthropomorphes f\xe9minins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_obj_anime_homme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des objets anthropomorphes masculins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_obj_anime_neutre',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des objets anthropomorphes neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_anime_femme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des personnages anim\xe9s femmes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_anime_homme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des personnages anim\xe9s hommes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_anime_neutre',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des personnages anim\xe9s neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_fictif_femme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des personnages fictifs f\xe9minins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_fictif_homme',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des personnages fictifs masculins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_fictif_neutre',
            field=models.CharField(max_length=200, verbose_name='R\xf4le des personnages fictifs neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='site',
            field=models.URLField(verbose_name="Chemin d'acc\xe8s au site d'h\xe9bergement"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='solicitation_autre',
            field=models.CharField(choices=[('Lire', 'Lire'), ('Regarder', 'Regarder'), ('Bricoler', 'Bricoler'), ('Jouer (au sens ludique)', 'Jouer (au sens ludique)'), ('\xc9crire', '\xc9crire'), ('Autre', 'Autre')], max_length=200, verbose_name="En g\xe9n\xe9ral (hors musique) comment sollicite-t-on l'usager?"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='solicitation_musicale',
            field=models.CharField(choices=[('Interpr\xe9ter', 'Interpr\xe9ter'), ('Reproduire', 'Reproduire'), ('\xc9couter', '\xc9couter'), ('Inventer/composer/improviser', 'Inventer/composer/improviser'), ('Lire', 'Lire'), ('Regarder', 'Regarder'), ('Autre', 'Autre')], max_length=200, verbose_name="Comment sollicite-t-on musicalement l'usager?"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='sonore_valeur',
            field=models.CharField(choices=[('Premier plan', 'Premier Plan'), ('Arri\xe8re plan', 'Arri\xe8re plan'), ('Alternance', 'Alternance'), ('Aucune', 'Aucune'), ('Autre', 'Autre')], max_length=200, verbose_name='Mise en valeur du sonore'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='sous_titre',
            field=models.CharField(choices=[('Pas de sous titrage', 'Pas de sous titrage'), ('Fran\xe7ais', 'Fran\xe7ais'), ('Anglais', 'Anglais'), ('Allemand', 'Allemand'), ('Portugais', 'Portugais'), ('Autre', 'Autre')], max_length=200, verbose_name='Sous-titrage'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='support_diffusion',
            field=models.CharField(choices=[('Ordinateur', 'Ordinateur'), ('Smartphone', 'Smartphone'), ('Tablette', 'Tablette'), ('Lunettes 3D', 'Lunettes 3D'), ('Consoles de JV', 'Consoles de JV'), ('DVD', 'DVD'), ('CD', 'CD'), ('Autre', 'Autre')], max_length=200, verbose_name='Support de diffusion'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='temps_mus',
            field=models.CharField(default='00:00:00', max_length=8, verbose_name='Temps de musique seule (hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='temps_mus_par',
            field=models.CharField(default='00:00:00', max_length=8, verbose_name='Temps de parole et musique superpos\xe9es (hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='temps_par',
            field=models.CharField(default='00:00:00', max_length=8, verbose_name='Temps de parole seule (hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='titre',
            field=models.CharField(max_length=200, unique=True, verbose_name="Titre de l'outil"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='url',
            field=models.URLField(verbose_name="Chemin d'acc\xe8s direct (c\xe0d quand on a fini de parcourir le site)"),
        ),
        migrations.AlterField(
            model_name='pratmus',
            name='nom',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

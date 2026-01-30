
# Ces lignes doivent être tout en haut, SANS espaces devant
define s = Character("Sam", color="#00aaff")
define m = Character("Max", color="#ff0055")
define t = Character("Trixie", color='#FFD1DC')
define j = Character("Juge", color='#5FF43E')
define b = Character("Bruno", color='#ff8000')
define p = Character("Purple Tentacle", color='#FFA1DC')
define g = Character("Green Tentacle", color='#FFF1DC')
define f = Character("Flambée", color='#AAF1DC')
define l = Character("Lee Harvey", color='#BBF1DC')
define c = Character("Conroy Bumpus", color='#DAF1DC')
define d = Character("DÉPOSITION DE FLAMBÉ", color='#DAF1DC')
define n = Character("narrateur", color='#DAF1DC')

# Variables pour suivre les indices découverts
default indice_ticket = False
default indice_costume = False
default indice_sauce = False
default indice_poils = False
default confiance_bruno = 0

image bureau_small = im.Scale("bureau.png", 900, 600)
image brunoprison_small = im.Scale("brunoprison.png", 900, 600)
image crimescenes_small = im.Scale("crimescenes.png", 900, 600)
image maison_small = im.Scale("maison.jpg", 900, 600)
image lapinporte_small = im.Scale("lapinporte.png", 900, 600)

# Le Juge et le Tribunal
image grandjudge_small = im.Scale("grandjudge.jpg", 900, 600)
image grandjugeshoked_small = im.Scale("grandjugeshoked.jpg", 900, 600)
image marto_small = im.Scale("marto.jpg", 900, 600)

# Personnages (Sprites)
image samnormal_small = im.Scale("samnormal.png", 900, 600)
image objectionsam_small = im.Scale("objectionsam.png", 900, 600)
image tentaclenormal_small = im.Scale("tentaclenormal.png", 900, 600)
image tentacleobjection_small = im.Scale("tentacleobjection.png", 900, 600)

# Les Témoins à la barre
image flambebar_small = im.Scale("flambebar.png", 900, 600)
image leebar_small = im.Scale("leebar.png", 900, 600)
image bumpusbar_small = im.Scale("bumpusbar.png", 900, 600)
image noncoupable_small = im.Scale("noncoupable.jpg", 900, 600)
image porteouvert_small = im.Scale("porteouvert.png", 900, 600)


# Indices / Objets
image lapincostume_small = im.Scale("lapincostume.png", 1200, 600)
image lapinparle_small = im.Scale("lapinparle.png", 1200, 600)

label start:
#1------------
    play music "sound/Ambiance Tribunal Tendu.mp3"
    scene bureau_small
    s "Le téléphone sonne, Max. C'est soit un client désespéré, soit le fisc qui a enfin trouvé notre cachette sous le stand de hot-dogs."

    menu choix_telephone:
        "Que fait Max ?"

        "Répondre poliment":
            m "Allô, Police Freelance, comment puis-je vous aider aujourd'hui ?"
            s "Max... tu es malade ?"
            $ confiance_bruno += 1

        "Répondre de manière chaotique":
            m "BONJOUR C'EST LA HOTLINE DES EXPLOSIFS ARTISANAUX !"
            s "Max, on va perdre ce client..."

    s "(Décroche) Police Freelance, j'écoute. Si c'est pour l'abonnement aux bibles illustrées, mon partenaire est déjà possédé. ... Trixie ?"
    t "Sam ! C'est affreux ! Bruno est derrière les barreaux ! Ils disent qu'il a fait une chose terrible !"

    menu choix_reponse_trixie:
        "Comment réagir ?"

        "Rassurer Trixie calmement":
            s "Calme-toi, ma belle. On arrive plus vite qu'un avocat après une ambulance."
            $ confiance_bruno += 2
            t "Merci Sam... je savais que je pouvais compter sur vous !"

        "Faire une blague inappropriée":
            m "Ne t'inquiète pas ! En prison, Bruno pourra enfin avoir une manucure gratuite !"
            t "MAX ! Ce n'est pas drôle !"
            s "On arrive, Trixie. Ignore mon partenaire."

    s "Max, range ta scie sauteuse, on a un Bigfoot à sortir du pétrin."

#2------------
    scene brunoprison_small
    b "(Sanglotant) Je vous jure, Sam... j'étais au concert avec Trixie ! On chantait 'L'amour au bord du goudron' !"
    m "Respire, Bruno. Ton haleine de sapin renversé fait fondre le plexiglas."

    menu interrogation_bruno:
        "Que demander à Bruno ?"

        "Parle-moi du concert":
            b "C'était magique ! Trixie et moi, on a chanté toute la soirée. J'ai même gardé le ticket !"
            s "Le ticket pourrait être utile. Continue."
            $ confiance_bruno += 1

        "Qu'as-tu vu exactement sur la scène de crime ?":
            b "Les Frères Kushman... figés. J'ai voulu vérifier s'ils respiraient encore..."
            m "Grave erreur tactique, mon ami poilu !"
            $ indice_poils = True

        "As-tu des ennemis ?":
            b "Moi ? Non ! Enfin... il y a eu cette histoire avec Conroy Bumpus en 1998, mais c'était juste une mouche..."
            s "Une mouche ? Explique."
            b "Sa mouche de compagnie est morte dans mon restaurant. Un accident ! Mais il a juré de se venger..."

    b "Le procès commence dans deux heures ! Je ne veux pas finir en tapis de sol, Sam !"
    s "On va te sortir de là, Bruno. Promis."

#3------------
    play music "sound/Ambiance Tribunal Tendu second song.mp3"
    scene grandjudge_small
    j "L'audience est ouverte. La défense est-elle prête ?"
    s "Aussi prête qu'un caniche dans un mixeur, Monsieur le Juge."

    play sound "sound/objection.mp3"
    show objection at left
    scene tentacleobjection_small
    p "Objection !"
    hide objection
    p "Cette affaire est plus simple qu'un plan de domination mondiale ! Le corps a été retrouvé couvert de poils de Bigfoot, des empreintes géantes partout, et un ticket de concert. Coupable !"
    g "C'est mathématique, Maître."

    menu choix_defense:
        "Comment réagir à l'accusation ?"

        "Demander à examiner les preuves":
            show objection at right
            play sound "sound/objection.mp3"
            scene objectionsam_small
            s "OBJECTION ! Ces preuves n'ont pas été examinées correctement !"
            hide objection
            $ confiance_bruno += 2

        "Faire une diversion avec Max":
            m "OBJECTION ! On n'a même pas eu le temps de renifler les indices !"
            scene marto_small
            j "Maître Max... on ne 'renifle' pas les indices."

    scene marto_small
    play sound "sound/marteau.mp3"
    j "Accordé. Mais ne ramenez pas de confettis cette fois."

#4------------ ENQUÊTE INTERACTIVE
    play music "sound/Ambiance Tribunal Tendu.mp3"
    scene crimescenes_small
    n "Sam et Max arrivent sur la scène de crime."

    menu investigation_scene:
        "Que voulez-vous examiner en premier ?"

        "Interroger Flambé" if not indice_ticket:
            s "Tiens, voilà Flambé, le frère de la victime. Dites-nous, mon brave, qu'avez-vous vu à 23h ?"
            f "Une ombre géante... des cris... puis un grand type a couru vers sa voiture. Je me suis caché dans un baril de chapelure vide."
            jump investigation_scene

        "Examiner le sol" if not indice_ticket:
            m "(Frappe le sol avec des bâtons) Regarde Sam ! Un papier brillant sous un pneu !"
            s "Un ticket de concert... au nom de Lee-Harvey."
            $ indice_ticket = True
            m "Qui est ce Lee-Harvey ?"
            f "Regardez au dos : il y a l'adresse du propriétaire. '122 bis, Allée du Complot'."
            jump investigation_scene

        "Analyser les traces de pas":
            s "Ces empreintes sont étranges... elles semblent trop parfaites."
            m "Comme si quelqu'un les avait faites exprès !"
            $ indice_poils = True
            jump investigation_scene

        "Continuer l'enquête" if indice_ticket:
            jump suite_enquete

label suite_enquete:
    n "Sam et Max se rendent à l'adresse trouvée sur le ticket."
    scene maison_small
    s "Police Freelance. On aimerait savoir ce que votre ticket faisait sur une scène de crime."
    l "J'étais avec mon patron, Conroy Bumpus, le roi du poulet frit ! On classait des dossiers 'Défense' très confidentiels."

    menu choix_investigation_maison:
        "Que faire ?"

        "Fouiller discrètement":
            s "Intéressant... Max, tu peux aller chercher de l'eau dans la cuisine ?"
            m "Compris, chef !"
            scene lapinporte_small
            n "Max 'se perd' et ouvre une porte interdite..."

        "Forcer l'entrée de la pièce fermée":
            scene lapinporte_small
            play sound "sound/porte.mp3"
            m "Oups, ma main a glissé de façon répétée sur cette porte !"
            l "Hé ! Vous n'avez pas le droit !"

    scene porteouvert_small
    play sound "sound/porte.mp3"
    s "Regarde ça... Un costume de Bigfoot, de la colle et des poils synthétiques."
    $ indice_costume = True
    l "C'est... c'est juste un délire entre moi et le patron ! Un truc de team-building !"

    menu analyse_costume:
        "Que faire avec cette preuve ?"

        "Prendre le costume":
            s "On confisque ça comme preuve."
            m "Je peux l'essayer maintenant ?"
            s "Plus tard, Max."

        "Prendre des photos":
            m "FLASH ! Souriez pour le procès !"
            l "Attendez, on peut s'arranger..."

#5------------ CONTRE-INTERROGATOIRE INTERACTIF
    scene grandjudge_small
    j "Maître Sam, votre témoin, Flambé, est à la barre."
    scene samnormal_small
    s "Flambé, racontez-nous encore ce que vous avez vu dans le noir."
    scene flambebar_small

    play music "sound/Ambiance Objection Rapide.mp3"
    d "DÉPOSITION DE FLAMBÉ :"
    d "'Il était 23h, je sniffais de la chapelure derrière le parking.'"

    menu contre_interro_1:
        "Appuyer sur cette déclaration ?"

        "OBJECTION !":
            show objection at right
            play sound "sound/objection.mp3"
            scene objectionsam_small
            s "Vous 'sniffiez' de la chapelure ? C'est votre occupation habituelle ?"
            hide objection
            scene flambebar_small
            f "Euh... je suis un artiste culinaire ! C'est pour mon nez !"

        "Laisser passer":
            s "(Chacun ses loisirs...)"

    scene flambebar_small
    d "'Soudain, une ombre de 3 mètres avec des poils partout est passée devant moi.'"

    menu contre_interro_2:
        "Que faire ?"

        "Présenter le costume de Bigfoot":
            show objection at right
            play sound "sound/objection.mp3"
            scene objectionsam_small
            s "OBJECTION ! Vous dites avoir vu une ombre de 3 mètres ?"
            hide objection
            scene samnormal_small
            s "Regardez ce costume trouvé chez Bumpus. Max, essaie-le."
            play sound "sound/zip.mp3"
            scene lapincostume_small
            m "Je me sens beau, Sam. Je ressemble à un tapis qui a muté."
            s "Ce costume est bien trop petit pour faire 3 mètres ! Il est à la taille de Conroy Bumpus !"
            $ confiance_bruno += 3

        "Demander des précisions":
            s "Pouvez-vous décrire cette ombre plus précisément ?"
            f "Euh... grande ? Poilue ? Dans le noir c'est difficile..."

    scene flambebar_small
    d "'Elle tenait une aile de poulet KFP comme si c'était un poignard !'"

    menu contre_interro_3:
        "Une aile de poulet KFP ? Que faire ?"

        "Présenter l'analyse de sauce" if indice_sauce:
            show OBJECTION at right
            play sound "sound/objection.mp3"
            m "PRENDS ÇA ! On a analysé la sauce ! C'est la 'Sauce Spéciale Vengeance' de Bumpus !"
            hide OBJECTION
            $ confiance_bruno += 3

        "Demander où il a vu le logo KFP":
            s "Dans le noir, comment avez-vous pu voir que c'était du KFP ?"
            f "Euh... je... l'odeur ? La forme ?"
            $ confiance_bruno += 1

    d "'J'ai entendu un cri : 'C'est pour Beelzébuth !', puis le suspect s'est enfui en moonwalk.'"

    menu contre_interro_4:
        "Beelzébuth ? Réagir ?"

        "Demander qui est Beelzébuth":
            s "Qui est Beelzébuth ?"
            scene bumpusbar_small
            n "Soudain, Conroy Bumpus bondit dans la salle !"
            c "BEELZÉBUTH ÉTAIT MA MOUCHE ! KUSHMAN L'A TUÉE EN 1998 !"
            $ confiance_bruno += 5

        "Ignorer ce détail":
            s "Un moonwalk ? Vraiment ?"

#6------------ RÉVÉLATION FINALE
    scene grandjudge_small
    j "Je... j'avoue que ces preuves sont troublantes."

    if confiance_bruno >= 8:
        scene objectionsam_small
        s "Monsieur le Juge, j'ai rassemblé suffisamment de preuves pour innocenter Bruno !"
        scene bumpusbar_small
        c "(S'effondre à la barre) ASSEZ ! Oui, c'est moi ! Kushman a tué Beelzébuth en 1998 !"
        c "Elle n'avait même pas encore pondu son premier œuf ! C'était ma mouche de compagnie préférée !"
        scene samnormal_small
        s "La vengeance est un plat qui se mange froid, mais le poulet, c'est meilleur quand c'est chaud, n'est-ce pas Conroy ?"
        scene marto_small
        play sound "sound/marteau.mp3"
        j "Conroy Bumpus, vous ferez votre peine à Azcaban. Bruno, vous êtes ...."
        scene noncoupable_small
        j "NON COUPABLE !"

    else:
        scene grandjugeshoked_small
        j "Je regrette, mais les preuves ne sont pas suffisantes..."
        scene samnormal_small
        s "Attendez ! Je peux encore..."
        scene marto_small
        play sound "sound/marteau.mp3"
        j "COUPABLE !"
        scene brunoprison_small
        b "NOOOOON !"
        n "GAME OVER - Vous n'avez pas rassemblé assez de preuves !"
        return

    scene lapinparle_small
    m "Excellent travail, Sam ! On forme une sacrée équipe !"
    scene samnormal_small
    s "Allez Max, on rentre. On a une ville à protéger et un dossier de frais de déplacement à falsifier."

    n "Félicitations ! Vous avez sauvé Bruno avec [confiance_bruno] points de confiance !"

    stop music fadeout 1.0
    return

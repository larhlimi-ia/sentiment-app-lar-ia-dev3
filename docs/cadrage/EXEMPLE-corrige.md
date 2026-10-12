# Fiche de cadrage : Tri des courriels du secretariat (exemple corrige)

> Exemple fourni par l'enseignant. Il montre le niveau de detail attendu.
> Ne pas le rendre tel quel : il porte sur un autre cas que les trois du TP.

## Besoin en une phrase (obligatoire)

Repartir automatiquement les courriels recus par le secretariat entre quatre
services, pour eviter les reexpeditions manuelles qui occupent une personne
deux heures par jour.

## Utilisateur final (obligatoire)

L'agent du secretariat qui ouvre la boite partagee le matin. Il garde la main :
la proposition de service s'affiche, il valide ou corrige d'un clic.

## Approche retenue (obligatoire : cocher exactement une case)

- [ ] Regles ecrites a la main
- [x] Apprentissage supervise classique
- [ ] Grand modele de langage
- [ ] Ne rien automatiser

## Justification (obligatoire : citer au moins deux criteres)

Le critere (a) est satisfait : trois ans d'archives etiquetees par le service
destinataire, soit environ 40 000 courriels, suffisent largement pour un
classifieur de texte. Le critere (c) pese aussi : l'agent doit pouvoir
comprendre pourquoi un courriel a ete oriente vers tel service, et un modele
lineaire sur des mots permet d'afficher les termes decisifs, ce qu'un grand
modele de langage ne ferait pas aussi simplement. Le critere (b) confirme le
choix : l'entrainement tient sur un poste ordinaire, sans GPU ni abonnement.

## Donnees necessaires (obligatoire)

Objet et corps des courriels archives, avec le service destinataire comme
etiquette. Les pieces jointes et les adresses d'expediteur sont ecartees pour
limiter les donnees personnelles traitees.

## Metrique de succes (obligatoire)

Exactitude globale d'au moins 0,85 sur un jeu de test de six mois non vus, et
surtout un rappel d'au moins 0,95 sur le service juridique, dont les courriels
ont des delais legaux.

## Consequence d'une erreur (obligatoire)

Un courriel mal oriente arrive avec un ou deux jours de retard. C'est genant
mais rattrapable, sauf pour le service juridique, d'ou le seuil de rappel plus
exigeant sur cette classe.

## Risques ethiques ou de confidentialite (obligatoire)

Les courriels contiennent des donnees personnelles d'usagers. Le modele est
entraine et heberge en interne, les archives sont pseudonymisees avant
entrainement, et aucune donnee ne sort vers un service tiers.

## Approche ecartee et pourquoi (facultatif)

Les regles ecrites a la main ont ete essayees en 2023 : la liste de mots-cles
etait devenue ingerable et manquait un courriel sur quatre.

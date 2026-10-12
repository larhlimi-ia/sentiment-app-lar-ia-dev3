# TP1 : mettre en place le depot et cadrer trois cas

**Cours :** Developpement et deploiement d'applications intelligentes
**Semaine 1** · **Travail en binome** · **Depot :** `sentiment-app-lar-ia-dev`

## Ce que vous allez faire

Deux choses, qui reviendront toutes les semaines. D'abord un depot propre : un environnement reproductible, des secrets qui n'entrent pas dans Git, des artefacts lourds exclus, des tests qui verifient tout cela a votre place. Ensuite un exercice de cadrage : decider, pour trois situations, quelle approche convient et pourquoi.

Le cadrage n'est pas un prealable administratif. C'est la partie qui determine si le projet a un sens : un modele a 0,95 de score qui repond a la mauvaise question ne vaut rien.

## Objectifs

A la fin de la seance, votre depot contient :

1. un environnement virtuel en Python 3.11, avec les dependances figees ;
2. un `.env` local, jamais commite ;
3. les trois fiches de `docs/cadrage/` remplies ;
4. un historique Git avec au moins un commit par membre ;
5. `pytest -q` qui affiche **38 tests au vert** ;
6. l'integration continue au vert sur GitHub.

## Partie A : le depot (environ un tiers de la seance)

Suivez `MARCHE-A-SUIVRE.md`, controles T1 a T7. Le diagnostic `python scripts/check_setup.py` vous dit a tout moment ou vous en etes.

## Partie B : le cadrage (le reste de la seance)

Trois situations, une fiche chacune dans `docs/cadrage/`.

### Cas 1 : ordonnances incompletes en pharmacie

Une chaine de pharmacies recoit des ordonnances scannees. Environ une sur dix est incomplete : posologie absente, signature manquante, date illisible. Le personnel les trie a la main. Peut-on automatiser ce reperage ?

### Cas 2 : questions sur le reglement interieur

Le service des ressources humaines recoit chaque jour les memes questions sur le reglement interieur : conges, teletravail, notes de frais. Le reglement fait 80 pages et change deux fois par an. Peut-on repondre automatiquement ?

### Cas 3 : priorisation des avis negatifs

Un site de commerce recoit 2 000 avis par jour. L'equipe veut traiter en priorite les avis negatifs, pour rattraper les clients mecontents avant qu'ils ne partent. Elle fixe une exigence : **ne pas manquer plus d'un avis negatif sur dix**, soit un rappel d'au moins 0,90 sur cette classe.

### Pour chaque cas

Remplissez toutes les rubriques obligatoires, cochez **une seule** approche, et justifiez en citant au moins deux criteres parmi :

- **(a)** volume et qualite des donnees disponibles
- **(b)** cout et delai de mise en oeuvre
- **(c)** besoin d'expliquer la decision a l'utilisateur
- **(d)** consequence d'une erreur

`docs/cadrage/EXEMPLE-corrige.md` montre le niveau attendu sur un quatrieme cas.

## Partie C : apercu de la suite (facultatif)

Si le temps le permet, lancez les deux scripts de `exemples/` : un modele entraine, une interface affichee. Ils montrent ou mene ce depot. Observez ce qui se passe quand vous soumettez un avis d'un domaine que le modele n'a pas appris.

## Livrables

- les trois fiches remplies, commitees ;
- `pytest -q` au vert, 38 tests ;
- un commit par membre du binome ;
- l'integration continue au vert.

## Bareme indicatif (sur 20)

| Critere | Points |
| --- | --- |
| Environnement et structure, `pytest -q` au vert | 5 |
| Aucun secret ni artefact lourd dans Git | 3 |
| Fiches de cadrage completes | 4 |
| Pertinence des approches retenues | 4 |
| Justifications citant les criteres | 2 |
| Travail du binome visible dans l'historique | 2 |

## Pieges frequents

- Installer la derniere version de Python au lieu de la 3.11.
- Commiter `.venv/`, ce qui produit un depot de plusieurs centaines de Mo.
- Commiter `.env` avec sa cle.
- Cocher deux approches « parce que les deux conviennent » : le TP demande de trancher.
- Ecrire une justification sans citer les criteres : les tests verifient leur presence.

`DEPANNAGE.md` traite les onze pannes rencontrees en seance.

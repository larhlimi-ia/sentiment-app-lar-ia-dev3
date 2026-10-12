# Git : le minimum pour le binome

## Une fois, dans le depot

```
git config user.name "votre-identifiant"
git config user.email "votre.adresse@exemple.fr"
```

Sans `--global` : la configuration reste propre a ce depot et n'affecte pas vos autres projets.

## Le cycle de travail

```
git pull                 # recuperer le travail de l'autre AVANT de commencer
...                      # travailler
git status               # voir ce qui a change
git add -A               # tout preparer
git status               # relire : ni .venv/, ni .env, ni .joblib
git commit -m "message clair"
git push
```

## Le commit du second membre

Un test exige deux auteurs. Chacun pousse depuis son poste, avec sa propre identite. Pour un commit sans modification :

```
git commit --allow-empty -m "relecture du binome"
```

Verifier :

```
git log --format="%an : %s"
git shortlog -sn --all
```

## Rattraper une erreur

| Situation | Commande |
| --- | --- |
| fichier ajoute par erreur, pas encore commite | `git restore --staged <fichier>` |
| modifier le dernier message de commit | `git commit --amend -m "nouveau message"` |
| `.venv/` ou `.env` commite par erreur | `git rm -r --cached .venv` puis commitez |
| revenir a la derniere version commitee | `git restore <fichier>` |
| voir ce que Git suit reellement | `git ls-files` |
| savoir pourquoi un fichier est ignore | `git check-ignore -v <fichier>` |

## Conflits

Si `git pull` signale un conflit, le fichier contient des marqueurs `<<<<<<<`, `=======` et `>>>>>>>`. Ouvrez-le, gardez ce qu'il faut, supprimez les marqueurs, puis :

```
git add <fichier>
git commit
```

Le meilleur remede reste la prevention : `git pull` avant de commencer, et des commits courts.

### Questionnaire MLOps - 4DVSO - Intégration Continue - M1

#### Fondamentaux DevOps et MLOps

1. **Expliquez ce que signifie DevOps et comment il facilite la collaboration entre les équipes de développement et d'opérations.**

##### Réponse 
    
 Le devOps est une pratique ou un poste de travail (métier) qui vise à améliorer 
 la vitesse de production et la maintenabilité des projets en axant la conception 
 des applications sur le développement et les opérations de déployment. 
 On favorise l'automatisation et la surveillance à tous les stades de 
 la construction, on met en lace des tests avant tout déploiement des applications. 
 Le devOps sert à accélérer le processus de création des applications ou de leurs features.

2. **Décrivez ce qu'est le MLOps et en quoi il diffère du DevOps, surtout en ce qui concerne le cycle de vie des modèles de machine learning.**

##### Réponse

Le MLOps est la dérive du devOps pour les projets de machine learning.
L'idée est d'automatiser la production de modèles, de les déployer et de les 
monitorer.

3. **Expliquez l'acronyme C.A.L.M.S et son importance dans le contexte DevOps**

##### Réponse

C.A.L.M.S est un acronyme qui signifie Culture, Automation, Lean, Measurement, Sharing.
Il définit les principes fondamentaux du devOps qui permettent de faciliter la collaboration entre les 
équipes de développement et d'opérations ou leurs tâches en générales.

4. **Listez 6 outils couramment utilisés dans la pratique du DevOps et MLOps et décrivez brièvement leur fonction.**

##### Réponse

- Git : Outil de gestion de version
- Docker : Outil de conteneurisation
- Kubernetes : Outil de gestion de conteneurs
- GitLab : Outil de gestion de version et d'intégration continue
- Azure DevOps : Outil de gestion de version et d'intégration continue
- Kubeflow : Outil de gestion de version et d'intégration continue

5. **Expliquez ce qu'est l'intégration continue et son rôle.**

##### Réponse

L'intégration continue est une pratique de développement logiciel qui consiste
à vérifier régulièrement que le code source est fonctionnel 
et qu'il ne casse pas l'application couramment en production.  

6. **Décrivez ce qu'est la livraison continue et comment elle s'intègre dans les workflows MLOps.**

##### Réponse

La livraison continue est une pratique de développement logiciel qui consiste
à déployer régulièrement les nouvelles fonctionnalités de l'application.

7. **Expliquez le déploiement continu et sa différence avec la livraison continue.**

##### Réponse

La différence entre la livraison continue et le déploiement continu est que 
dans le cas de la livraison continue, les nouvelles fonctionnalités sont
déployés manuellement alors que dans le cas du déploiement continu,
les nouvelles fonctionnalités sont déployés automatiquement.
Les tests sont automatisés et s'ils sont passés les features sont directement déployées
dans le deuxième cas.

8. **Décrivez le concept de versionnage sémantique et pourquoi il est important dans la gestion des versions de logiciels.**

##### Réponse

Le versionnage sémantique est une convention de versionnement des logiciels qui permet de
définir des règles pour le changement de version. Cela permet de savoir si une nouvelle
version est compatible avec une ancienne version.
Le fonctionnement de cette convention est basé sur trois nombres séparés par des points tel quel:


| name version  | Major | Minor | Patch |
|---------------|-------|-------|-------|
| node v12.18.3 | 12    | 18    | 3     |
| python 3.8.5  | 3     | 8     | 5     |

Un modification majeur correspond à l'implémentation d'une fonctionnalité qui cassera la 
rétrocompatibilité, une modification mineur correspond à l'implémentation d'une fonctionnalité
qui ne cassera pas la rétrocompatibilité et un patch correspond à une correction de bug.

9. **Listez quatre fournisseurs de services cloud et mentionnez une caractéristique unique pour chacun.**

##### Réponse

- AWS : Amazon Web Services
- Azure : Microsoft
- Google Cloud
- OVH

10. **Définissez le setvice IaaS et donnez un exemple.**

##### Réponse

IaaS est un service de cloud computing qui fournit des ressources informatiques
virtuelles sur internet. C'est une infrastructure virtualisée
qui est accessible via une API ou un dashboard web.

11. **Définissez le PaaS et donnez un exemple.**

##### Réponse

PaaS est un service de cloud computing qui fournit une plateforme de développement
et de déploiement d'applications. C'est une plateforme qui permet de développer
des applications sans se soucier de l'infrastructure nécessaire à l'application.

13. **Définissez le SaaS et donnez un exemple**

##### Réponse

SaaS est un service de cloud computing qui fournit des applications logicielles
hébergées sur internet. C'est une application qui est accessible via un navigateur
web.

14. **Définissez le DVC, et donnez un exemple d'une command.**

##### Réponse

DVC est un outil de gestion de version pour les données. Il permet de versionner
les données et de les partager entre les membres d'une équipe de développement.

```bash

dvc init
dvc add data.csv
dvc commit -m "Add data.csv"
dvc push

```

15. **C'est quoi un training job ?**

##### Réponse

Un training job est un processus qui consiste à entraîner un modèle de machine learning
sur un jeu de données avant de le déployer en production ou pour tester la fiabilité de 
notre modèle.
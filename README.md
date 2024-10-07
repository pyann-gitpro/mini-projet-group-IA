
# (Mini-projet-Zorlangue-caesar-cryptageImage)
**Lien à ajouter : https://github.com/????????**
<!-- description -->
Ce projet est un programme pédagogique de remise en oeuvre des sujets pratiqués : Langage Python, Bonne pratique d'installation et de développement.

---

# Zorglangue - Projet de Cryptage

---

## Description du projet

Le projet **Zorglangue** s'inspire du langage inventé par le personnage **Zorglub** de la bande dessinée Spirou et Fantasio. L'objectif est d'inverser les lettres dans chaque mot d'une phrase tout en conservant l'ordre des mots et les règles de ponctuation.

Ce projet intègre également des fonctionnalités supplémentaires telles que la génération aléatoire de clés de cryptage, un système de décryptage interactif, et un suivi des erreurs pour évaluer la qualité des décryptages.

---

## Fonctionnalités principales

1. **Inversion des lettres dans les mots**
   - Chaque mot est inversé mais l'ordre des mots est conservé. La ponctuation et les majuscules sont respectées.

2. **Génération d'une clé aléatoire**
   - Génération d'une clé simple pour un chiffrement de type César ou autre chiffrement basique.

3. **Décryptage avec tentatives utilisateur**
   - L'utilisateur peut essayer de deviner la clé de décryptage. Le programme affiche le résultat à chaque tentative.

4. **Suivi des erreurs et journalisation**
   - Les erreurs de décryptage sont enregistrées dans un **DataFrame** et suivies en temps réel.
   - Le programme génère des journaux d'activités (`app.log`) pour un suivi détaillé.

5. **Tests automatiques**
   - Des tests sont inclus pour vérifier la cohérence du chiffrement et du décryptage.

---

## Structure du projet

```bash
├── app/
│   ├── __init__.py           # Initialisation du package
│   ├── components/
│   │   ├── zorglangue.py      # Inversion des lettres et gestion des phrases
│   │   ├── cryptage.py        # Génération de clés et cryptage simple
│   │   └── erreurs.py         # Suivi des erreurs et calcul des métriques
├── tests/
│   ├── test_zorglangue.py     # Tests pour Zorglangue
│   └── test_cryptage.py       # Tests pour les clés et cryptage
├── .github/
│   └── workflows/
│       └── test.yml           # Github Actions - Tests automatiques
├── requirements.txt           # Dépendances du projet
├── README.md                  # Ce fichier README
└── main.py                    # Script principal
```

## Généralités (Titre 5)

Cette application simule une colonie de fourmis composée de différentes classes : ouvrières, soldats et une reine. Chaque fourmi effectue des actions comme collecter de la nourriture, défendre la colonie ou produire de nouvelles fourmis. L'énergie de la colonie est partagée et est consommée lorsque les fourmis se déplacent.

## Tests Unitaires / Github Actions et Workflows(Titre 6)

- **Créer un fichier de workflow** : Dans votre dépôt GitHub, créez un fichier `.github/workflows/tests.yml` (ou un nom similaire). Ce fichier YAML définit les étapes de votre workflow d'automatisation.
- **Définir les déclencheurs** : Indiquez quand vous souhaitez que vos tests soient exécutés (par exemple, à chaque push sur la branche main, lors de la création d'une pull request, etc.).
- **Configurer l'environnement** : Spécifiez l'environnement d'exécution de vos tests (système d'exploitation, version de Python, dépendances, etc.).
- **Exécuter les tests** : Utilisez les actions appropriées pour installer vos dépendances, puis lancez vos tests avec la commande de votre framework de test (pytest, unittest, etc.).
- **Afficher les résultats** : Utilisez les actions pour afficher les résultats des tests directement sur GitHub, par exemple en les publiant dans les commentaires de la pull request.

***Voici un exemple simple de workflow pour pytest :***

```yaml
name: Python application CI/CD
on:
  push:
    branches: [ main, dev ]  # Branch to survey
  pull_request:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11"]
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements_train.txt
        # Add any specific installation commands for libcpab
        pip install -e libcpab


    # tests
    - name: Run unit tests (un fichier)
      run: |
        pytest tests/test_0.py
    - name: Run unit tests (un autre fichier)
      run: |
        pytest tests/test_1.py
```

## Créateurs (Titre 7)

- [Saadia CHADLI](mailto:@gmail.com)
- [Jules NDIAYE](mailto:@gmail.com)
- [Yann PAAEHO](mailto:paaeho.yann.pro@gmail.com)

---
#### Best Practices (Nota Bene, notes supp)
1. **Structure du code**

>    ***Organisation des classes :*** Le code est organisé en trois classes principales qui héritent de la classe mère Fourmi. Cela permet une modularité et facilite les évolutions futures de l'application.
        Ouvriere : Responsable de la collecte de nourriture.
        Soldat : Défend la colonie.
        Reine : Produit de nouvelles fourmis.

>    ***Méthodes de classe (@classmethod) :*** La méthode se_deplacer est utilisée avec le décorateur @classmethod pour représenter une action globale qui affecte l'énergie partagée par la colonie.

2. **Ajout de fonctionnalités**

>    ***Facilité d'ajout de nouvelles actions :*** Si vous souhaitez ajouter de nouvelles actions pour une fourmi (par exemple, exploration), vous pouvez simplement définir une nouvelle méthode dans les sous-classes concernées.

>    ***Attributs partagés :*** L'attribut energie_class est un bon exemple d'attribut partagé au niveau de la classe, garantissant que toutes les instances accèdent à la même ressource énergétique.

3. **Gestion de l'énergie**

> L'énergie est un élément clé dans cette simulation. Chaque action de déplacement réduit l'énergie de la colonie entière. Assurez-vous de suivre l'état de l'énergie via la méthode se_deplacer.

4. **Modularité et réutilisabilité**

>    Si vous voulez réutiliser ce projet ou l'étendre à d'autres types d'insectes, vous pouvez facilement le faire en ajoutant de nouvelles sous-classes à la classe mère Fourmi.

>    La gestion de la nourriture et des nouvelles fourmis est conçue pour être flexible et adaptable à des scénarios plus complexes.

---
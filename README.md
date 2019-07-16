DATA CHALLENGE

Le but de se projet était de réaliser un programme permettant d'effectuer un external sorting sur un fichier donné.

Ce projet a été réaliser en Python en utilisant l'IDE Spyder, pour la synchronisation avec GITHub j'ai utilisé GIT Kraken.
Pour exécuter ce programme il suffit d'importer les fichier python sur un compilateur Python quelconque et de les exécuter, l'ordre d'éxécution devrait être :
1. GenerateFileToSort.py
2. ExternalSort.py
3. UnitTest.py

Description des différents fichiers :
GenerateFileToSort.py : génère un fichier texte contenant un nombre de lignes données, chaque ligne est une suite de charactères aléatoire compris entre 1 et une limite fixée (dans l'exemple le fichier crée contient 500 lignes de 1 à 20 charactères)

ExternalSort.py : 
fichier réalisant l'external sorting sur un fichier donnée, l'algorithme choisis permet de diviser le fichier d'entré en un nombre de sous fichiers determinés en fonction de la taille de chaque sous fichier voulu (la taille utilisé dans l'exemple est 100 lignes par fichier), ces fichiers sont ensuite triés en utilisant la méthode "sorted" disponible dans la librairie python de base. 
Ils sont ensuite mergés dans un fichier de sorti selon l'algorithme suivant : 
1. les fichiers sont représenté sous forme de pile où leur premier élement, qui est leur minimum est directement accessible
2. On récupère le minimum des minimums de chaque fichier et on l'ajoute au fichier de sorti
3. On remplace le minimum du fichier choisi par son élement suivant
4. on répète 2 et 3 jusqu'à avoir vidé tous les fichiers

UnitTest.py :
Fichier permettant de controller la sortie du programme de tri en triant le fichier de départ avec la méthode de tri disponible dans la librairie python et en controllant ensuite ce résultat avec le fichier créer par notre programme

unsorted.py : 
Le fichier généré que l'on désire trier

sorted.py :
Le fichier obtenu après l'exécution de notre programme

Temp/subfileX.txt :
les sous fichiers générés pendant l'exécution du programme

Amélioration possible du programme :
Une amélioration qui pourrait indéniablement augmenter les perfomances de ce programme serait de paraléliser le tri des sous fichiers
Il faudrait comparer les résultats de ce programme avec d'autres algorithme de de tri et de merge

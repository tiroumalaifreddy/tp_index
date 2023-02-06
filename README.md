
# TP Index ENSAI - Indexation Web

Ce mini-projet implémente un générateur d'index à partir d'une liste d'URL. L'application extrait pour chaque URL le titre du document qui est ensuite tokenisé. Un index inversé est ensuite crée. Il existe deux types d'index : un index avec un compte de chaque token dans l'URL tokenisé et un index avec la position des tokens dans l'URL tokenisé. Ces index sont ensuite exportés dans des fichiers json. 
Le fichier metadata.json contient quelques statistiques sur l'index crée.



## Authors

- [@tiroumalaifreddy](https://www.github.com/tiroumalaifreddy)


## Installation

Dans l'idéal, lancer un environnement virtuel (voir https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html).

Pour installer les packages requis:
```bash
pip install -r requirements.txt
```
    
## Usage/Examples

L'application prend en entrée:
- ```--json_file {file_path : str}````: permet d'indiquer le chemin du fichier json contenant la liste des URLs


En se plaçant à la racine du projet et en ayant le fichier des URLs à la racine (```crawled_urls.json```) :

```python
python3.8 main.py --json_file crawled_urls.json
```

Deux fichiers .txt seront alors crées dà la racine:
-title.non_pos_index.json : index avec le compte des tokens
-title.pos_index.json : index avec la position du token dans l'URL tokenisé

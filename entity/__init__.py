
# ce fichier sera parcouru par python a chaque import du module 'entity'
# il listera tous les sous modules qui seront accessibles
# en effet, dans le fichier "detection.py", il y a "from entity import Dataset, Algorithm"
# et là il voit que entity c'est un dossier et pas un fichier du coup il regarde dans le "__init__.py"

from .algorithm import Algorithm
from .dataset import Dataset
from .input_parameters import InputParameters

from sklearn.model_selection import ShuffleSplit

class Dataset():
    # args est le tableau des paramètres supplémentaires(en option(*))
    # kwargs est le dico des paramètres supplémentaires(en option(*))
    # les paramètres de la forme a = 'quelque chose' sont stockés dans kwargs
    # les paramètres non nommés sont stockés dans args
    # notion d'odre = tableau
    # notion d'association = dico (un dico n'a pas d'ordre)

    def __init__(self, data, label, *args, **kwargs):
        self.data = data
        self.label = label
        self.shuffle_split = None
        self.train_indexes_table =[]
        self.test_indexes_table =[]

    def generate_train_test_indexes(self, n_splits, test_proportion, random_state = 0):
        self.shuffle_split = ShuffleSplit(n_splits = n_splits, random_state = random_state, test_size = test_proportion)
        for train_indexes, test_indexes in self.shuffle_split.split(self.label):
            self.train_indexes_table.append(train_indexes)
            self.test_indexes_table.append(test_indexes)

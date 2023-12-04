class Category:
    categories = []

    def add(self, categorie: str):
        if categorie not in self.categories:
            self.categories.append(categorie)
            return self.categories.index(categorie)

        raise ValueError

    def get(self, indx: int):
        if indx > len(self.categories) - 1:
            raise IndexError

        return self.categories[indx]

    def delete(self, indx: int):
        if indx < len(self.categories):
            self.categories.pop(indx)

    def update(self, indx: int, categorie: str):
        if indx < len(self.categories):
            self.categories[indx] = categorie
        elif categorie in self.categories:
            raise ValueError
        else:
            self.categories.append(categorie)

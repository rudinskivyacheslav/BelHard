class Category:
    def __init__(self):
        self.categories = []

    def list_category_name(self):
        return list(map(lambda x: x.get("name"), self.categories))

    def add(self, categorie: {}):
        if categorie.get("name") not in self.list_category_name():
            self.categories.append(categorie)
            return self.categories.index(categorie)

        raise ValueError

    def get(self, indx: int):
        if indx < len(self.categories):
            return self.categories[indx]

        raise IndexError

    def delete(self, indx: int):
        if indx < len(self.categories):
            self.categories.pop(indx)

    def update(self, indx: int, categorie: {}):
        if indx < len(self.categories):
            self.categories[indx] = categorie
        elif categorie in self.list_category_name():
            raise ValueError
        else:
            self.categories.append(categorie)

    def make_published(self, indx: int):
        if indx < len(self.categories):
            self.categories[indx]["is_published"] = True # у меня тут не сработал метод self.categories[indx].get("is_published") = True
        raise IndexError

    def make_unpublished(self, indx: int):
        if indx < len(self.categories):
            self.categories[indx]["is_published"] = False
        raise IndexError


cat = Category()
cat.categories = [
        {"name": "11", "is_published": False},
        {"name": "22", "is_published": True},
        {"name": "33", "is_published": True},
        {"name": "44", "is_published": False}
                  ]
res = cat.add({"name": "111", "is_published": True})


a = {"name": "11", "is_published": False}
print(a.values())

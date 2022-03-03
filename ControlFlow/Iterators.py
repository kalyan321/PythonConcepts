class squares:
    def __init__(self, limit):
        self.limit = limit
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.limit:
            val = self.n * self.n
            self.n += 1
            return val
        else:
            raise StopIteration


def iterators_explanation():
    names = ["kalyan", "prashanth", "sunanda", "raja", "eswaramma"]
    iter_names_obj = iter(names)
    while iter_names_obj._:
        try:
            name = next(iter_names_obj)
            print(name)
        except StopIteration:
            print(StopIteration)
            break


def check_objects_has_iterators():
    print(hasattr(3, '__iter__'))
    print(hasattr((1, 2), '__iter__'))
    print(hasattr({'1': [2, 3]}, '__iter__'))
    print(hasattr('ab', '__iter__'))
    print(hasattr([1, 2], '__iter__'))


def pythagorean_triplets():
    pt = ((a, b, c) for a in range(10) for b in range(10) for c in range(10) if a * a == (b * b + c * c))
    print(pt)


if __name__ == "__main__":
    # iterator_explanation()
    # check_objects_has_iterators()

    # for sq in squares(4):
    #     print(sq)
    # sq = [x for x in squares(10)]
    # print(sq)

    pythagorean_triplets()
    pass

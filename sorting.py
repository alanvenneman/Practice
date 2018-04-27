from Project.Mixin import Mixin


class Sort(Mixin):
    def __init__(self):

        mix = Mixin()
        self.li = mix.listGeneration(10, 500)
        print("Before sort: ", self.li)

    def get_list(self):
        return self.li


class DoSort(Sort):
    def __init__(self):
        Sort.__init__(self)

new_sort = DoSort()
new_list = new_sort.get_list()
insert = new_sort.insertion_sort(new_list)
# f string
print(f"After sort: {insert}")

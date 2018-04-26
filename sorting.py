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

    def insertion_sort(self, sort):
        for i in range(1, len(sort)):
            current_element = sort[i]
            k = i - 1
            while k >= 0 and sort[k] > current_element:
                sort[k + 1] = sort[k]
                k -= 1

            sort[k + 1] = current_element
        return sort


new_sort = DoSort()
new_list = new_sort.get_list()
insert = new_sort.insertion_sort(new_list)
# f string
print(f"After sort: {insert}")

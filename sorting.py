<<<<<<< HEAD
from module.Mixin import Mixin
=======
from Project.Mixin import Mixin
>>>>>>> 019139d9c4330293b87053aab7a29cc3cdfa3e20


class Sort(Mixin):
    def __init__(self):
<<<<<<< HEAD

=======
        Mixin.__init__(self)
>>>>>>> 019139d9c4330293b87053aab7a29cc3cdfa3e20
        mix = Mixin()
        self.li = mix.listGeneration(10, 500)
        print("Before sort: ", self.li)

    def get_list(self):
        return self.li


class DoSort(Sort):
    def __init__(self):
        Sort.__init__(self)

<<<<<<< HEAD
new_sort = DoSort()
new_list = new_sort.get_list()
insert = new_sort.insertion_sort(new_list)
# f string
print(f"After sort: {insert}")
=======
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
print("After sort: ", insert)
>>>>>>> 019139d9c4330293b87053aab7a29cc3cdfa3e20

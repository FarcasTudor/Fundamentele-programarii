
class Sorter:

    def _negare(self, x):
        return not x

    def _identitate(self, x):
        return x

class BubbleSort(Sorter):

    def sort(self, list, key=lambda x:x, cmp=lambda x,y: x>y, reversed=False):
        # functie care sorteaza o lista de elemente folosindu-se de  Bubble Sort
        if reversed:
            operatie = self._negare
        else:
            operatie = self._identitate

        for x in range(0, len(list)-1):
            for y in range(x+1, len(list)):
                if operatie(cmp(key(list[x]), key(list[y]))):
                    aux = list[x]
                    list[x] = list[y]
                    list[y] = aux



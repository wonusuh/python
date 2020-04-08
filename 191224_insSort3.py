src = [5, 4, 3, 2, 1]

class InsSort:
    def __init__(self, src):
        self.src = src
    def ins_sort(self):
        target = []
        while self.src:
            tmp = self.src.pop(0)
            minIdx = 0
            for index in range(len(target)):
                if tmp < target[index]:
                    if target[index] < target[minIdx]:
                        minIdx = index
                else:
                    minIdx = index + 1
            target.insert(minIdx, tmp)
        return target
    trg = ins_sort(src)

# AttributeError: 'list' object has no attribute 'src'

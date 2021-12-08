import numpy as np

class Entry:
    def __init__(self, line):
        self.sigpat = line[0].split()
        self.out_val = line[1].split()
    
    def __str__(self):
        return f"sigpat: {self.sigpat} | output value: {self.out_val}"

    def __repr__(self):
        return f"{self.sigpat}, {self.out_val}"
    
    def uniq_count(self):
        return sum([len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7 for x in self.out_val])



def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split(" | ") for line in f]
    return data


def main():
    data = gobble('input')
    print(data[0])
    
    e = [Entry(d) for d in data]

    print(sum([x.uniq_count() for x in e]))

    #print(e[0])
    #print(e)


if __name__ == "__main__":
    main()


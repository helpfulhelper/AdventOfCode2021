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

class Digit:
    def __init__(self, entry):
        self.sigpat = [x for x in entry.sigpat]
        self.out_val = [x for x in entry.out_val]
        self.enc = {str(i): None for i in range(10)}
        #uniques
        for sig in self.sigpat:
            if len(sig) == 2:
                self.enc["1"] = sig
            elif len(sig) == 3:
                self.enc["7"] = sig
            elif len(sig) == 4:
                self.enc["4"] = sig
            elif len(sig) == 7:
                self.enc["8"] = sig
        #6 digits
        for sig in self.sigpat:
            if len(sig) == 6:
                if len(set(self.enc["1"]) - set(sig)) != 0:
                    self.enc["6"] = sig
                elif len(set(self.enc["4"]) - set(sig)) != 0:
                    self.enc["0"] = sig
                else:
                    self.enc["9"] = sig
        #5 digits
        for sig in self.sigpat:
            if len(sig) == 5:
                if len(set(self.enc["1"]) - set(sig)) == 0:
                    self.enc["3"] = sig
                elif len(set(self.enc["6"]) - set(sig)) == 1:
                    self.enc["5"] = sig
                else:
                    self.enc["2"] = sig
    def __repr__(self):
        return f'{self.enc}'
    def __str__(self):
        return f'{self.enc}'

    def output(self):
        num = []
        for e in self.out_val:
            for k, v in self.enc.items():
                if set(e) == set(v):
                    num.append(str(k))
        return int(''.join(num))



def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split(" | ") for line in f]
    return data


def main():
    data = gobble('input')
    e = [Entry(d) for d in data]
    digit = [Digit(d) for d in e]

#    print([d.output() for d in digit])

    print(sum([d.output() for d in digit]))
 

if __name__ == "__main__":
    main()


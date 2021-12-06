class School:
    def __init__(self):
        self.bucket = [0,0,0,0,0,0,0,0,0]

    def tick(self):
        old = self.bucket[:]
        spawn = old[0]
        for ind,val in enumerate(self.bucket):
            if ind+1 < len(self.bucket):
                self.bucket[ind] = old[ind+1]
            else:
                self.bucket[ind] = old[0]
        self.bucket[6] += spawn

    def add_fish(self, age):
        self.bucket[age] += 1

    def __repr__(self):
        return f'{self.bucket}'
    def __str__(self):
        return f'{self.bucket}'

def main():
    with open("input") as f:
        data = f.read().split(',')
        data = [int(d) for d in data]
    #print(data)

    school = School()
    for d in data:
        school.add_fish(d)

    for day in range(256):
       school.tick()

    print(sum(school.bucket))


if __name__ == "__main__":
    main()

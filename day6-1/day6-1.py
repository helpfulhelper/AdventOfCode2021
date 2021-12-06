class LanternFish:
    def __init__(self, age=9):
        self.age = age
    
    def tick(self, school):
        if self.age == 0:
            self.age = 6
            school.append(LanternFish())
        else:
            self.age -= 1
    
    def __repr__(self):
        return f'{self.age}'
    def __str__(self):
        return f'{self.age}'


def main():
    with open("input") as f:
        data = f.read().split(',')
        data = [int(d) for d in data]
    #print(data)

    school = []
    for d in data:
        school.append(LanternFish(d))
    #print(school)
    for day in range(80):
        for fish in school:
            fish.tick(school)
        print(day)
    print(len(school))
    #print(school)

if __name__ == "__main__":
    main()


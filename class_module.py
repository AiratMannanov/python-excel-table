class Human():
    def __init__(self, name, surname, age, sex, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.city = city

    @property
    def getCity(self):
        return self.city

    @property
    def getName(self):
        return self.name

    @property
    def isGrandParent(self):
        return self.age > 70

    @property
    def isKid(self):
        return self.age < 18

    @property
    def isWoman(self):
        return self.sex == 'ж'

    @property
    def isMan(self):
        return self.sex == 'м'

    def describeHuman(self):
        fName = self.name + " " + self.surname + " lives in " + self.city + \
            ". Has " + str(self.age) + " years. Identify self as " + self.sex
        print(fName)

    def checkGender(self):
        if (self.sex == "м"):
            return "м"
        elif(self.sex == "ж"):
            return "ж"
        else:
            return "undefined gender"


class Student(Human):
    def __init__(self, name, surname, age, sex, city, uni, faculty, avrgMarks):
        super().__init__(name, surname, age, sex, city)
        self.uni = uni
        self.faculty = faculty
        self.avrgMarks = avrgMarks

    @property
    def getUni(self):
        return self.uni

    @property
    def getFaculty(self):
        return self.faculty

    @property
    def scholarship(self):
        if (self.avrgMarks == 5):
            return 5000
        elif (self.avrgMarks < 3.6):
            return 0
        else:
            return 3000

import class_module as cm
import pandas as pd


class AppController():
    def __init__(self, fileName):
        data = pd.read_excel(fileName + '.xlsx', dtype=object)
        data = data.fillna('')
        self.data = data.to_dict('split')
        self.people = []

        for item in self.data['data']:
            if (len(item[5])):
                student = cm.Student(item[0], item[1], item[2],
                                     item[3], item[4], item[5], item[6], item[7])
                self.people.append(student)
            else:
                human = cm.Human(item[0], item[1], item[2], item[3], item[4])
                self.people.append(human)

    @property
    def students(self):
        return list(filter(lambda person: isinstance(person, cm.Student), self.people))

    @property
    def humans(self):
        return list(filter(lambda person: isinstance(person, cm.Human), self.people))

    @property
    def women(self):
        return list(map(lambda person: person.getName, filter(lambda person: person.isWoman, self.people)))

    @property
    def men(self):
        return list(map(lambda person: person.getName, filter(lambda person: person.isMan, self.people)))

    @property
    def uniqueCities(self):
        cities = list(map(lambda person: person.getCity, self.people))
        return list(set(cities))

    @property
    def uniqueUniAndFaculty(self):
        data = dict()
        for student in self.students:
            data[student.getUni] = dict()

        for student in self.students:
            data[student.getUni][student.getFaculty] = []

        for student in self.students:
            data[student.getUni][student.getFaculty].append(student.getName)

        formatedData = dict()
        for uni in data.keys():
            for faculty in data[uni].keys():
                formatedData[uni + '/' + faculty] = data[uni][faculty]
        max = self.getMaxLength(formatedData)
        formatedData = self.fillTheSameSize(formatedData, max)
        return formatedData

    @property
    def studentsWithScholarship(self):
        return dict({
            'имя': list(map(lambda student: student.getName, self.students)),
            'стипендия': list(map(lambda student: student.scholarship, self.students)),
        })

    @property
    def cityData(self):
        cityData = dict()
        for city in self.uniqueCities:
            cityData[city] = self.getCityPeople(city)
        maxLength = self.getMaxLength(cityData)
        self.fillTheSameSize(cityData, maxLength)
        return cityData

    @property
    def genderData(self):
        genderData = dict({
            'муж': self.men,
            'жен': self.women
        })
        maxLength = self.getMaxLength(genderData)
        self.fillTheSameSize(genderData, maxLength)
        return genderData

    @property
    def kidsData(self):
        kidsData = dict({
            'дети': list(map(lambda person: person.getName, filter(lambda person: person.isKid, self.people)))
        })
        return kidsData

    @property
    def grandParentData(self):
        grandParentData = dict({
            'пенсионеры': list(map(lambda person: person.getName, filter(lambda person: person.isGrandParent, self.people)))
        })
        return grandParentData

    def getCityPeople(self, city):
        return list(map(lambda person: person.getName, filter(lambda person: person.getCity == city, self.people)))

    @staticmethod
    def getMaxLength(dict):
        return max(list(
            (map(lambda array: len(array), dict.values()))))

    @staticmethod
    def fillTheSameSize(dict, maxSize):
        for array in dict.values():
            while(len(array) < maxSize):
                array.append('nan')
        return dict

    def getInput(self):
        userInput = input()
        if (not userInput.isnumeric()):
            print('Please enter a number\n')
            self.getInput()

        if (int(userInput) > 0 and int(userInput) < 7):
            self.createExcelTable(userInput)
        else:
            print('Enter number in range\n')
            self.getInput()

    def welcome(self):
        print('Hello, select a table that you want\n')
        print('1 - City Table\n')
        print('2 - Uni/Faculty Table\n')
        print('3 - Gender Table\n')
        print('4 - Kids Table\n')
        print('5 - Grandparents Table\n')
        print('6 - Students with Scolarship Table\n')
        self.getInput()

    def createExcelTable(self, select):
        selectInt = int(select)
        name = None
        data = None
        if (selectInt == 1):
            name = 'CityTable'
            data = self.cityData
        elif (selectInt == 2):
            name = 'UniTable'
            data = self.uniqueUniAndFaculty
        elif (selectInt == 3):
            name = 'GenderTable'
            data = self.genderData
        elif (selectInt == 4):
            name = 'KidsTable'
            data = self.kidsData
        elif (selectInt == 5):
            name = 'GrandParentsTable'
            data = self.grandParentData
        elif (selectInt == 6):
            name = 'ScholarshipTable'
            data = self.studentsWithScholarship

        writer = pd.ExcelWriter(name + '.xlsx', engine='xlsxwriter')
        pd.DataFrame(data).to_excel(
            writer, sheet_name=name, index=False)
        writer.save()
        table = pd.read_excel(
            name + '.xlsx', dtype=object).fillna('-')
        print(table)


app = AppController('data12')
app.welcome()

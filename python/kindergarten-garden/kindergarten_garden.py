class Garden:
    PLANTS = {'C': 'Clover',
              'G': 'Grass',
              'R': 'Radishes',
              'V': 'Violets'}

    STUDENTS = [
        'Alice',
        'Bob',
        'Charlie',
        'David',
        'Eve',
        'Fred',
        'Ginny',
        'Harriet',
        'Ileana',
        'Joseph',
        'Kincaid',
        'Larry',
    ]

    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = sorted(students)
        self.rows = diagram.split('\n')
    
    def plants(self, student):
        col = self.students.index(student) * 2
        plants = [self.rows[0][col], self.rows[0][col+1], 
                  self.rows[1][col], self.rows[1][col+1]]

        names_plants = [Garden.PLANTS[plant] for plant in plants]
        
        return names_plants

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = self.matrix_string.split("\n")
        self.row_nums = [[int(x) for x in row.split()] for row in self.rows]

    def row(self, index):
        return self.row_nums[index-1]

    def column(self, index):
        column = []
        for row in self.row_nums:
            column.append(row[index-1])
        return column

class grid_element:
    def __init__(self,row,col, label, tens, sevens):
        self.row = row 
        self.col = col
        self.name = 'img' + str(self.row) + str(self.col)
        self.label = label
        self.tens_mapping = tens
        self.sevens_mapping = sevens
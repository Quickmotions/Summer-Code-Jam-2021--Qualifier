def make_table(rows, labels = None, centered = False):
    import math
    table = ""
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    :   │ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘
    """
    amountRow = len(rows) #amount of items in row
    amountColumn = len(rows[0]) #amount of items in column
    columnLen = []
    for col in range(amountColumn):
        columnLen.append(0)
        for row in rows:
            if len(str(row[col])) > columnLen[col]:
                columnLen[col] = len(str(row[col]))
        if labels != None:
            if len(str(labels[col])) > columnLen[col]:
                columnLen[col] = len(str(labels[col]))
    

    row = "┌"
    for col in range(amountColumn):
        row += "─" * (columnLen[col] +2)
        if col != amountColumn -1:
            row += "┬"
    row += "┐"
    table += row + "\n"

    if labels != None:
        row = "│"
        for col in range(amountColumn):
            if centered == False:
                padding = columnLen[col] - len(str(labels[col]))
                row += " " + str(labels[col]) + " " * padding + " "
            else: 
                padding = columnLen[col] - len(str(labels[col]))
                padding /=2
                row += " " + " " * math.floor(padding) + str(labels[col]) + " " * math.ceil(padding) + " "
            row += "│"
        table += row + "\n"
        

        row = "├"
        for col in range(amountColumn):
            row += "─" * (columnLen[col] +2)
            if col != amountColumn -1:
                row += "┼"
        row += "┤"
        table += row + "\n"

        

    for list in rows:
        row = "│"
        for col in range(amountColumn):
            if centered == False:
                padding = columnLen[col] - len(str(list[col]))

                row += " " + str(list[col]) + " " * padding + " "
            else: 
                padding = columnLen[col] - len(str(list[col]))
                padding /=2
                row += " " + " " * math.floor(padding) + str(list[col]) + " " * math.ceil(padding) + " "
            row += "│"
        table += row + "\n"

    row = "└"
    for col in range(amountColumn):
        row += "─" * (columnLen[col] +2)
        if col != amountColumn -1:
            row += "┴"
    row += "┘"
    table += row + "\n"

    
    return table

print(make_table(
    rows=[['Apple', 5, 70, 'Red', 76], 
    ['Banana', 3, 5, 'Yellow', 8],
    ['Cherry', 7, 31, 'Red', 92], 
    ['Kiwi', 4, 102, 'Green', 1], 
    ['Strawberry', 6, 134, 'Red', 28]],
    
    
    centered=True
))
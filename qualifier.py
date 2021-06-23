def make_table(rows, labels = None, centered = False):
    import math
    table = []
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    :   │ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘
    """
    columnLen = 0
    for row in rows:
        for item in row:
            if len(str(item)) > columnLen:
                columnLen = len(str(item))
    for item in labels:
        if len(str(item)) > columnLen:
            columnLen = len(str(item))
    
    #columnLen is longest amount of chr in items
    amountRow = len(rows) #amount of items in row
    amountColumn = len(rows[0]) #amount of items in column

    row = "┌"
    for _ in range(columnLen+1) :
        row += "─"
    if amountRow > 1:
        for _ in range(amountColumn - 1):
            row += "┬"
            for _ in range(columnLen+1):
                row += "─"     
    row += "┐"
    
    table.append(row)

    if labels != None:
        row = "│"
        for item in labels:
            if centered == False:
                row += " " + str(item)
                extraSpace = columnLen - len(str(item))
                for _ in range(extraSpace):
                    row += " "
            else:
                extraSpace = columnLen - len(str(item))
                padding = extraSpace / 2
                print("padding len " +str(padding))
                for _ in range(math.floor(padding)):
                    row += " "
                row += " " + str(item)
                for _ in range(math.ceil(padding)):
                    row += " "
            row += "│"
        table.append(row)
        row = "│"
        for _ in range(columnLen+1) :
            row += "─"
        if amountRow > 1:
            for _ in range(amountColumn - 1):
                row += "┼"
                for _ in range(columnLen+1):
                    row += "─"     
        row += "│"
        table.append(row)

    for list in rows:
        row = "│"
        for item in list:
            if centered == False:
                row += " " + str(item)
                extraSpace = columnLen - len(str(item))
                for _ in range(extraSpace):
                    row += " "
            else:
                extraSpace = columnLen - len(str(item))
                padding = extraSpace / 2
                print("padding len " +str(padding))
                for _ in range(math.floor(padding)):
                    row += " "
                row += " " + str(item)
                for _ in range(math.ceil(padding)):
                    row += " "
            row += "│"
        table.append(row)
    
    row = "└"
    for _ in range(columnLen+1) :
        row += "─"
    if amountRow > 1:
        for _ in range(amountColumn - 1):
            row += "┴"
            for _ in range(columnLen+1):
                row += "─"     
    row += "┘"
    
    table.append(row)
    
    for x in table:
        print(x)

    


make_table(
    rows=[
        ["Ducky Yellow", 3],
        ["Ducky Dave", 12],
        ["Ducky Tube", 7],
        ["Ducky Lemon", 1]
    ],
    labels=["Name", "Duckiness"],
    centered=False
)

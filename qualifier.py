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
    longestLen = 0
    amountColumn = 0
    amountRow = 0
    for row in rows:
        amountRow += 1
        for item in row:
            amountColumn += 1
            if len(str(item)) > longestLen:
                longestLen = len(str(item))  #find the longest length of all words and then set that as the length of columns
    for item in labels:
        if len(str(labels)) > longestLen:
            longestLen = len(str(labels))  #find the longest length of all words and then set that as the length of columns
    columnLen = longestLen + 2 #add two for the start space and end space
    print("col len " +str(columnLen))
    amountColumn = int(amountColumn / amountRow)

    row = "┌"
    for _ in range(columnLen):
        row += "─"
    if amountRow > 1:
        for _ in range(amountColumn - 1):
            row += "┬"
            for _ in range(columnLen):
                row += "─"     
    row += "┐"
    
    table.append(row)

    if labels != None:
        row = "│"
        for item in labels:
            if centered == False:
                row += " " + str(item)
                extraSpace = columnLen - len(item)
                for _ in range(extraSpace):
                    row += " "
            else:
                extraSpace = columnLen - len(item)
                padding = extraSpace / 2
                print("padding len " +str(padding))
                for _ in range(math.floor(padding)):
                    row += " "
                row += " " + str(item)
                for _ in range(math.ceil(padding)):
                    row += " "
            row += "│"
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
    centered=True
)

import csv

data = []
with open('C:/Users/Asus/Desktop/players.csv', "r", encoding="utf-8") as f:
    reader_obj = csv.reader(f)
    for row in reader_obj:
        # assign a to "highest market value in eur"
        a = str(row[13])

        # ignore the header
        if a == "highest_market_value_in_eur":
            print(a)
        # ignore empyt cells
        elif a == "":
            print("empty")
        # get the ones greater than 20m eur
        elif float(a) >= 20000000.0:
            data.append(row[-1])


with open("data2.txt", "w", encoding="utf-8") as f:
    for i in range(28464):
        #line below gives variable declaration in JS
        f.write(f"let obj{i} = \"{data[i]}\";\n")

        #line below gives variable list in JS
        #f.write(f"obj{i}, ")


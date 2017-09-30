from openpyxl import load_workbook
import media as m
import movies_showcase as BUILD

xlwb = load_workbook("assets\moviesdb.xlsx")
xlws = xlwb["movies"]
movies = []

print(m.Movie.__doc__)

# Find number of items in xlws
max_row = 0
while(True):
    if(xlws["A" + str(max_row + 1)].value == "***"):
        break
    max_row += 1

# Compile items from xlws into "movies[]"
for r in range(1, max_row+1):
    movies.append(
        m.Movie(str(xlws["A" + str(r)].value),
                str(xlws["B" + str(r)].value),
                str(xlws["C" + str(r)].value),
                str(xlws["D" + str(r)].value),
                str(xlws["E" + str(r)].value),
                str(xlws["F" + str(r)].value),
                str(xlws["G" + str(r)].value),
                str(xlws["H" + str(r)].value)))
    print("Movie Added: " + xlws["A" + str(r)].value)

BUILD.open_movies_page(movies)

import csv

a = ["Top Gun", "Risky Business", "Minority Report"]
b = ["Titanic", "The Revenant", "Inception"]
c = ["Training Day", "Man on Fire", "Flight"]

with open("st.csv", "w", newline ="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(a)
    w.writerow(b)
    w.writerow(c)

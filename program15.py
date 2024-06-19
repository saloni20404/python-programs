# Program to read data from a CSV file and print it to the console
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(", ".join(row))

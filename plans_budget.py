import datetime

def create_plans(string):
  
    pl = open("plans.txt", "a", encoding="utf-8")
    pl.write("\n")
    pl.write(string)
    pl.close()

def show_plans():
    pl = open("plans.txt", "r", encoding="utf-8")
    str_pl = pl.read()
    pl.close()
    return str_pl
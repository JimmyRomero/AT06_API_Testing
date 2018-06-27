def days_in_month(name_of_month):
    monthDict = {
        "January": "31",
        "February": "28",
        "March": "31",
        "April": "30",
        "may": "31",
        "June": "30",
        "July": "31",
        "August": "31",
        "September": "30",
        "October": "31",
        "November": "30",
        "December": "31"
    }
    if monthDict.get(name_of_month):
        print(monthDict[name_of_month])
    else:
        print("None")


days_in_month("January")
days_in_month("February")
days_in_month("April")
days_in_month("December")
days_in_month("It is not a valid month")

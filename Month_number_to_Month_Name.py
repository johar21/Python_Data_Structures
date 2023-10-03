def f_replace_month(input_list):
    dic_month = {"01": "Jan", "02": "Feb", "03": "Mar"}
    l = []
    for i in input_list:
        month_number = i.split("-")
        month_name = dic_month[month_number[1]]
        l.append(month_number[0] + "-" + month_name + "-" + month_number[2])
    return l


lst_dates = ["01-01-2020", "21-03-2020", "22-02-2020"]
print(f_replace_month(lst_dates))

start_date = "19010101"
end_date = "20001231"
month_days = {
    1: "31",
    2: "28",
    3: "31",
    4: "30",
    5: "31",
    6: "30",
    7: "31",
    8: "31",
    9: "30",
    10: "31",
    11: "30",
    12: "31",
}


def add_day(date_str):
    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[6:]
    if int(day) == int(month_days[int(month)]):
        day_update = "1"
        if int(month) != 12:
            month_update = str(int(month) + 1)
            if int(month_update) < 10:
                month_update = "0" + month_update
            year_update = year
        else:
            month_update = "01"
            year_update = str(int(year) + 1)
    else:
        day_update = str(int(day) + 1)
        month_update = month
        year_update = year
    returned_date = year_update + month_update + day_update
    return returned_date


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False


if __name__ == "__main__":
    curr_date = start_date
    curr_day = 2

    end_date = add_day(end_date)
    count = 0

    while curr_date != end_date:
        year = curr_date[:4]
        month = curr_date[4:6]
        day = curr_date[6:]
        if int(day) == 1 and curr_day == 0:
            count += 1
        if leap_year(int(year)):
            month_days[2] = "29"
        else:
            month_days[2] = "28"

        curr_day = (curr_day + 1) % 7
        curr_date = add_day(curr_date)

    print(count)

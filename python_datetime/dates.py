from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y")  # 01/11/17
print(date_str)

birthday = "1-May-12"
parsted_birthday = datetime.strptime(birthday, "%d-%b-%y")
birthdate_str = parsted_birthday.strftime("%m/%d/%y")

print(birthdate_str)

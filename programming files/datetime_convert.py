from datetime import datetime
# Adding Comment
date_str = "03-2022-17 30:45:10"
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
formatted_date = date_obj.strftime('%m/%Y/%d %M:%S:%H')
print(formatted_date)

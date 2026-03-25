time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = time_string.split(',')
print(time_list)

total_minutes = 0
for item in time_list:
    parts = item.split()
    print(parts)

    for sub_item in parts:
        if 'h' in sub_item:
            value = int(sub_item.replace('h', ''))
            total_minutes += value * 60

        elif 'm' in sub_item:
             value = int(sub_item.replace('m', ''))
             total_minutes += value

        elif 's' in sub_item:   
            value = int(sub_item.replace('s', ''))  
            total_minutes += value // 60
print(total_minutes)            



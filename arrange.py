###
###
### arrange.py - This script clears the raw data and writes to hour_data.csv also adding a new column, minutes since 00.00.0000:00.00.00
###
###


input_file = open('raw_data.txt', 'r')
input_lines = input_file.readlines(0)[1:]

final_lines = ['"year","doy","h","m","velocity","density","temperature","minutes"\n']

hour_data = open('hour_data.csv','w')

for line in input_lines:
    if '999' not in line:
        line_parts = line.split()
        line_parts[-1] = line_parts[-1][:-1]
        line_parts.append(int(line_parts[0])*525949 + int(line_parts[1])*1440 + int(line_parts[2])*60 + int(line_parts[3]))
        for i in range(len(line_parts)):
            line_parts[i] = f'"{line_parts[i]}"'
        final_lines.append(','.join(line_parts) + "\n")
        
hour_data.writelines(final_lines)

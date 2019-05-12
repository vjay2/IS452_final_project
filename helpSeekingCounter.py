import csv
import pprint

#read in the file, by row, adding each row but the header into the "rows" list
rows = []
with open('TQ_AC_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    first_row = True
    for row in reader:
        if not first_row:
            rows.append(row)
        else:
            first_row = False

#initialize all_data dictionary
all_data = {}

#make a function to process the rows (see narrative for more details on each step)
def process_row(row):
    user_id = row[4]
    TQ = row[6]
    AC = row[5]

    k = user_id
    if k not in all_data.keys():
        all_data[k] = {"TQ_0_count":0, "TQ_1_count":0, "TQ_2_count":0,
                       "TQ_3_count":0, "AC_0_count":0, "AC_1_count":0, "AC_2_count":0,
                       "AC_3_count":0, "count":0}
    this_data = all_data[k]

    this_data["count"] += 1
    if TQ == "0":
        this_data["TQ_0_count"] += 1
    if TQ == "1":
        this_data["TQ_1_count"] += 1
    if TQ == "2":
        this_data["TQ_2_count"] += 1
    if TQ == "3":
        this_data["TQ_3_count"] += 1
    if AC == "0":
        this_data["AC_0_count"] += 1
    if AC == "1":
        this_data["AC_1_count"] += 1
    if AC == "2":
        this_data["AC_2_count"] += 1
    if AC == "3":
        this_data["AC_3_count"] += 1

#go back to each row in the "rows" list where each comment info line is stored
#if the line isn't empty, process it with the process_row function
for row in rows:
    if len(row) > 0:
        process_row(row)

#make output file
output_file = open("counted_file.csv", "w")

#make headers
output_file.write("user_id, TQ_0, TQ_1, TQ_2, TQ_3, AC_0, AC_1, AC_2, AC_3, count\n")

#for each user_id within the master dictionary, make easy-to-work-with variables for each of the accumulated counts
for k in all_data.keys():
    (user_id) = k
    this_data = all_data[k]
    TQ_0 = this_data["TQ_0_count"]
    TQ_1 = this_data["TQ_1_count"]
    TQ_2 = this_data["TQ_2_count"]
    TQ_3 = this_data["TQ_3_count"]
    AC_0 = this_data["AC_0_count"]
    AC_1 = this_data["AC_1_count"]
    AC_2 = this_data["AC_2_count"]
    AC_3 = this_data["AC_3_count"]
    count = this_data["count"]

    #write these counts and the user_id to the file
    output_file.write(str(user_id) + ',' + str(TQ_0) + ',' + str(TQ_1) + ',' +
                      str(TQ_2) + ',' + str(TQ_3) + ',' + str(AC_0) + ',' +
                      str(AC_1) + ',' + str(AC_2) + ',' + str(AC_3) + ',' +
                      str(count) + '\n')
output_file.close()

#making a change that can be pushed

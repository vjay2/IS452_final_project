import csv
import pprint

rows = []
with open('TQ_AC_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    first_row = True
    for row in reader:
        if not first_row:
            rows.append(row)
        else:
            first_row = False

pprint.pprint(rows)

all_data = {}
def process_row(row):
    # Change #1: What row is your field in?
    user_id = row[4]
    TQ = row[6]
    AC = row[5]

    # Change #2: Pack fields into a key -- data will be stored under this key
    k = user_id
    if k not in all_data.keys():
        all_data[k] = {"TQ_0_count":0, "TQ_1_count":0, "TQ_2_count":0,
                       "TQ_3_count":0, "AC_0_count":0, "AC_1_count":0, "AC_2_count":0,
                       "AC_3_count":0, "count":0}
    this_data = all_data[k]

    this_data["count"] += 1
    if this_data["count"] == 600:
        print(row)
    #print(TQ)
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

for row in rows:
    if len(row) > 0:
        process_row(row)

output_file = open("counted_file.csv", "w")

# Change #3: Write a header for your field here -- this is what will appear in your csv's headers
output_file.write("user_id, TQ_0, TQ_1, TQ_2, TQ_3, AC_0, AC_1, AC_2, AC_3, count\n")

for k in all_data.keys():
    # Change #4: Unpack your fields from the key. They must be in the same order you packed them into the key above.
    #(pp, type_field, dist_bin, congruence_bin) = k
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

    # Change #5: Write out each of your values for every line of the csv.
    output_file.write(str(user_id) + ',' + str(TQ_0) + ',' + str(TQ_1) + ',' +
                      str(TQ_2) + ',' + str(TQ_3) + ',' + str(AC_0) + ',' +
                      str(AC_1) + ',' + str(AC_2) + ',' + str(AC_3) + ',' +
                      str(count) + '\n')
output_file.close()

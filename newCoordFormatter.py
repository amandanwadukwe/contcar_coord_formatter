import csv  


#Make each line of in a coords txt file into an item  in an array
lines = []

with open('coOrds220928.txt') as coords:
    while True:
        line = coords.readline()
        if not line:
            break
        lines.append(line.strip())




def filter_line(line_string, cond_num):
    arrayed_and_filtered = []
    for occurence in line_string.split(" "):
        if len(occurence) > cond_num:
            arrayed_and_filtered.append(occurence)
    return arrayed_and_filtered

v1 = filter_line(lines[2], 0)
v2 = filter_line(lines[3], 0)
v3 = filter_line(lines[4], 0)
elements = []
number_of_atoms = []
el_and_atoms_list = []


#Extract the number of atoms of each element
number_of_atoms = filter_line(lines[6], 0)

#Extract all the elements into the array called "elements"
elements = filter_line(lines[5], 0)

for index in range(len(number_of_atoms)):
    el_and_atoms_list.append(elements[index])
    el_and_atoms_list.append(int(number_of_atoms[index]))



item = iter(el_and_atoms_list)
el_and_atoms_dict = dict(zip(item, item))


def calculate_position_of_each_atom(el, start_point, end_point):
    positions = []
    
    for index in range(len(lines)):
        if index <= end_point and index > start_point:
            x_pos = float(filter_line(lines[index], 1)[0]) * float(v1[0]) + float(filter_line(lines[index], 1)[1]) * float(v2[0]) + float(filter_line(lines[index], 1)[2]) * float(v3[0])
            y_pos = float(filter_line(lines[index], 1)[0]) * float(v1[1]) + float(filter_line(lines[index], 1)[1]) * float(v2[1]) + float(filter_line(lines[index], 1)[2]) * float(v3[1])
            z_pos = float(filter_line(lines[index], 1)[0]) * float(v1[2]) + float(filter_line(lines[index], 1)[1]) * float(v2[2]) + float(filter_line(lines[index], 1)[2]) * float(v3[2])

            positions.append([x_pos, y_pos, z_pos])
    
    return positions
                
    # writer = csv.writer(result, delimiter=",")


with open('newCoordFormat.xyz', 'w', encoding='UTF8') as newCoordFormat:
    writer = csv.writer(newCoordFormat, delimiter=" ")

    header = [77]
    writer.writerow(header)


    # write the data
    for data in calculate_position_of_each_atom("C",77,121):
        writer.writerow(data)

    for data in calculate_position_of_each_atom("H",121, 149):
        writer.writerow(data)

    for data in calculate_position_of_each_atom("N", 149, 153):
        writer.writerow(data)

    for data in calculate_position_of_each_atom("Zn", 153, 154):
        writer.writerow(data)

    
print(elements)

import csv  
import sys

def filter_line(line_string, cond_num):
            arrayed_and_filtered = []
            for occurence in line_string.split(" "):
                if len(occurence) > cond_num:
                    arrayed_and_filtered.append(occurence)
            return arrayed_and_filtered

def calculate_position_of_each_atom(array_of_atom_details):
            positions = []
            #  where the endpoint = array_of_atom_details[2], startpoint = array_of_atom_details[1] and array_of_atom_details[0] is just a label
            for index in range(len(lines)):
                if index <= array_of_atom_details[2] and index > array_of_atom_details[1]:
                    x_pos = float(filter_line(lines[index], 1)[0]) * float(v1[0]) + float(filter_line(lines[index], 1)[1]) * float(v2[0]) + float(filter_line(lines[index], 1)[2]) * float(v3[0])
                    y_pos = float(filter_line(lines[index], 1)[0]) * float(v1[1]) + float(filter_line(lines[index], 1)[1]) * float(v2[1]) + float(filter_line(lines[index], 1)[2]) * float(v3[1])
                    z_pos = float(filter_line(lines[index], 1)[0]) * float(v1[2]) + float(filter_line(lines[index], 1)[1]) * float(v2[2]) + float(filter_line(lines[index], 1)[2]) * float(v3[2])

                    positions.append([x_pos, y_pos, z_pos])
            
            return positions

def get_all_output(array_of_elment_start_and_end_points):
    all_data = []
    for data in array_of_elment_start_and_end_points:
        for positions in calculate_position_of_each_atom(data):
            all_data.append(positions)

    return all_data

for file_index in range(len(sys.argv)):
    #For each file
    if( file_index > 0):
        file_detials = [["C",77,121], ["H",121, 149],["N", 149, 153],["Zn", 153, 154]]
        #Make each line of in a coords txt file into an item  in an array
        lines = []
        with open(sys.argv[file_index]) as coords:
            while True:
                line = coords.readline()
                if not line:
                    break
                lines.append(line.strip())

        v1 = filter_line(lines[2], 0)
        v2 = filter_line(lines[3], 0)
        v3 = filter_line(lines[4], 0)
                        
        #Create a file
        with open(sys.argv[file_index][slice(0, -4)] + ".xyz", 'w', encoding='UTF8') as newCoordFormat:
            writer = csv.writer(newCoordFormat, delimiter=" ")

            # write the data
            header = []
            header.append(len(get_all_output(file_detials)))
            writer.writerow(header)

            for output in get_all_output(file_detials):
                writer.writerow(output)

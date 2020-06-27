import sys
import random

def get_lines_count(filepath):
    counter = 0
    with open(filepath,'r',newline='\n') as f_in:
        for _ in f_in:
            counter +=1
    return counter

def get_lines_marker_set(total_file_lines, lines_number_to_mark):
    marker_set = set()
    while len(marker_set) < lines_number_to_mark:
        marker_set.add(random.randint(0,total_file_lines-1))
    return marker_set

def mark_file(f_in_path, f_out_path, marker_set):
    with open(f_in_path,'r',newline = '\n') as f_in, open(f_out_path, 'w', newline = '\n') as f_out:
        for counter, line_in in enumerate(f_in):
            marker = '1' if counter in marker_set else '0'
            line_out = marker + '\t' + line_in
            f_out.write(line_out)

if len(sys.argv) != 4:
    print("usage:   python add_human_ann_column.py f_in_path f_out_path lines_to_mark_number")
    print("example: python add human_ann_column.py dev-0/in.tsv dev-0/in-for-humans.tsv 100")
    sys.exit(1)

f_in_path = sys.argv[1]
f_out_path = sys.argv[2]
lines_to_mark_number = int(sys.argv[3])

lines_count = get_lines_count(f_in_path)

if lines_to_mark_number > lines_count:
    print("markers number exceed line count")
    sys.exit(1)

marker_set = get_lines_marker_set(lines_count, lines_to_mark_number)
mark_file(f_in_path, f_out_path, marker_set)

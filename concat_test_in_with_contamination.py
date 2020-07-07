f_contamination_flag = open('test-A/contamination_flag.tsv', newline='\n')
f_in = open('test-A/in.tsv', newline='\n')

f_out = open('test-A/in_with_contamination.tsv','w', newline= '\n')

for contam_flag, line in zip(f_contamination_flag, f_in):
    contam = contam_flag.rstrip()
    contam = 'LINE_NOT_CONTAMINATED' if contam=='0' else 'LINE_CONTAMINATED'
    f_out.write(contam + '\t' + line)

f_out.close()

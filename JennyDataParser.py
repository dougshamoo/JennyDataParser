__author__ = 'dougs_000'


def get_mean(data):
    """
    Takes a frequency dictionary
    Returns the mean of the data
    """
    total = 0
    for key in data:
        total += (key * data[key])
    return float(total) / sum(data.values())



in_downpay = 'downpaymentratio.txt'
in_highestmonth = 'highestmonthlyinstallment.txt'
in_loanterm = 'loanterm.txt'

out_downpay = "downpaymentratio_output.txt"
out_highestmonth = 'highestmonthlyinstallment_output.txt'
out_loanterm = 'loanterm_output.txt'

inputdata = in_loanterm
outputdata = out_loanterm
in_file = open(inputdata, 'r')
out_file = open(outputdata, 'w')

data_dict = {}

for line in in_file:
    line_data = line.split()
    group = int(line_data[0])
    value = int(line_data[1])
    if group in data_dict:
        data_dict[group] += value
    else:
        data_dict[group] = value
in_file.close()

total_val = sum(data_dict.values())
for g in sorted(data_dict.keys()):
    percentage = float(data_dict[g]) / total_val
    out_file.write('{0}\t{1}\t{2}\n'.format(str(g), str(data_dict[g]), str(percentage)))

out_file.write('\nThe mean is: {0}\n'.format(str(get_mean(data_dict))))
out_file.close()


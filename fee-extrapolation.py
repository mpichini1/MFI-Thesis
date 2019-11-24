import read_pdf
import re

text = read_pdf.pdfreading()
print(text)


entry_charge = re.search("[E-e][N-n][T-t][R-r][Y-y]\s?[C-c][H-h][A-a][R-r][G-g][E-e][S-s]?\s?(\d[.]\d\d%|N/A)", text)

if entry_charge:
    print(entry_charge.group(0))
else:
    print("error")


exit_charge = re.search("[E-e][X-x][I-i][T-t]\s?[C-c][H-h][A-a][R-r][G-g][E-e][S-s]?\s?(\d[.]\d\d%|N/A)", text)

if exit_charge:
    print(exit_charge.group(0))
else:
    print("error")

ongoing_charges = re.search("[O-o][N-n][G-g][O-o][I-i][N-n][G-g]\s?[C-c][H-h][A-a][R-r][G-g][E-e][S-s]?\s?(\d[.]\d\d%|N/A)", text)

if ongoing_charges:
    print(ongoing_charges.group(0))
else:
    print("error")

performance_fee = re.search("[P-p][E-e][R-r][F-f][O-o][R-r][M-m][A-a][N-n][C-c][E-e]\s?[F-f][E-e][E-e][S-s]??\s?(\d[.]\d\d%|N/A|[N-n][O-o][N-n][E-e])", text)

if performance_fee:
	print(performance_fee.group(0))
else:
	print("error")
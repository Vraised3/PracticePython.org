from bokeh.plotting import figure, show, output_file
import numpy as np
import json
import calendar

with open('scientist_birthdays.json', 'r') as SB:
    SB = json.load(SB)

x = [scientist for scientist in SB.keys()]
y = [int(SB.get(val)[:2]) for val in SB.keys()]
# y = [calendar.month_name[int(month[:2])] for month in y]

f = figure()
f.vbar(x=x, top=y, width=0.5)

show(f)


# x = np.linspace(1, 10)
# y = np.sin(x)

# f = figure()

# f.vbar(x=x, top=y, width=0.5)

# show(f)

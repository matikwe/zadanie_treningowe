import pandas as pd
import matplotlib.pyplot as plt
import html5lib

def show_max_or_min(data, column, minimum=False):
    description = data[column].describe()
    if minimum:
        return description['min']
    return description['max']

data = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states',flavor='html5lib')
states = data[0]
print(states)

#A
maximum = states[('Numberof Reps.', 'Numberof Reps.')].max()
minimum = states[('Numberof Reps.', 'Numberof Reps.')].min()

max_states = states[states[('Numberof Reps.', 'Numberof Reps.')] == maximum][('Name &postal abbs. [1]', 'Name &postal abbs. [1]')]
min_states = states[states[('Numberof Reps.', 'Numberof Reps.')] == minimum][('Name &postal abbs. [1]', 'Name &postal abbs. [1]')]

print("Max: ", maximum)
print(max_states)

print("Min: ", minimum)
print(min_states)

#B
population = states[('Population[B][3]', 'Population[B][3]')]
area = states[('Total area[4]', 'km2')]

states[('stat', 'g')] = population / area
states.plot(x=('Name &postal abbs. [1]', 'Name &postal abbs. [1]'), y=('stat', 'g'), kind='bar')
plt.tight_layout()
plt.show()

#C
states[('stat', 'e')] = pd.to_datetime(states[('Established[A]', 'Established[A]')])
states.sort_values(('stat', 'e'), ascending=True, ignore_index=True, inplace=True)
print(states[[('Name &postal abbs. [1]', 'Name &postal abbs. [1]'), ('Established[A]', 'Established[A]')]])

#D
maximum = show_max_or_min(states, ('Population[B][3]', 'Population[B][3]'))
print("Max:", maximum)

minimum = show_max_or_min(states, ('Population[B][3]', 'Population[B][3]'), True)
print("Max:", minimum)



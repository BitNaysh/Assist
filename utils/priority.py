import pandas as pd 

data = pd.read_csv('dataset.csv')

# priority_dict = {(1, 1): 4, (1, 2): 4, (1, 3): 5, (1, 4): 5, (1, 5): 5, (2, 1): 3, (2, 2): 3, (2, 3): 4, (2, 4): 5, (2, 5): 5, (3, 1): 2, (3, 2): 2, (3, 3): 3, (3, 4): 4, (3, 5): 4, (4, 1): 1, (4, 2): 1, (4, 3): 2, (4, 4): 3, (4, 5): 3}
priority_dict = {}

for i in range(len(data)):
    priority_dict[(data['credits'][i], data['grade'][i])] = data['priority'][i]


print(priority_dict)
def get_priority(credits, grade):
    return priority_dict[(credits, grade)]
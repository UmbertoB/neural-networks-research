import pandas as pd
from dataset_path import dataset_path
from pathlib import Path

yesDir = dataset_path + '/train/yes'
paths = []
for ext in ['*.jpg', '*.jpeg', '*.JPG', '*.png']:
    paths = [*paths, *[path.parts[-3:] for path in Path(dataset_path).rglob(ext)]]

df = pd.DataFrame(data=paths, columns=['Dataset', 'State', 'Path'])
df.to_csv('dataframe.csv')

pie = df.groupby(['Dataset']).count().plot(kind='pie', y='State', autopct='%1.0f%%')

fig = pie.get_figure()
fig.savefig("plots/dataset-pie.png")

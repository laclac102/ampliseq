#!/usr/bin/env python

import sys
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA

usage = """beta_diversity_plot.py <raw_data.tsv> <output_file_name>"""

#--- Check and read arguments ---#
if len(sys.argv) != 3:
    exit("Usage: " + usage )

OUTFILE_NAME=sys.argv[2]

df = pd.read_csv(sys.argv[1], sep="\t", skiprows=0, index_col=0)
# %%
cat = sorted(set(df['SubjectID1']).union(df['SubjectID2']))
df=(df.assign(SubjectID1=pd.Categorical(df['SubjectID1'],
                                  categories=cat,
                                  ordered=True),
           SubjectID2=pd.Categorical(df['SubjectID2'],
                                  categories=cat,
                                  ordered=True),
           )
    .pivot_table(index='SubjectID1',
                 columns='SubjectID2',
                 values='Distance',
                 dropna=False, fill_value=0)
    .pipe(lambda x: x+x.values.T)
)

# %%
X= df[df.columns]

# %%

pca = PCA()
components = pca.fit_transform(X)

# %%
fig = px.scatter_3d(components, x=0, y=1, z=2, color=df.index)
# %%
fig.write_html(OUTFILE_NAME + '_plot_mqc.html')
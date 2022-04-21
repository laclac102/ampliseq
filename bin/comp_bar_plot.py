#!/usr/bin/env python

import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

usage = """comp_bar_plot.py <input.tsv> <level> <output_file>"""

#--- Check and read arguments ---#
# if len(sys.argv) != 3:
#     exit("Usage: " + usage )

# file_name   = sys.argv[1]
# output_name = sys.argv[3]
for i in range(2,4):
    file_name = "rel-table-{}.tsv".format(i)
    df = pd.read_csv(file_name, sep="\t", skiprows=1)
# df.columns=['OTU','sampleID_1','sampleID_1a','sampleID_2','sampleID_2a']
    df=df.set_index('#OTU ID')
    fig = px.bar(df.T, x=df.columns, y=df.index)
    fig.update_layout(
        xaxis_title="<b> Sample <b>",
        yaxis_title="<b> Relative abundance <b>",
        legend_title="<b> Composition bar plot level <b>" + str(i)
        )                # fig.show()
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
                buttons=list(
                    [dict(label = 'All',
                        method = 'update',
                        args = [{'visible': [True]*9 },
                                {'title': 'All',
                                'showlegend':True}])]))]
    )
fig.write_html("Composition_bar_plot_mqc.html")

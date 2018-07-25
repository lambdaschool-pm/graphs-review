import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, Oval, Range1d, LabelSet, Label, ColumnDataSource
from bokeh.palettes import Spectral8

from graph import *

WIDTH = 800
HEIGHT = 800  # TODO make a rectangle instead of square 640 x 400
CIRCLE_SIZE = 30

graph_data = Graph()
# graph_data.debug_create_test_data()
graph_data.randomize(3, 5, 150, 60)
graph_data.get_connected_components()

N = len(graph_data.vertexes)
node_indices = list(range(N))

label_source = ColumnDataSource(data=dict(x=[vertex.pos['x'] for vertex in graph_data.vertexes], y=[
                                vertex.pos['y'] for vertex in graph_data.vertexes], value=[vertex.value for vertex in graph_data.vertexes]))
#labels = LabelSet(x='x', y='y', text='value', level='glyph', x_offset=-6, y_offset=-10, source=label_source, render_mode='canvas')
labels = LabelSet(x='x', y='y', text='value', level='overlay',
                  text_align='center', text_baseline='middle', source=label_source, render_mode='canvas')

start = []
end = []

color_list = []
for i, vertex in enumerate(graph_data.vertexes):
    color_list.append(vertex.color)
    for edge in vertex.edges:
        j = graph_data.vertexes.index(edge.destination)
        start.append(i)
        end.append(j)

#plot = figure(title='Graph Layout Demonstration', x_range=(-1.1, 1.1), y_range=(-1.1, 1.1), tools='', toolbar_location=None)
plot = figure(x_range=(
    0, WIDTH), y_range=(0, HEIGHT), tools='', toolbar_location=None)
#plot.axis.visible = False
#plot.grid.grid_line_color = None
#plot.outline_line_color = None
graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
#graph.node_renderer.data_source.add(Spectral8, 'color')
graph.node_renderer.data_source.add(color_list, 'color')
#graph.node_renderer.glyph = Oval(height=25, width=25, fill_color='color')
graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, fill_color='color')

#graph.edge_renderer.data_source.data = dict(start=[0]*N, end=node_indices)
graph.edge_renderer.data_source.data = dict(start=start, end=end)
# start of layout code

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.add_layout(labels)

output_file('graph.html')
show(plot)

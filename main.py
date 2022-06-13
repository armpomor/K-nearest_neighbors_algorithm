import plotly.graph_objs as go
from random import sample
from math import dist


COLORS = {'WHITE': [255, 255, 255], 'BLACK': [0, 0, 0], 'RED': [255, 0, 0], 
          'GREEN': [0, 255, 0], 'BLUE': [0, 0, 255]}
ROW = 20   # количество рядов клеток
COL = 40   # количество столбцов

def nearest_color(color):
    """
    Возвращает класс, к которому принадлежит клетка
    """
    s = {key: dist(value, color) for key, value in COLORS.items()}
    return COLORS.get(min(s, key=s.get))


colors_cells_1 = [[sample(range(0, 256), 3) for i in range(COL)] for j in range(ROW)]

fig_1 = go.Figure(go.Image(z=colors_cells_1))
fig_1.update_layout(title=dict(text='K-nearest neighbors algorithm', font=dict(size=20)), margin=dict(l=0, t=30, b=0, r=0))


colors_cells_2 = [[nearest_color(i) for i in j] for j in colors_cells_1]

fig_2 = go.Figure(go.Image(z=colors_cells_2))
fig_2.update_layout(title=dict(text='K-nearest neighbors algorithm', font=dict(size=20)), margin=dict(l=0, t=30, b=0, r=0))

fig_1.show()
fig_2.show()



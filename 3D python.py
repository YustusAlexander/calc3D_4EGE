# https://plotly.com/python/3d-line-plots/


import plotly.express as px

df = px.data.gapminder().query("country=='Brazil'")

fig = px.line_3d(df, x="gdpPercap", y="pop", z="year")
fig.show()


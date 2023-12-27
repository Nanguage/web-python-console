import micropip
await micropip.install('altair')
await micropip.install('vega_datasets')

import altair as alt

# load a simple dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()

chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)

await api.insertHtml(chart.to_html())

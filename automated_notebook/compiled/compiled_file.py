# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# First Step
import tensorflow
import requests

a = 3

# +
# First Step

from PIL import Image

b = a + 5
image_url = "https://same-project.github.io/SAME-samples/automated_notebook/FaroeIslands.jpeg"
image = Image.open(requests.get(image_url, stream=True).raw)
image.show()

# +
# First Step

import plotly


def some_math(x, z) -> tuple:
    return (x + z, x / z)


# +
# Second Step

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mu = 0
std = 1
x = np.linspace(start=-4, stop=4, num=100)
y = stats.norm.pdf(x, mu, std)
plt.plot(x, y)
plt.show()

# +
# Second Step

import requests
import pandas as pd
import io
import plotly.figure_factory as ff
import chart_studio.plotly as py

url = "https://same-project.github.io/SAME-samples/automated_notebook/test.csv"

r = requests.get(url)
if r.ok:
    data = r.content.decode("utf-8")
    df = pd.read_csv(io.StringIO(data))

df = pd.read_csv("test.csv")

df.describe()
# -


# Third Step
g = some_math(8, 21)

# +
# Fourth Step

print(f"j: {g[0]}")

# +
# Fourth Step

print(f"k: {g[1]}")
# -

def function_0002():
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
    df = None
    
    if r.ok:
        data = r.content.decode("utf-8")
        df = pd.read_csv(io.StringIO(data))

    df.describe()
    # -
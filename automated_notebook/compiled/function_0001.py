def function_0001():
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

    a = 3

    # +
    # First Step

    from PIL import Image

    b = a + 5

    image = Image.open("FaroeIslands.jpeg")
    image.show()

    # +
    # First Step

    import plotly

    def some_math(x, z) -> tuple:
        return (x + z, x / z)

from matplotlib.pyplot import subplots


def plot_slice(x, y, data, figsize=(5, 5), dpi=200):
    fig, ax = subplots(1, 1, figsize=figsize, dpi=dpi)

    ax.pcolormesh(x, y, data.T, shading='auto')

    ax.invert_yaxis()

    return fig, ax

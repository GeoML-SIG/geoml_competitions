from matplotlib.pyplot import subplots


def plot_slice(x, y, data):
    fig, ax = subplots(1, 1, figsize=(7, 7), dpi=200)

    ax.pcolormesh(x, y, data.T)

    ax.invert_yaxis()

    return fig, ax

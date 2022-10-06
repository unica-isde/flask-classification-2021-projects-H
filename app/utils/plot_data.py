import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def generate(labels, values):

    """
    Generate the image
    @param labels: classification labels.
    @param values: prediction scores for the labels.
    @return: the plotted data as a PNG stream of bytes.
    """

    colors = ["r", "g", "b", "c", "m"]

    fig = Figure(figsize=(13, 6), dpi=150)

    axis = fig.add_subplot(1, 1, 1)
    axis.barh(labels, values, color=colors)

    axis.set_title("OUTPUT SCORES")
    axis.set_xlabel("SCORE %")
    axis.set_ylabel("LABEL")
    axis.grid(True)
    axis.invert_yaxis()

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return output.getvalue()

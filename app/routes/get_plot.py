import json
from app import app
from flask import Response, abort

from app.utils import json_data, plot_data


@app.route('/plot/<string:job_id>', methods=['GET'])
def get_plot(job_id):

    """
    Plot data as a PNG file

    @param job_id: job_id Id string of a job.
    @return: the desired plot image or a response error.
    """

    content = json_data.fetch(job_id)

    if content is None:
        abort(404)

    else:
        data_dict = json.loads(content)
        labels, values = zip(*data_dict.items())

        img = plot_data.generate(labels, values)
        return Response(img,
                        mimetype='image/png',
                        headers={'Content-Disposition': 'attachment;filename=plot.png'})

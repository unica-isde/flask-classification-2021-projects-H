from app import app
from flask import Response, abort

from app.utils import json_data


@app.route('/json/<string:job_id>', methods=['GET'])
def get_json(job_id):

    """
    Download JSON data
    @param job_id: Id string of a job.
    @return: the desired JSON file or a response error.
    """

    data = json_data.fetch(job_id)

    if data is None:
        abort(404)

    else:
        return Response(data,
                        mimetype='application/json',
                        headers={'Content-Disposition': 'attachment;filename=data.json'})
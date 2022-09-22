import requests
import json
from flask import url_for


def fetch(job_id, url=None):

    """Fetch the wanted JSON data

    @param job_id: Id of a job.
    @param url: URL from which to retrieve the data.
    @return: the desired JSON data or None.
    """


    if url is None:
        url = 'http://localhost:5000' + \
              url_for('classifications_id', job_id=job_id)

    try:
        request = requests.get(url)

        json_data = request.json()

        data = json.dumps(dict(json_data.get('data')))
        return data


    except Exception as e:

        print(repr(e))
        return None

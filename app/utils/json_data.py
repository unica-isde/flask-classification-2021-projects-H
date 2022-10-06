import json
from config import Configuration

import redis
from rq import Connection, Queue


def fetch(job_id):
    """Fetch the wanted JSON data

    @param job_id: Id of a job.
    @return: the desired JSON data or None.
    """

    redis_url = Configuration.REDIS_URL
    redis_conn = redis.from_url(redis_url)
    with Connection(redis_conn):
        q = Queue(name=Configuration.QUEUE)
        data = {}
        try:

            result = q.fetch_job(job_id).result
            # transform result in a dictionary
            for item in result:
                data[item[0]] = item[1]
            data = json.dumps(data)
            return data

        except:
            return None
e

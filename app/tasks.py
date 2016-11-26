from app.models.FormData import FormData
from app.models.meta import Session
from celery import Celery

celery = Celery(
    broker='sqla+sqlite:///celery_broker.db',
    backend='db+sqlite:///celery_backend.db'
)


@celery.task
def add_record_task(name):
    form_data = FormData(name=name)
    session = Session()
    session.add(form_data)
    session.commit()
    session.close()


@celery.task
def get_records_sync_task():
    session = Session()
    data = session.query(FormData).all()
    session.close()
    return data


if __name__ == '__main__':
    celery.worker_main()

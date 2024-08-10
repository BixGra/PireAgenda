FROM python:3.10

WORKDIR /etc/PireAgenda

COPY . /etc/PireAgenda/.

RUN  pip install --upgrade pip && pip --no-cache-dir install -r /etc/PireAgenda/requirements.txt

ENV PYTHONPATH $PYTHONPATH:$PATH:/etc/PireAgenda/src/

ENV PATH /opt/conda/envs/env/bin:$PATH

ENV PROJECT_PATH /etc/PireAgenda/src/

RUN python src/initialize.py

EXPOSE 8003

ENTRYPOINT gunicorn -b 0.0.0.0:8003 -k uvicorn.workers.UvicornWorker src.main:app --threads 2 --workers 1 --timeout 1000 --graceful-timeout 30
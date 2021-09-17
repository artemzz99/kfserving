FROM python:3.8.12-slim

COPY sklearnserver_custom sklearnserver
COPY kfserving kfserving

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -e ./kfserving
RUN pip install --no-cache-dir -e ./sklearnserver
COPY third_party third_party

ENTRYPOINT ["python", "-m", "sklearnserver"]

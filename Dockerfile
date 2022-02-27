FROM python:3.8


COPY . .
RUN pip install pipenv
RUN pipenv lock && pipenv install --system --deploy


EXPOSE 8080

# Use the ping endpoint as a healthcheck,
# so Docker knows if the API is still running ok or needs to be restarted
HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://localhost:8080/ping || exit 1

CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "8080"]
# script uvicorn service.main:app --host 0.0.0.0 --port 8080
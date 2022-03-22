FROM python
COPY . /app
WORKDIR /app
CMD python SchedulerTest.py




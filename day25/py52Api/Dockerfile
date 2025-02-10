FROM python:3-alpine
WORKDIR /app
ADD ./req.txt /app
RUN pip install -r req.txt
CMD ["python","main_pytest.py"]
FROM python:3.9

WORKDIR /app2
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . . 
CMD [ "python","sold_out.py" ]

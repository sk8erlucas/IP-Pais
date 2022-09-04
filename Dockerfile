# To run:
# docker build -t ippais .
# docker run --rm -it -p 5000:5000 ippais

FROM python:3.10

RUN pip install gspread Flask geocoder flask_cors
COPY ./App /app


ENV ENV=prod

CMD [ "python", "/app/Capotas_Lopez___Pais.py" ]
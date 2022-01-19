FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update
RUN apt-get install -y gcc libavdevice-dev libavfilter-dev libopus-dev libvpx-dev pkg-config netcat

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

RUN chmod +x entrypoint.sh

CMD ./entrypoint.sh

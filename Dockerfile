FROM ubuntu:22.04

WORKDIR /work_directory

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip
RUN pip install dicttoxml
RUN pip install xmltodict
RUN pip install beautifulsoup4
RUN pip install lxml
RUN pip install pyyaml
RUN pip install rec-avro
RUN pip install avro
RUN pip install dataclasses-avroschema
RUN pip install typing_extensions

COPY . .
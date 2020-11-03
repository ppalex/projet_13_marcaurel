# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /marcaurel

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install GCC
RUN apk add build-base
#    
RUN \
    wget https://download.osgeo.org/geos/geos-3.8.1.tar.bz2 \
    && tar xjf geos-3.8.1.tar.bz2 \
    && cd geos-3.8.1 \
    && ./configure \
    && make install \
    && cd ..


RUN \
    apk update \
    && apk add sqlite \
    && apk add sqlite-libs \
    && apk add sqlite-dev
    
# RUN \
#     wget https://sqlite.org/2020/sqlite-autoconf-3330000.tar.gz \
#     && tar -xvzf sqlite-autoconf-3330000.tar.gz \
#     && cd sqlite-autoconf-3330000 \
#     && CFLAGS="-DSQLITE_ENABLE_COLUMN_METADATA=1" \
#     && ./configure \
#     && make \
#     && make install \
#     && cd ..


RUN \
    apk add tiff-dev

RUN \
    wget https://download.osgeo.org/proj/proj-7.1.1.tar.gz \
    && wget https://download.osgeo.org/proj/proj-datumgrid-1.8.tar.gz \
    && tar xzf proj-7.1.1.tar.gz \
    && cd proj-7.1.1 \
    && mkdir nad \
    && cd nad \
    && tar xzf ../../proj-datumgrid-1.8.tar.gz \
    && cd .. \
    && ./configure --without-curl \    
    && make \
    && make install \
    && cd ..

# RUN \
#     wget https://download.osgeo.org/gdal/3.1.4/gdal-3.1.4.tar.gz \
#     && tar xzf gdal-3.1.4.tar.gz \
#     && cd gdal-3.1.4 \
#     && ./configure \
#     && make \
#     && make install \
#     && cd ..


RUN \
    apk add gdal \
    && apk add gdal-dev



# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /marcaurel/
RUN pip install -r requirements.txt

# copy project
COPY . .
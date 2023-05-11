FROM python:3.10.11
#Build args
ARG VCS_REF
ARG BUILD_DATE
# Setting resource quota
ARG MIN_MEM=2G
ARG MAX_MEM=2G

WORKDIR /src
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
#Execution
CMD python app.py
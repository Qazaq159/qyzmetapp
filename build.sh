#!/bin/bash

docker build -t ferkinkz/qyzmetapp.back:latest .

docker login

docker push ferkinkz/qyzmetapp.back:latest

#!/bin/bash

docker run -p 5432:5432 \
           --name postgres_container \
           -e POSTGRES_USER=postgres \
           -e POSTGRES_PASSWORD=password \
           -d postgres




#!/bin/bash

docker run -p 5432:5432 \
           --name some-postgres \
           -e POSTGRES_USER=postgres \
           -e POSTGRES_PASSWORD=password \
           -d postgres




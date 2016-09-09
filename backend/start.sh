#!/bin/bash

set -e
docker build -t riak .
docker run --detach  --publish '8080:8080' --name 'riak-cs' riak

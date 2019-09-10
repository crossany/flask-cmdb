#!/bin/bash
uwsgi --socket 0.0.0.0:80 --protocol=http -w wsgi:app --enable-threads --thunder-lock

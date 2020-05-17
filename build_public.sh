#!/bin/sh

tar --sort=name --mtime='UTC 2020-05-05' -czvf bytecode-docker.tar.gz service

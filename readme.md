resources:

- https://mariokartwii.com/arm64/
- https://cybersandeep.gitbook.io/arm64basicguide/chapter-1-getting-to-know-arm64

- https://austinhenley.com/blog/teenytinycompiler1.html
- https://www.youtube.com/playlist?list=PLUDlas_Zy_qC7c5tCgTMYq2idyyT241qs

- https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/


stack:
- arm64 assembly with linux syscalls.
- runs on a ubuntu container.

how to run:

build the docker container first:
```bash
docker build --platform linux/arm64 -t frog .
```

run the container:
```bash
docker run --platform linux/arm64 frog
```
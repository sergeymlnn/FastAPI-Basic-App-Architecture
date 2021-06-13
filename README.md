## Introduction

The project provides users an application template based on [FastAPI](https://fastapi.tiangolo.com/) for the development of straightforward and flexible web applications.


## Getting Started

Sometimes software engineers build different applications using the same architectural strategies.
The goal of this project is to provide developers an initial project structure, that can be easily extended and shared accross different applications.

[FastAPI](https://fastapi.tiangolo.com/) is a core framework of the application, so the project follows its patterns and techniques to build web applications. 


## Prerequisites

Make sure you have [Docker](https://www.docker.com/) with [Docker Compose](https://docs.docker.com/compose/) and [Git](https://git-scm.com/) installed on your machine to clone and run the application.


## Installing

On the first step we clone the repository to the working directory.

```
git clone https://github.com/sergeymlnn/FastAPI-Basic-App-Architecture.git /path/to/your/directory

```

Once the repository is cloned, you can build and run docker container with the app:

```bash
docker-compose up -d --build
```

**Note:**
    The application runs on port 8003. Make sure this port is free on your machine.

You can easily check docker logs of the container, once it's up and running:

```
docker logs --tail 5 fastapi_base
```

or live-logs

```
docker logs -f fastapi_base
```


## Running the tests

```bash
docker-compose exec web pytest . -v -s
```


## And coding style tests

Running flake8 style checker

```bash
docker exec -it fastapi_base flake8 --max-line-length 10 .
```

Running mypy type checker

```bash
docker exec -it fastapi_base mypy .
```


## Deployment

...


## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - Web framework Used
* [PyTest](https://docs.pytest.org/en/6.2.x/) - Web Framework for Testing
* [aiohttp](https://docs.aiohttp.org/en/stable/) - Asynchronous Web Client For Testing
* [flake8](https://rometools.github.io/rome/) - Style Checker
* [myoy](https://mypy.readthedocs.io/en/stable/) - Types checker


## Contributing

...


## Versioning

The latest available version of the application is 0.1.

## Author

* **Sergey M** - *Initial work* - [prathamlahoti](https://github.com/sergeymlnn)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

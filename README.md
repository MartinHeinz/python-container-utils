# Python Container Utils

[![Build, Test, Lint](https://github.com/MartinHeinz/python-container-utils/actions/workflows/build-test.yml/badge.svg)](https://github.com/MartinHeinz/python-container-utils/actions/workflows/build-test.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/24c484895e18e48c487c/test_coverage)](https://codeclimate.com/github/MartinHeinz/python-container-utils/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/24c484895e18e48c487c/maintainability)](https://codeclimate.com/github/MartinHeinz/python-container-utils/maintainability)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MartinHeinz_python-container-utils&metric=alert_status)](https://sonarcloud.io/dashboard?id=MartinHeinz_python-project-blueprint)

Extra utilities for working with container images. 

## Testing Environment

Two container registries are required to perform tests of copying images. These are set up using `docker` and `docker-compose`, through `make` target:

```bash
make env
```

## Development

- Create virtual environment
- Install dependencies:

```bash
pip install -r requirements.txt
```

- Run tests:

```bash
make test
```

- Build package:

```bash
make build
```

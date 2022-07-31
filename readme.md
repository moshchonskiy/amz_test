### Installation

* clone this repository
* go to the folder with cloned repository
* Install the latest version of Docker CE: https://docs.docker.com/install/
* Install the latest version of docker-compose: https://docs.docker.com/compose/install/
* Build test containers `make build`
* Run test containers `make run`

### Test running
* `make test`
  * Make sure your testing containers are built and running `make run`

### Commands

Use `make` or `make help` to check what build in commands are available.
The most important commands:

- `make build`: prepare local context and build Docker container, use it initially and after each change in dependencies and Docker configuration
- `make run`: start testing and reporting Docker containers
- `make stop`: stop testing and reporting Docker containers
- `make test`: run test
- `make clean`: clean cache, report and logs directries
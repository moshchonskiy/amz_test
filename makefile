.DEFAULT_GOAL := help

.PHONY: build
build: ## build containers
	@printf "=========Building Docker containers=========\n\n"
	@docker pull selenoid/chrome:101.0
	@docker pull selenoid/chrome:101.0
	@docker pull aerokube/selenoid-ui
	@docker-compose build

.PHONY: run
run: ## run containers
	@printf "=========Running Docker containers=========\n\n"
	@docker-compose up -d

.PHONY: stop
stop: ## stop containers
	@printf "=========Stopping Docker containers=========\n\n"
	@docker-compose down -v

.PHONY: test
test-api: ## run tests
	@printf "=========Running tests=========\n\n"
	@docker-compose exec automation-tests sh -c "pytest ."

.PHONY: clean
clean: ## clean reports/logs
	@printf "=========Cleaning all reports/logs/caches=========\n\n"
	@find . -type d -name logs -o -name reports -o -name .pytest_cache -o -name results | xargs rm -r

.PHONY: help
# got from :https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# but disallow underscore in command names as we want some private to have format "_command-name"
help: ## print command reference, same as just `make`
	@printf "  Welcome to \033[36mcontainer\033[0m command refference.\n"
	@printf "  If you wish to contribute, please follow guide at top section of \033[36mMakefile\033[0m.\n\n"
	@printf "  Usage:\n    \033[36mmake <target> [..arguments]\033[0m\n\n  Targets:\n"
	@grep -E '^[a-zA-Z-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "    \033[36m%-20s\033[0m %s\n", $$1, $$2}'




app/build-docker:
	@echo '+ Building docker image'
	@docker build . -t docker.pkg.github.com/huma-engineering/simpleapp:v0.0.1

app/run-docker: app/build-docker
	@echo '+ Building docker image'
	@docker run -it -p5001:5000 docker.pkg.github.com/huma-engineering/simpleapp:v0.0.1
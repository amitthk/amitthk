node_version:=$(shell node -v)
npm_version:=$(shell npm -v)
timeStamp:=$(shell date +%Y%m%d%H%M%S)
app_context:="./docker"
aws_s3_bucket_name:= "mys3bucket-repo"
project_name:= "myangular4project"

.PHONY: show install build archive test publish clean cleanprod deploy

show:
	@ echo Timestamp: $(timeStamp)
	@ echo Node Version: $(node_version)
	@ echo npm_version: $(npm_version)

clean:
	echo "cleaning the dist directory"
	@ rm -rf dist
	@ rm -rf dist.tar.gz
	@ rm -rf release/*.tar.gz

install:
	@ npm install --max-old-space-size=400

build:
	echo "building in production mode"
	@ npm run build --prod --max-old-space-size=400

archive:
	@ mkdir -p release
	@ cd dist && tar -czvf ../release/$(project_name)-$(timeStamp).tar.gz . && cd ..

test:
	echo "test the app"
	@ npm run test

publish:
	@ aws s3 cp ./release/$(project_name)*.tar.g s3://$(aws_s3_bucket_name)/$()/$(timeStamp)/

cleanprod:
	echo "cleaning the prod directory"
	@ rm -rf $(app_context)/app
	@ cd ./docker && docker-compose stop $project_name_ui

deploy:
	@ mkdir $(app_context)/app
	@ cp ./release/$(project_name)*.tar.gz $(app_context)/app/
	@ tar -xzvf $(app_context)/app/$(project_name)*.tar.gz -C $(app_context)/app
	@ echo running the container using docker-compose. Make sure docker, docker-compose are there and docker-compose.yaml exist in ./docker directory
	@ cd ./docker && docker-compose up -d --build $project_name_ui

INFO := @bash -c '\
  printf $(YELLOW); \
  echo "=> $$1"; \
  printf $(NC)' SOME_VALUE
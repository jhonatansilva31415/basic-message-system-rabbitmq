rabbit:
	docker-compose up --build
build:
	docker build -t rabbit_pc  .
consumer:
	docker run --net=basic-message-system-rabbitmq_default \
		   -e SEVERITY=$(severity)\
		   -e RUN_COMMAND=run-consumer\
		   -e RABBIT_HOST=rabbitdocker\
		   rabbit_pc
producer:
	docker run --net=basic-message-system-rabbitmq_default\
		   -e MESSAGE=$(message)\
		   -e SEVERITY=$(severity)\
		   -e RUN_COMMAND=run-producer\
		   -e RABBIT_HOST=rabbitdocker\
		   rabbit_pc

run-consumer:
	python consumer.py 
run-producer:
	python producer.py


test:
	echo $^(severity)

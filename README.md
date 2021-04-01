# A very simple RabbitMQ Docker Implementation

If you are curious to explore RabbitMQ with Docker, this repo might be for you 


The idea is simple, 



So first run the RabbitMQ instance with 

`make rabbit`

This will instantiate RabbitMQ for you, if can access it's dashboard if you into it.

After this you need to run a consumer, you can pop up how many consumers you want, just keep
oppening terminal screens and you're good to go, to instantiate one consumer, you need to 

`make consumer severity=error,warning,x,y,z`

Where error, warning, x, y, z and so on are the bindings you want to subscribe to.

After running as much consumers as you want, you can go and start sending messages like this 

`make producer severity=error message='"Run Forrest! Run!"'`

Like this 

![alt text](http://url/to/img.png)


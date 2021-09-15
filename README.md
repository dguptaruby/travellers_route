# Project Setup
* Take pull of this repository
* Run below comand at Docker file level
> **sudo docker build . -t <image_name>:latest**
* Then below command
> **sudo docker run -it -d --name <container_name> -p 8001:8000 <image_name>:latest**
* After running above command application will run 
* Go to the postman and run below url as **get** method
> http://127.0.0.1:8000/api/getroute/
* Pass list of locations as input in the body as shown below
> **{
    "list_cord":[
    [75.85962616866853,22.79614270933867],
    [75.84514379758467,22.797291799510006],
    [75.88513552642058,22.75784003109508],
    [ 75.89375487666832,22.744328470876017]
    ]
}**
* Respose of the above api will give us the sequence of coordinates 
* This sequence of coordinate will be route 
> **{
    "plan_output": 
"Route for vehicle:  
[75.85962616866853, 22.79614270933867] -> [75.89375487666832, 22.744328470876017] -> [75.88513552642058, 22.75784003109508] -> [75.84514379758467, 22.797291799510006] -> [75.85962616866853, 22.79614270933867]
"
}**
* Run below command to test it
> **./manage.py test**

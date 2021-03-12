# Ouranos

This repository contains all the code :computer: for automatic planting machine which our team Ouranos has created.
For more info about the machine please visit [Ouranos Robotics](http://ouranosrobotics.com/)

Our machine has three main freatures

* __Plantation__ :herb:
* __Irrigation__ :droplet:
* __Monitoring__ :eyes:

Till now our machine is capable of automatically planting a plant on the given location. 
[Agrobot](https://github.com/gaurav-patel-git/ouranos/blob/362362ad78ec3ff750cd854586311151705c3dd6/helper.py#L10) class is :heart: of our machine.
This class is responsible for obtaining magnetometer and gps data from sensors and then using that data it guides our robot :rocket:
It contains few methods for calculating real time distance :feet: and heading in order to aling bot to reach to destination. 
All the data from different sensors is collected in real time and processed at the same time with the help of multiprocessing concept so data can be processed simultaneously :relieved:

We began from testing each sensor whose code you can find out in the repository. Then we acheived our first milestone by implementing the __Plantation__ feature by doing everything manullay
by instructing the robot what to do and how to do. Once everything is working manually we started to automate stuff :octocat: 

To give instruction to robot we build a mobile app :iphone: and a server :satellite:. The mobile app will send instruction to server and then the server will give instruction to our Bot. We are using 
sockets to deliver and receive instructions. For testing purpose the server is hosted on the raspberry pi itself but it can be anywhere on the cloud. Due to this the raspberry pi and 
mobile aap has to be in same network. 

We are now working on the other features. Hope to complete them soon :sunglasses:

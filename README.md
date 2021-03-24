# Vehicle_counting_system


## Project Report 
### On 
# Vehicle Counting Mode
								
Swapnil Sunil Pandit.
Swapnilraj.pandit@gmail.com
24-03-2021




### Abstract:
Deep learning is a popular Machine Learning Algorithm that is used in many areas in current daily life. It’s strong and powerful performance and ready to use framework. In Deep learning people are developing various software and system to support human tasks. 
Traffic monitoring is one of the sectors that are used Deep leaning for several purposes. By using Cameras installed on some of the roads, many tasks such as vehicle identification, vehicle counting, vehicle speed monitoring, etc. In this report, we’ll discuss Video-Based Vehicle Counting. In this model Open CV2 library is used due to its good performance and compute time in object detection. 
The aim of this project to create a simple vehicle counting system. The counting is based on four types of vehicle car, motorcycle, bus, and truck. 


### Why OpenCV:
I would have use YOLO34py model because YOLO34py is extremely fast. But to run the YOLO34py model I need NVIDIA graphics card and I don’t have NVIDIA graphics,. And I suppose to complete this task on time and I know OpenCV very well so I decided to use CV2 
The OpenCV2 library is the logical tool to use. Open CV is an open-source library made up of a collection of modules for performing real time Computer Vision tasks. I quickly learned how to load images and videos as pre-processing steps or to produce visuals, perform background subtraction to detect objects. 
Detection is an aspect of CV and image processing with identifying the objects of a certain class like people and vehicles in the video. Object detection can be applied to solving hard problem. Vehicle detection which is most trick, but I have frame differentiation approach for it. A video is set of frames stacked together in the right sequence. When we see an object moving in a video, it means that the object is at different location.  So vehicles need to be counted at particular zone or when they cross line.

### Objectives of the proposed system :
I have built this video based Vehicle Counting Model using Python programming language and hence it is very easy to understand and reusable. The accuracy of the model is very good. It comprised of three processes:
###        1. Detection 
###        2. Tracking 
###        3. Counting 
1. Detection- In this process the program detects the vehicle using Frame Differentiation algorithm of Deep learning. Wherein the videos frames are stacked up with Framed Vehicle. After stacking the moving part of the detected object is highlighted. It is then converted to grayscale and then contoured. Lastly after background subtraction the contoured part will be dilated. 
2. Tracking - In this process the orientation of the object is checked and then the dilated frame is appended on original frame. 
3. Counting - The most easy part of program wherein the number vehicles are counted based on crossing of particular line of video frame.


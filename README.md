# Yolov3_Tiny_VisDrone
Training yolov3_tiny on VisDrone 2019 detection dataset

![darknet](https://user-images.githubusercontent.com/13064391/225038398-377a31a8-5cb1-4cf0-8379-64ce17016774.png)

# Platform
GPU : NVIDIA Quadro RTX 6000/8000<br>
CUDA toolkit version : 11.4<br>
Driver version : 470.57.02<br>
cuDNN version : 8.8.1.3<br>
OpenCV version : 4.2.0 <br>
Ubuntu : 20.04 <br>

# Resources 
Dataset : https://github.com/VisDrone/VisDrone-Dataset <br>
Darknet installation guide : https://github.com/ERYAGNIK003/darknet <br>
Download convolution layers(darknet53) weights : https://pjreddie.com/media/files/darknet53.conv.74 <br>
Transform VisDrone data format to Darknet : https://github.com/zhaobaiyu/visdrone <br>
Training instruction : https://github.com/AlexeyAB/darknet/issues/504 <br>
visualizing network : https://github.com/hahnyuan/darknet-visualizer <br>

# Directory structure
|<br>
|___darknet<br>
|<br>
|___VisDrone<br>
&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    |__VisDrone2019-DET-train<br>
&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    |__VisDrone2019-DET-val<br>
&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    |__VisDrone2019-DET-test-dev<br>
&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    |__dataTransform.py<br>
    
# Steps
- Setup CUDA driver, cuDNN library, OpenCV and Darknet on your system as per given in  https://github.com/ERYAGNIK003/darknet <br>
- Download darknet53 weights into darknet directory
  - cd darknet
  - wget https://pjreddie.com/media/files/darknet53.conv.74
- Download VisDrone 2019 DET dataset and organise darknet and visdrone as per given directory structure
- Download dataTransform.py from repository and store into VisDrone directory, this will helps to convert data format
- Execute it by "python dataTransform.py" , this will create images.txt file in all three dataset directory
- Add configuration files into darknet directory
  - Download visdrone.data into darknet/cfg/
    - Modify "path-to-dataset/images.txt" according to your dataset path
  - Download visdrone.names into darknet/data/
  - Download yolov3_visdrone.cfg into darknet/cfg/
- To visualize your netowrk use graph visualizer
  - pip install graphviz
  - sudo apt-get install graphviz
  - git clone https://github.com/hahnyuan/darknet-visualizer
  - cd darknet-visualizer
  - python3 darknet_visualize.py example/yolov3.cfg (replace path to .cfg file as per yours)
- Start training yolov3_tiny on visdrone dataset using below command,
  - cd darknet
  - ./darknet detector train cfg/visdrone.data cfg/yolov3_tiny.cfg darknet53.conv.74 -dont_show -map

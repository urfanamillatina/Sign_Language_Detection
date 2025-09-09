# Sign Language Detection Model - Indonesian Language (SIBI - Sistem Isyarat Bahasa Indonesia)

## A Computer Vision project to Detect Hand Sign for Sign Language - Still on progress.


<p align="center">
  <img src="./assets/hand_sign_med.gif" alt="Watch the demo" width="500"/><br/>
  <em>Signing My Name</em>
</p>

### Key Takeaways:

- Learning a new language!
- Contributing to the accessibility of communication between 


### Objectives:
This computer vision project is to detect sign language from hand gestures. Utilizing AI/ML to contribute to more accessible ways of communication between deaf and non-deaf people in Indonesia.

### Prelimenary
This is a preliminary to first test out workflows, integration, dataset, dependencies and model. 

As the preliminary model, it's trained on yolov5n which has small capacity, with fewer epochs (10) for faster training, and smaller image size (320 x 320 pixels) for faster inference which can result in lower accuracy. As of now, the training is for only alphabetic SIBI signs which is 26 class. 

Continuously, the classes will be added, like numericals, common expressions, etc. 


The performance metrics are good, but during the live testing using Webcam (MacOS) the accuracy and the confidence become worse. The more distance the hands from the camera, the less accurate the detections are, especially in signing similar gestures like the letter A, M, N.


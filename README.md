<p align="center">
<h1 align="center">Sign Language Detection Model

Indonesian Language (SIBI - Sistem Isyarat Bahasa Indonesia)
</h1>
</p>

<p align= "center">
<img src="https://img.shields.io/badge/Status-On%20Progress-yellow" />
<img src="https://img.shields.io/badge/YOLOv5n-blue?logo=yolo&logoColor=white"/>
<img src= "https://img.shields.io/badge/Ultralytics-007ACC?logo=python&logoColor=white">
<img src= "https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white"/>
</p>


<p align="center">
<h3 align="center">A Computer Vision project to Detect Hand Sign for Sign Language, specifically for Indonesian Sign Language (SIBI -Sistem Isyarat Bahasa Indonesia)</h3>
</p>


<p align="center">
  <img src="./assets/hand_sign_med.gif" alt="Watch the demo" width="500"/><br/>
  <em>Signing My Name: Millatina </em>
</p>

## Key Takeaways:

- Personally, this is an opportunity to learn a new language for me! And contributing to the accessibility of communication between deaf & non-deaf people through Computer Vision.
- As a preliminary model, the training performance is excellent,  but the live test using webcam shows poor accuracy and confidence level, especially the farther away the hands are from the camera.
- Next actions: to train with bigger models; improve accuracy and confidence level on live tests; and  add more classes like numericals (1-10) and common expressions.


## Objectives:
This computer vision project aims to detect sign language from hand gestures. Utilizing AI/ML to contribute to more accessible ways of communication between deaf and non-deaf people in Indonesia.


### Prelimnary
This is a preliminary to test out workflows, integrations, dataset, dependencies and model.

This preliminary model is trained on YOLOv5n, which has a smaller capacity, with fewer epochs (10) for faster training, and a smaller image size (320 x 320 pixels) for faster inference, which can result in lower accuracy. Currently, the training is limited to only alphabetic SIBI signs, which comprise 26 classes.

Continuously, more classes will be added, like numericals and common expressions, etc.


## Tech Stack

### Core Libraries


![YOLOv5n](https://img.shields.io/badge/YOLOv5n-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)
![Ultralytics](https://img.shields.io/badge/Ultralytics-0083CA?style=for-the-badge&logo=yolo&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-003366?style=for-the-badge&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Other Tools


![Roboflow](https://img.shields.io/badge/Roboflow-3A10E5?style=for-the-badge&logo=roboflow&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FFCC00?style=for-the-badge&logo=google&logoColor=black)
![tqdm](https://img.shields.io/badge/tqdm-4A90E2?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-2E4C6D?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-3670A0?style=for-the-badge&logo=python&logoColor=white)

### IDE



![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-0078d7?style=for-the-badge&logo=visual-studio-code&logoColor=white)


## The Dataset:
The dataset is retrieved from Roboflow universe [here](https://universe.roboflow.com/my-projects-7vrlf/sign-language-sibi-katux)

## The Model: 

This model is utilizing YOLO v5 Nano through ultralytics.

## Preliminary Results:

The performance metrics for training are excellent like shown in the plot below:
<p align="center">
  <img src="./assets/performance.png" alt="performance metrics" width="500"/><br/>
  <em>YOLOv5n Training Metrics</em>
</p>

It shows that overtime, the precision, recall, Mean Average Precision and the Average of Mean Average Precision are increasing during the training. The metrics are improving the more training cycles have been completed. 


## Live Test on Webcam

Testing the model live using webcam on MacOS (localhost). Even though the training's performance is excellent, during the live testing, the accuracy and the confidence in detecting hands and signs become worse. The more distance the hands from the camera, the less accurate the detections are, especially in signing similar gestures like the letter A, M, N. The gif file above has better accuracy and confidence level since the hand is closer to the camera.

## Next Actions
- To train with bigger model and more epochs.
- To improve accuracy and confidence level on live test.
- Try other algorithms
- To train more classes: like numericals (1-10) and common expressions.

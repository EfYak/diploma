# info_fusion
This project is devoted to multimodality and its application in Intelligent Transport Systems.<br>
Vibro, video and audio signals have been collected across roads of Brisbane, QLD, Australia.<br>
The main idea of the research is to prove the statement that several "inexpensive" and flexible systems can perform at the same level or outperform an "expensive" and train-dependent system.<br>
<br>
## Vibro
  ![signal4-105269-106950](https://user-images.githubusercontent.com/19166880/146504581-8da4b62e-6b6c-41af-89cd-f34f6e44eec9.png)
  ![signal3-87860-89480](https://user-images.githubusercontent.com/19166880/146504596-646732d0-a3f4-40ee-8069-59da4cd6f3a9.png)
  <br>
  As it could be seen on the images above, there are some well-distinguished spikes when a vehicle passes the sensor close enough.<br>
  However, because of an unstable connection device-server and due to technical flaws, all collected data has a considerable short duration and cannot be used for a thorough         analysis and further model training.<br> 
  Such an example is provided below. <br>
  ![signal](https://user-images.githubusercontent.com/19166880/146507848-b23af77b-20aa-4463-a3ad-0695c4d7c7b4.png)
  Here flat straight lines are those where the connection had been lost.<br>
## Video
  Different areas of the city had been explored until the best-fitted was found.<br>
  ![image](https://user-images.githubusercontent.com/19166880/146508968-4735e7b4-a308-4c14-a68b-c6b4b1dcc4b3.png)
  ![image](https://user-images.githubusercontent.com/19166880/146509028-86d09b80-e00b-4286-be87-954729e315e8.png)
  The chosen spot had a good observation angle and a complicated traffic scheme with turn lines, traffic lights and a crossroad.<br>
  These aspects made the chosen spot the most attractive to the aim of this project.<br>
  ![image](https://user-images.githubusercontent.com/19166880/146511547-91908eef-e1a3-40be-b496-8e48ecde56bd.png)
  <br>
  <br>
  At first Faster-RCNN-Inception-V2 model was pretrained.<br>
  The model showed substantial-quality and successfully recognized all labels.<br>
  ![image](https://user-images.githubusercontent.com/19166880/146528469-845b2043-6b4e-45bf-9be9-3d8fbb1bc563.png)
  Then the pre-trained model was applied to the chosen spot.<br>
  The quality of the model significantly dropped as was expected.<br>
  This step was meant to prove the hypothesis that such an approach, once trained, could not be reapplied on various roads.<br>
  ![image](https://user-images.githubusercontent.com/19166880/146529614-6aa2edb0-5703-4295-90bb-81536bbc6b6a.png)
  Than a simple CNN was trained on the spot to the futher usage in conjuction with an audio model.<br>
  This model had a simplified task only to detect a vehicle in a small region of interest.<br>
  ![image](https://user-images.githubusercontent.com/19166880/146530988-29acc830-a756-4dbc-920c-47a94583b3e6.jpg)

## Audio
  An audio dataset had been collected using a simple audio recorder on a cell phone and then synchronized with the video dataset.<br>
  A raw signal was converted to a mel-spectrogram and labelled "car"/"no car".<br>
  ![image](https://user-images.githubusercontent.com/19166880/146531644-2b6e4350-b3c3-4ef5-a8cd-4e943b8faabf.png)
  Due to a huge class imbalance an augmentation to the "car" class had been applied.<br>
  ![image](https://user-images.githubusercontent.com/19166880/146532538-a133f673-4d12-4f55-af67-7164169450dd.png)
  After that a pretrained ResNet34 had been fine-tuned to recognize aforementioned classes.<br>
  
## Information Fusion
  At this stage of the research, the fusion of audio and video data had been analysed visually. <br> 
  ![ezgif com-gif-maker](https://user-images.githubusercontent.com/19166880/146758305-d6a2467e-c701-4ea0-8317-2068976489e3.gif)
  Overall systems performed satisfactory in conjuction.<br>
## Further Work
  Audio signals can be very noisy and in some cases, it is a complicated task to detect a vehicle in a current ROI.<br>
  Thus, there are some possible ways of improvement.<br>
  Either use vibrations or improve the audio classifier or both.<br>
  <br>
  A simple CNN classifier showed that it can perform at the same level as the "heavy" Faster-RCNN-Inception-V2 model.<br>
  It was able to solve approximately the same task as the model with sophisticated architecture.<br> 

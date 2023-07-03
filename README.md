# Neural-Style-Transfer
#### Image Style transfer done using VGG-19

A content image and a style image is merged together to get a result which looks like the style image<br>
VGG19 pretrained model is used (with freezed weights) and the whole training process operates around the loss function<br>
<br>


## CONTENT IMAGE + STYLE IMAGE = OUTPUT IMAGE

<br>

 <div class="row">
      <div class="column">             
        <img src="https://raw.githubusercontent.com/sanjay-906/Neural-Style-Transfer/main/pictures/input.jpg"   style="width:30%"  align="left">  
      </div>
      <div class="column">
       <img src="https://raw.githubusercontent.com/sanjay-906/Neural-Style-Transfer/main/pictures/paintstyle.jpg"   style="width:20%"  align="left">
      </div>

   <div class="column">
       <img src="https://raw.githubusercontent.com/sanjay-906/Neural-Style-Transfer/main/pictures/result.png"   style="width:30%"  align="left">
      </div>
    </div>
    </div>

&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>
&nbsp;
<br>


### LOSS FUNCTION:<br>


![loss](https://raw.githubusercontent.com/sanjay-906/Neural-Style-Transfer/main/pictures/Loss%20function.jpg)



### CONTENT LOSS:<br>
content loss is captured by the mean squared error of the generated image and content image(they are the outputs from the 5 convolution layers)
<br>

### STYLE LOSS:<br>
style of an image is captured using gram matrix.. it is the dot product of the features of convolution layers.. which is done to calculate the correlation between the features, which turns out to be the style blobs in the style image

<br>

### RESULTS:<br>

224x224 image size; After training for 10,000 epochs

![results](https://raw.githubusercontent.com/sanjay-906/Neural-Style-Transfer/main/pictures/results.jpg)

<br>

### RESULT AT VARIOUS STAGES:<br>

![resultsatvariousstages](https://raw.githubusercontent.com/sanjay-906/Neural-Style-Transfer/main/pictures/op.gif)

<br>

### RESULT COMPARISION<br>

With Style Image:<br>
![starrynight](https://raw.githubusercontent.com/sanjay-906/Neural-Style-Transfer/main/pictures/1paintstyle.jpg)
<br>

https://github.com/sanjay-906/Neural-Style-Transfer/assets/99668976/23fc69db-aab4-42da-a112-b980d6735ba6

<br>


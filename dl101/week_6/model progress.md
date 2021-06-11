# Summary of my progress with my own model   
## What was your model’s prediction accuracy last time you presented?
- 0.85  

## What’s it now?  
- 0.95

## What optimization, additional data, data wrangling, augmentation, learning approach, ...did you use to improve the accuracy of your classification model?
1. changed pretrained model (`Resnet50`)
2. changed image size
3. data augmentation
4. normalization input data
5. deleting bad images

## Be ready to tell why you think you cannot improve the accuracy of your model further. 
- I think would be able to improve the accuracy at least a litt bit more. But I was running out of GPU resources im `Google Colab` (and also in personal time).

## What other optimization techniques or ways you could possibly take that you couldn’t try/use yet.
- With an accuracy rate of 95% only a few wrong classified images are left. A more detail investigation shows that some of these images are very focused/zoomed - showing only parts of the flower. Further data augmentation with zooming technique might increase the accuracy rate by a few 0.1%   
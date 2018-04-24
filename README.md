# Unet_dsb2018
Unet Keras implementation for Kaggle Data Science Bowl 2018

# Features
* imgaug library for images augmentation with custom data generator
* random crops for training
* test time augmentation
* evaluation of arbitrary sized images
* padding if shape of image is not multiple of 16 = 2**(# of convolution blocks in unet)

It's not possible to have both *arbitrary sized images evaluation* and *valid padding* in the network because you cannot access the shapes (shape=(None,None,:) for arbitrary sized images) to crop the features before the concatenate layer. For now I'm sticking with the evaluation of arbitrary sized images.
  
Alternative: valid & reflection padding + sliding window evaluation

# TODO
* weighted cross entropy

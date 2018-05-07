# Unet_dsb2018
Unet Keras implementation for Kaggle Data Science Bowl 2018

# Features
* weighted cross entropy
* imgaug library for images augmentation with custom data generator
* random crops for training
* test time augmentation
* evaluation of arbitrary sized images
* OR valid & reflection padding + sliding window evaluation (input size 412x412, output 228x228)
* padding if shape of image is not multiple of 16 = 2**(# of convolution blocks in unet)

It's not possible to have both *arbitrary sized images evaluation* and *valid padding* in the network because you cannot access the shapes (shape=(None,None,:) for arbitrary sized images) to crop the features before the concatenate layer. They are implemented in different notebooks.

# List of augmentations: 
* scale +/-15%
* rotations 90/180/270
* flip up/lr

# Top Scores:
* Unet: LB 0.350
* Unet+weighted cross entropy: LB 0.432
* Unet+weighted cross entropy+valid padding: 0.330 (needs fixing)

# TODO:
* fix validation score/validation generator in weighted_valid notebook
* fix weighted_valid notebook meanIOU output 

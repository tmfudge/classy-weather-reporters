# Classy Weather Reporters

## Project Summary
We have chosen a multi-class weather dataset (MWD) for image classification, as it is a valuable dataset used in the research paper entitled “Multi-class weather recognition from still images using heterogeneous ensemble method”. The dataset provides a platform for outdoor weather analysis by extracting various features for recognizing different weather conditions.

## TensorFlow 
TensorFlow is an open-source library developed by Google primarily for deep learning applications.
with this project we used Tensorflow: for image classification, tf.keras.Sequential model and for loading data we used tf.keras.utils.image_dataset_from_directory.

## Weather Classification
We used three different classification of weather that this dataset will provide training for:

* Clouds
* Rain
* Sunshine

![Data_Visualization](https://user-images.githubusercontent.com/85952426/171284407-cf3f2808-191a-4ae1-98c1-dcbda97e25bb.png)


## Training Data
We used a validation split of 80% of images for training, and 20% of images for validation. Out of 921 data sets.

Our initial values gave us Accuracy 87.5% and Loss 0.93


![Training_Validation](https://user-images.githubusercontent.com/85952426/171284754-43ebde2c-bc8e-49ff-bc0a-746442e6c309.png)

In the plots above, Our initial values gave us Accuracy 87.5% and Loss 0.93  in the training process. Also, the difference in accuracy between training and validation accuracy is noticeable—a sign of overfitting.
Improving the variety of training data would be next step

## DATA AUGMENTATION
In order to reduce Overfitting, we apply data augmentation. We implemented data augmentation using the following three Keras preprocessing layers: 

* tf.keras.layers.RandomFlip
* tf.keras.layers.RandomRotation
*  and tf.keras.layers.RandomZoom.

![Data_Augmentation](https://user-images.githubusercontent.com/85952426/171285484-45561098-5c10-44ef-a107-e1f8d1079e77.png)

## DROPOUT
Another technique we used to reduce overfitting is “dropout”. After applying data augmentation and tf.keras.layers.Dropout, there is less overfitting than before, and training and validation accuracy are closer aligned.

![Training_after_Data_Augmentation](https://user-images.githubusercontent.com/85952426/171285843-5e45e0d3-8e38-4f19-b6dc-7e1b50c936de.png)

## PREDICT ON NEW DATA

(https://images.unsplash.com/photo-1633467189683-9c84b2eed802?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2067)




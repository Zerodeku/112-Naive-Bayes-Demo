# Naive Bayes Demo (Spam Filter)

## Run Code

To train the model, use the command:

    python NBtrain.py -f training_folder

The "training_folder" should contain a folder named "spam" and a folder named "ham".  See folder "data1" for an example.

To test the model with testing folder, use the command:

    python NBtest.py -f testing_folder [-p spam_prior]
    
The "testing_folder" should be of the same structure as the "training_folder".

## Dataset

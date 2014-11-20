# Naive Bayes Demo (Spam Filter)

## Run Code

To train the model, use the command:

    python NBtrain.py -f training_folder

The "training_folder" should contain a folder named "spam" and a folder named "ham".  See folder "data1" for an example.

To test the model with a testing folder, use the command:

    python NBtest.py -f testing_folder [-p spam_prior]
    
The "testing_folder" should be of the same structure as the "training_folder".

To test in an interactive mode:

    python NBtest.py -i [-p spam_prior]
    
## Dataset



## Disclaimer

This code is written for demo purpose only.  It hasn't been thoroughly tested.

# YeNet
Deep learning generated rap lyrics trained on a dataset of Kanye West's discography. I used [PyTorch](pytorch.org) to create a word-level recurrent neural network utilizing Long Short-Term Memory [(LSTM)](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21) cells
that can generate lyrics upon provided a "primer" word as indicated by the user.

## Generated Samples:
Here are some of my favourite bars out of the many I generated. If you don't think too hard, I guess they might almost make sense?
```
 you know the heart is the whole thing 
 you know i love that shit 
 i need the new girl ? 
 don't be like you 
 they say , " i know what , but she can't have to do 
 you don't really wanna be in a few girl 
 i can't let me go and the game 
 
 i know it's corny , we gon' make it 
 i don't know what i was to the world 
 
  you know how it feel like ? " 
 now i'm in my club , i don't want to do it 
 but i don't need my new slaves 
```
More lyrics, including the ones above, can be found in generated_samples > generated_lyrics.txt

## Try the Program!
Ensure the following libraries are installed along with a distribution of Python3:
* NumPy
* PyTorch

I recommend using [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) to install these packages, as well as running the project in a virtual environment.

Run train.py to instantiate and train a custom model, or simply run generate.py to try out the pretrained model in this repo.

In terms of training a custom model, having an available GPU will speed up the training process substantially, otherwise a decent-performing model will take over an hour to train.

## Next Steps:
* Implement a web scraper for data collection
* Train the network on a few other artists' discographies (curious to see what DrakeBot or DoomNet might produce)



Shoutout to [Robbie Barrat](https://github.com/robbiebarrat) for the dataset and a similar project built with Keras a couple years ago.


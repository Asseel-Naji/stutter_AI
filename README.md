# stutter_AI
This solution aims to help stutterers get a cleaned version of their speech, the aim of this project is to advance voice assitance to cover the %1 of the population who find difficulty using any voice assitance solution (ex. Alexa, Google, Siri..etc) and they have a very hard time using STT in general.

This proof of concept works by taking a stuttered speech sample, and processing it to remove stuttering, and then transcribing the resulting text using Amazon's transcribe. It is so far trained on a very limited dataset (50) and can only be used to some extent by its author (me), in order to adapt it for wider it needs over 300 hours of training data. This model deals with audio purely, so it can be adapted to any language (although you will need to change the transcribtion language for the transcribe API)

Below are the steps taken while developing the project (meant for Teckathon judging panel, jump to "Getting started" for more relevant information)

## Steps that got me here
### The idea
Stutters make up %1 of the population, and they were left behind in the last few years. As while many of the services nowadays are becoming more and more reliant on voice, they still can't use this technology, a stutterer can't transcribe his voice even using a sophisticated solution such as amazon's transcribe or Google's API, and they can't interact with voice assitance which is especially dangerous while driving.
Fortunately, the same technology that left them behind can solve this problem. Here is where deep learning comes into play.

### Research and steps
This task seemed daunting, especially given that I didn't expect the total lack of solutions online, it seems as if no-one bothered to solve this very real problem. But while this was a problem for me, it made me more determined as I felt I was actually solving a real problem that wasn't tackled much outside of research papers.

I was almost giving up on the teckathon itself as writing my own solution in 3 days is an impossible task, that's when I encountered this paper :
https://arxiv.org/pdf/1804.09202.pdf

While not many have tackled stuttering itself, a few have tried extracting vocals from music, and since some solutions for that exist online, I decided to try my hand with that approach.
The neural network is training as I write this, so I'm not sure of the effectivity yet. However even if this one doesn't work an amplitude based approach is still possible if the time allows it (training takes a lot of time, even of a fancy xxlarge EC2, thanks for the credit btw.)

After spending literally half the competition time researching and tinckering, I finally decided on this project : https://github.com/tsurumeso/vocal-remover

It is still in active development and I'm gonna pay back to the developer by putting in some pull requests by the end of today as I encountered a lot of bugs and grey areas I had to work out, which took the second half of the second day.

I had to record 50 samples of stuttering speech, as there are no data samples online anywhere, I think had to manually remove the stuttering from them one by one.
And afterward I found out that the samples should be two tracks stero and not one mono like I recorded. Debugging that took me way longer than I'd like to admit (here comes my first pull request).

As the moment of writing this I'm training it on 10 samples and it's taking a long time. once that finishes and I test it I'll train the rest and finalize.

TO DO:
Hopefully by the time the teckathon ends this will be empty :
1- Write an API end point that takes an audio and return a cleaned version of the audio and a transcribe..
2- Write a web portal for said API.

## Getting started

## Deploying on AWS

### Create an EC2 GPU instance.
The bigger, the better.
### Start a pytorch environment 
```
source activate pytorch_latest_p36
```
### Clone the respatory
```
git clone https://github.com/Asseel-Naji/stutter_AI.git 
```
### install the required packages
```
pip install -r requirements.txt
```
## CLI usage
The following command extracts the vocal and discards the stutter
### run on CPU
```
python inference.py --input path/to/an/audio/file
```
### run on GPU
```
python inference.py --input path/to/an/audio/file --gpu 0
```

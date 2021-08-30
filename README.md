# Audio's Text Summarization

A summarization application created using Python that takes the audio file from the user, convert the audio file into the text and then give summary.

# Table of Contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Launch](#launch)
* [Usage](#usage)
* [Future updates](#future-updates)
* [Call for Contributions](#call-for-contributions)

## Introduction

Audio's text summarization app is a simple application that is developed to give the summary of your audio file. The user is suppose to upload the audio file to the application then the application will convert the audio file into the text and then to its summary.

## Technologies

The project was developed using python 3.8. Also, other python libraries were used to complete the project. The other required libraries are as follows.
* nltk 3.6.2
* pytest 6.2.4
* pydub 0.25.1
* streamlit 0.87.0
* speechrecognition 3.8.1

## Launch 

The running of the application can be viewed by the help streamlit library. There is view.py file in the project. The developer can just run file under the streamlit. 

```bash
streamlit run view.py
```
## Usage 

After launching the application, it is simple to use it as well. The application will ask the user to upload the file, providing a form as shown below to browse the file from the device. 

![alt text](https://github.com/NikhilDwa/Audio-to-Text-Summarization/blob/speechtotext/nikhil/converting_speech_to_text/images/upload_file.JPG)

When the file is uploaded, the audio bar will appear. With the help of audio bar user can also listen the audio.

![alt text](https://github.com/NikhilDwa/Audio-to-Text-Summarization/blob/speechtotext/nikhil/converting_speech_to_text/images/uploaded_file.JPG)

Then the application will carry out the audio to text conversion. The text is converted and displayed to the user. Then the summarization is carried out and finally the summary is of the audio is displayed to the user.   

![alt text](https://github.com/NikhilDwa/Audio-to-Text-Summarization/blob/speechtotext/nikhil/converting_speech_to_text/images/text_summary.JPG)


## Future updates

Most of the tasks in the project are done however, some fo them are pending. The task list with completed and pending task are listed below.
- [x] Converting audio file to text
- [x] Preprocessing of the text
- [x] TF and IDF evaluations
- [x] Text summary
- [x] Unit testing 
- [ ] Converting large audio file to text
- [ ] Upload any kind of audio file
- [ ] Convert audio to video to summarize


## Call for Contributions

We welcome the enthusiastic developers. Pull requests are welcome. You can also contibute by helping to outreach new contibutors.
Please make sure to update tests as appropriate.

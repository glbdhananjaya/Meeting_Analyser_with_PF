# Project Team Information

## Team Members - Team H
- Bhashitha Dhananjaya
- Yasas Weerasinghe
- Gishan Nirmasanka
- Maneesha Wickramasingha

# Project Overview

## Description
This project is a OpenAI based automated transcription and summarization system utilizing Python to extract critical information from Microsoft Teams meetings. The system aims to generate concise summaries encompassing key takeaways, significant insights, actionable steps, and suggestions discussed during the meeting using a chat bot. This solution is intended to assist individuals who were unable to attend the meeting or have limited time to review lengthy recordings, providing them with a comprehensive yet efficient overview of the discussed topics.

## Installed Packages
- moviepy
- SpeechRecognition
- pocketsphinx
- openai

## Used Technologies
- OpenAI
- Python
- PromptFlow

## Referenced Links
- Prompflow Documentation: [https://microsoft.github.io/promptflow/how-to-guides/quick-start.html](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)
- Miniconda: [https://docs.conda.io/projects/miniconda/en/latest/](https://docs.conda.io/projects/miniconda/en/latest/)
- GitHub Repo: [https://github.com/microsoft/promptflow](https://github.com/microsoft/promptflow)

## Screenshots
![Screenshot 1](./screenshots/Screenshot_1.png)
![Screenshot 1](./screenshots/Screenshot_2.png)
![Screenshot 1](./screenshots/Screenshot_3.png)
![Screenshot 1](./screenshots/Screenshot_4.png)

# Project Evaluation

## Drawbacks 
- Transcriptions takes time since an audio file is generated first from the video.

## Suggestions
- A faster, more advanced speech recognition engine can be used. (e.g: Google Speech Recognotion API or any other cloud based API)
- More efficient transcription library can be used. (Advanced Models, e.g: Vosx)
- In pocketsphinx, real time transcription library can be used. 

## Assumptions
- We already have the team meeting recording locally

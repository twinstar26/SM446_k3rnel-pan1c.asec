# JARVIS for Corporate
- Problem Statement Number : **SM446**
- Organization : **FIS Global**

## K3RNEL-PAN1C.ASEC (Team Members)
- Atharva Veer (Team Leader)
- Yash Jain
- Harsh Chheda
- Kritika Ravishankar
- Dhwani Agarwal
- Divy Patel

## Technology Stack
- SNIPS NLU for intent parsing in chatbot
- Flask for server-side development
- HTML-CSS-JS / Bootstrap Web technologies for building user interface
- Py Audio for chunking required for Minutes of the Meetings
- SMTP@gmail.com for sending E-Mails

## Application Architecture
![Application Architecture](./Model/architecture.jpg)


## Features implemented
- User-interface for chat interaction and query output
- User-interface can take query in form of speech or text
- User-interface can return respone of the query on the chatbot screen or via email
- Supportes recording the meeting, summarizing and getting the apt. meeting from database depending on the keyword
- Supporting Stack-Overflow queries
- Supporting queries for Jira, Confluence and Bitbucket
- Supports taking feedback from the user on the response of the query and tweak the model depending on the feedback and continuously improving the model performance


## Working of Chatbot
![Chatbot-Internals](./Model/chatbot-internals.png)

## Comparison between various Chatbots
![Comparisons](./Model/comparison.jpg)

## Setup
```
Prerequisite:
    Python 3.7
    Local Instance of Jira, Bitbucket, Confluence running
```
```
Commands to install the dependencies
$ cd NLU
$ pip install -r requirements.txt
```

```
Starting the server
$ python app.py
```
```
Running the chatbot
http://localhost:5000/
```

<!-- # PPT Preparation
- [ ] Scalability
- [ ] Complexity
- [ ] Clarity
- [ ] Feasibility in the market
- [ ] Practicability
- [ ] UX
- [ ] Overall application performance benchmarking
- [ ] Prepare video of navigation

# Todo
- [ ] EMail HTML embedded (11 - 20) Y H
- [ ] Cross platform support (11 - 20) D Dh K
- [ ] Increase API features(include Write, Modify, Delete queries.) (11 - 20) D Dh K
- [ ] Speech to Text (11 - 20) D Dh K
- [ ] Text to Speech (11 - 20) D Dh K
- [ ] Refactor UI (11 - 20) Y H
- [ ] Inflate intents (11 - 20) A
- [ ] Optimize HTML templates for display (11 - 20) Y H
- [ ] Integrate Meeting feature (21 - 25) All In
- [ ] PPT Preparation (25 - 30) All In

# k3rnel-pan1c.asec
Smart India Hackathon 2020

## Setup for Frontend
```
cd frontend
```
```
npm install
```
```
node app.js
```
## Setup for NLU
```
cd NLU
pip install -r requirements.txt
```
```
python -m snips_nlu download en
``` -->
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
![Application Architecture](./Model/Arch.png)


## Features implemented
- User-interface for chat interaction and query output
- User-interface can take query in form of speech or text
- User-interface can return respone of the query on the chatbot screen or via email
- Supportes recording the meeting, summarizing and getting the apt. meeting from database depending on the keyword
- Supporting Stack-Overflow queries
- Supporting queries for Jira, Confluence and Bitbucket


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
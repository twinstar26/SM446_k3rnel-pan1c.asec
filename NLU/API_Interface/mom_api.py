import os

def momDetails(keyword):
    matches = set()
    d = os.getcwd()
    ls = os.listdir(d + "\minutes_of_meeting")
    for meeting in ls:
        if meeting != ".cph":
            with open(d + "\minutes_of_meeting\{}".format(meeting)) as current:
                lines = current.readlines()
                count = 0
                for line in lines:
                    if line == "===\n":
                        count += 1
                    if (count == 2):
                        if not (line == "===\n" or line == "==="):
                            key = line.split(" -> ")
                            if (key[1][:-1] == keyword):
                                matches.add(meeting)
    
    html = '''
        <div class='container p-4'><h2>Meetings</h2>
    '''

    for meeting in matches:
        with open(d + "\minutes_of_meeting\{}".format(meeting)) as current:
            html += "<div>"
            html += "<hr><h4>Summary</h4>"
            lines = current.readlines()
            html += "<p>" + lines[0][:-1] + "</p>"
            count = 0
            for line in lines:
                if (line == "===\n" or line == "==="):
                    count += 1
                    if count == 1:
                        html += "<hr><h4>Attendees</h4>"
                    if count == 2:
                        html += "<hr><h4>Keywords</h4>"
                    continue
                
                if (count == 1):
                    html += "<p>"+ line[:-1] +"</p>"
                if (count == 2):
                    html += "<p>"+ line[:-1] +"</p>"
            html += "</div>"
        html += "</div><hr>"
    return html


def summarizeMeeting():
    d = os.getcwd()
    matches = os.listdir(d + "\minutes_of_meeting")
    matches.reverse()
    print(matches)
    matches = [matches[-2]]
    
    html = '''
        <div class='container p-4'><h2>Previous Meeting</h2>
    '''

    for meeting in matches:
        with open(d + "\minutes_of_meeting\{}".format(meeting)) as current:
            html += "<div>"
            html += "<hr><h4>Summary</h4>"
            lines = current.readlines()
            html += "<p>" + lines[0][:-1] + "</p>"
            count = 0
            for line in lines:
                if (line == "===\n" or line == "==="):
                    count += 1
                    if count == 1:
                        html += "<hr><h4>Attendees</h4>"
                    if count == 2:
                        html += "<hr><h4>Keywords</h4>"
                    continue
                
                if (count == 1):
                    html += "<p>"+ line[:-1] +"</p>"
                if (count == 2):
                    html += "<p>"+ line[:-1] +"</p>"
            html += "</div>"
        html += "</div><hr>"
    return html

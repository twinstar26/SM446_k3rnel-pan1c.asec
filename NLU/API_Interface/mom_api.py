import os

def momDetails(keyword):
    matches = set()
    ls = os.listdir("../minutes_of_meeting")
    for meeting in ls:
        if meeting != ".cph":
            with open("../minutes_of_meeting/{}".format(meeting)) as current:
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
    
    html += '''
        <div class='container p-4'><h2>Meetings</h2>
    '''

    for meeting in matches:
        with open("../minutes_of_meetings/{}".format(meeting)) as current:
            html += "<div>"
            html += "<hr><h3>Summary</h3>"
            lines = current.readlines()
            html += "<p>" + lines[0][:-1] + "</p>"
            for line in lines:
                if (line == "===\n" or line == "==="):
                    count += 1
                    if count == 1:
                        html += "<hr><h3>Attendees</h3>"
                    if count == 2:
                        html += "<hr><h3>Keywords</h3>"
                    continue
                
                if (count == 1):
                    html += "<p>"+ line[:-1] +"</p>"
                if (count == 2):
                    html += "<p>"+ line[:-1] +"</p>"
            html += "</div>"
        html += "</div>"
    return html
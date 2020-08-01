import re
import requests

def topPostAnswer(error):

    r = requests.get("https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&site=stackoverflow&q={}".format(error.replace(" ", "+")))
    links = []
    count = 0
    for item in r.json()["items"]:
        if item["is_answered"] == True:
            count += 1
            links.append(item["link"])
            if (count == 5):
                break


    # print(links[0])
    r = requests.get(links[0])
    x = str(r._content)

    indices = [m.start() for m in re.finditer('<div class="post-text" itemprop="text">', x)]
    answers = []
    for i in indices:
        curr = ""
        for j in range(i, len(x) - 6):
            if ('</div>' == x[j:j+6]):
                break
            else:
                curr += x[j]
        curr += "</div>"
        inside_pre = False
        for i in range(len(curr) - 6):
            if (curr[i:i+5] == "<pre>"):
                inside_pre = True
            
            if (inside_pre):
                if (curr[i:i+2] == "\\n"):
                    curr = curr[:i] + "<br>" + curr[i+2:]
            
            if (curr[i:i+6] == "</pre>"):
                inside_pre = False

        curr = curr.replace("\\n", "")
        curr = curr.replace("\\r", "")
        answers.append(curr)

    html = '''<style> pre {
        padding: 10px;
        background-color: #E8EBEF;
    } </style>'''
    html += '<div>'
    html += '<h1 class="m-4">{}</h1>'.format(error)
    for i in answers:
        html += '''
        <div class="card m-4 p-4" style="width: 35rem; box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
            {}            
        </div>
        '''.format(i)
    # print(html)
    return html
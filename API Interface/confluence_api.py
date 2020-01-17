import requests

def allPages():
    r = requests.get("https://kernel-panic.atlassian.net/wiki/rest/api/content?expand=space,body.view,version,container", auth=('hkchheda_b17@it.vjti.ac.in', 'NDOzGw8BLJDCj8FGZL3x574E'))
    data = r.json()

    html = "<div class='container p-4'><h2>ALL Pages </h2>"
    for page in data["results"]:
        html += '''<div class="card p-4 mt-4" style="box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
            <div style="font-size: 1.25rem;">{}</div>
            <hr>
            <div><b>Author:</b> {}</div>
            <div><b>Type: </b> {}</div>
            <div><b>Space: </b> {}</div>
            <div><b>Status: </b> {}</div>
            <div><b>Created: </b> {}</div>
            <hr>
            <div><b>Content: </b> {}</div>
            <hr>
            <div><b>Descrption</b><br>{}</div>
        </div>
    '''.format(page["title"], page["version"]["by"]["displayName"], page["type"], page["space"]["name"], page["status"], page["version"]["friendlyWhen"], page["body"]["view"]["value"], page["space"]["_expandable"]["description"])
        
    html += "</div>"
    return html    

def pageByTitle(title):
    r = requests.get("https://kernel-panic.atlassian.net/wiki/rest/api/content?title={}&expand=space,body.view,version,container".format(title), auth=('hkchheda_b17@it.vjti.ac.in', 'NDOzGw8BLJDCj8FGZL3x574E'))
    page = r.json()["results"][0]

    html = "<div class='container p-4'><h2>Page Details for {}</h2>".format(title)
    html += '''<div class="card p-4 mt-4" style="box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
        <div style="font-size: 1.25rem;">{}</div>
        <hr>
        <div><b>Author:</b> {}</div>
        <div><b>Type: </b> {}</div>
        <div><b>Space: </b> {}</div>
        <div><b>Status: </b> {}</div>
        <div><b>Created: </b> {}</div>
        <hr>
        <div><b>Content: </b> {}</div>
        <hr>
        <div><b>Descrption</b><br>{}</div>
    </div>
'''.format(page["title"], page["version"]["by"]["displayName"], page["type"], page["space"]["name"], page["status"], page["version"]["friendlyWhen"], page["body"]["view"]["value"], page["space"]["_expandable"]["description"])
        
    html += "</div>"
    return html    


def allBlogPost():
    r = requests.get("https://kernel-panic.atlassian.net/wiki/rest/api/content?expand=space,body.view,version,container", auth=('hkchheda_b17@it.vjti.ac.in', 'NDOzGw8BLJDCj8FGZL3x574E'))
    data = r.json()
    print(data)

    html = "<div class='container p-4'><h2>ALL BlogPosts </h2>"
    for page in data["results"]:
        if page["type"] == "blogpost":
            html += '''<div class="card p-4 mt-4" style="box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
                <div style="font-size: 1.25rem;">{}</div>
                <hr>
                <div><b>Author:</b> {}</div>
                <div><b>Type: </b> {}</div>
                <div><b>Space: </b> {}</div>
                <div><b>Status: </b> {}</div>
                <div><b>Created: </b> {}</div>
                <hr>
                <div><b>Content: </b> {}</div>
                <hr>
                <div><b>Descrption</b><br>{}</div>
            </div>
        '''.format(page["title"], page["version"]["by"]["displayName"], page["type"], page["space"]["name"], page["status"], page["version"]["friendlyWhen"],page["body"]["view"]["value"],  page["space"]["_expandable"]["description"])
        
    html += "</div>"
    return html    

def blogPostbyTitle(title):
    pageByTitle(title)

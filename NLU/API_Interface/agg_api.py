import requests
from datetime import date

def allPR_RecentlyUpdatedIssues():
    r = requests.get("http://localhost:7990/rest/api/1.0/dashboard/pull-requests", \
        auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()

    html = "<div class='container p-4'><h2>Pull Requests</h2>"
    for pr in data["values"]:
        html += '''
                <div class="card p-4 mt-4" style="width: 30rem; box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
                    <div style="font-size: 1.25rem;">{}</div>
                    <hr>
                    <div><b>Author:</b> {}</div>
                    <div><b>Repo:</b> {}</div>
                    <div><b>State: </b> {}</div>
                    <div><b>Created: </b> {}</div>
                    <hr>
                    <div><b>Descrption</b><br> {}</div>
                </div>
            </div>
        '''.format(pr["title"], pr["author"]["user"]["displayName"], \
            pr["fromRef"]["repository"]["name"], \
            pr["state"], pr["createdDate"], pr["description"])

    r = requests.get('http://localhost:8080/rest/api/2/search', auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()
    html += "<div class='container p-4'><h2>Recently Updated Issues</h2>"
    for issue in data["issues"]:
        if issue["fields"]["updated"][0:10] == date.today().strftime("%Y-%m-%d"):
            html += '''
                <div class="card p-4 mt-4" style="display: block; width: 25rem; box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
                    <h3>{}</h3>
                    <hr>
                    <div><b>Reporter:</b> {}</div>
                    <div><b>Assignee:</b> {}</div>
                    <div><b>Status:</b> {}</div>
                    <div><b>Key:</b> {}</div>
                    <div><b>Priority:</b> {}</div>
                    <div><b>Watches:</b> {}</div>
                    <div><b>Created:</b> {}</div>
                </div>
            '''.format(issue["fields"]["summary"], issue["fields"]["reporter"]["displayName"], "Not Assigned" if (type(issue["fields"]["assignee"]) == type(None)) else issue["fields"]["assignee"]["displayName"], \
                issue["fields"]["status"]["name"], issue["key"], issue["fields"]["priority"]["name"], issue["fields"]["watches"]["watchCount"], \
                    issue["fields"]["created"])
    html += "</div>"
    return html


def allPR_Pages():
    r = requests.get("http://localhost:7990/rest/api/1.0/dashboard/pull-requests", \
        auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()

    html = "<div class='container p-4'><h2>Pull Requests by</h2>"
    for pr in data["values"]:
        html += '''
                <div class="card p-4 mt-4" style="width: 30rem; box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
                    <div style="font-size: 1.25rem;">{}</div>
                    <hr>
                    <div><b>Author:</b> {}</div>
                    <div><b>Repo:</b> {}</div>
                    <div><b>State: </b> {}</div>
                    <div><b>Created: </b> {}</div>
                    <hr>
                    <div><b>Descrption</b><br> {}</div>
                </div>
            </div>
        '''.format(pr["title"], pr["author"]["user"]["displayName"], \
            pr["fromRef"]["repository"]["name"], \
            pr["state"], pr["createdDate"], pr["description"])

    r = requests.get("http://localhost:8090/rest/api/content?expand=space,body.view,version,container&os_authType=basic", auth=("sm446-sih2020", "halva@puri123"))
    data = r.json()

    html += "<div class='container p-4'><h2>ALL Pages </h2>"
    for page in data["results"]:
        html += '''<div class="card p-4 mt-4" style="box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
            <div style="font-size: 1.25rem;">{}</div>
            <hr>
            <div><b>Author:</b> {}</div>
            <div><b>Type: </b> {}</div>
            <div><b>Space: </b> {}</div>
            <div><b>Status: </b> {}</div>
            <hr>
            <div><b>Content: </b> {}</div>
            <hr>
            <div><b>Descrption</b><br>{}</div>
        </div>
    '''.format(page["title"], page["version"]["by"]["displayName"], page["type"], page["space"]["name"], page["status"], page["body"]["view"]["value"], page["space"]["_expandable"]["description"])
        
    html += "</div>"
    return html

def allUsers_Project():
    r = requests.get("http://localhost:7990/rest/api/1.0/admin/users", \
        auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()
    html = '''
        <div class='container p-4'><h3>Users</h3>
        <div class="jumbotron p-3">
    '''

    for user in data["values"]:
        html += '''
            <li style="font-size: 1.25rem;">
                <strong>Name:{}</strong>
            </li>
            <li style="font-size: 1.25rem;">
                <strong>Display Name:{}</strong>
            </li>
            <li style="font-size: 1.25rem;">
                <strong>Email:{}</strong>
            </li>
            <hr>
        '''.format(user["name"], user["displayName"], user["emailAddress"])

    html += "</div></div>"

    r = requests.get('http://localhost:8080/rest/api/2/project', auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()
    html += '''
        <div class='container p-4'><h3>PROJECTS</h3>
        <div class="jumbotron p-3">
    '''
    for project in data:
        html += '<li style="font-size: 1.25rem;">{}</li>'.format(project["name"])
    html += "</div></div>"

    print(html)

    return html
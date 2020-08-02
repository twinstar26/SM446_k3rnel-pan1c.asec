import requests

def allPullRequests():
    r = requests.get("http://localhost:7990/rest/api/1.0/dashboard/pull-requests", \
        auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()

    html = "<div class='container p-4'><h2>Pull Requests by @{}</h2>".format(uname)
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

    return html

def allPullRequestByUserName(uname):
    r = requests.get("http://localhost:7990/rest/api/1.0/dashboard/pull-requests", \
        auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()

    html = "<div class='container p-4'><h2>Pull Requests by @{}</h2>".format(uname)
    for pr in data["values"]:
        if (pr["author"]["user"]["name"] == uname):
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

    return html

def users():
    r = requests.get("http://localhost:7990/rest/api/1.0/admin/users", \
        auth=('sm446-sih2020', 'halva@puri123'))
    data = r.json()

    users = []
    for user in data["values"]:
        users.append([user["name"], user["displayName"], user["emailAddress"]])
    
    return users

def allUsers():
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

    return html

def allRepositoriesByProjectKey(p_key):
    r = requests.get("http://localhost:7990/rest/api/1.0/projects/{}/repos".format(p_key), \
        auth=('sm446-sih2020', 'halva@puri123'))

    data = r.json()
    html = '''
        <div class='container p-4'><h3>Repos in {}</h3>
        <div class="jumbotron p-3">
    '''.format(p_key)

    for repo in data["values"]:
        html += '<li style="font-size: 1.25rem;"><a href="{}">{}</a></li>'\
            .format(repo["links"]["clone"][0]["href"], repo["name"])
    html += "</div></div>"

    return html
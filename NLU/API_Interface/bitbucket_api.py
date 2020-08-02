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

def allRepositoriesByWorkspace(workspace):
    r = requests.get("https://api.bitbucket.org/2.0/repositories/{}".format(workspace), \
        auth=('atharvaveer', 'einstien@123'))

    data = r.json()
    html = '''
        <div class='container p-4'><h3>Repos in {}</h3>
        <div class="jumbotron p-3">
    '''.format(workspace)

    for repo in data["values"]:
        html += '<li style="font-size: 1.25rem;"><a href="{}">{}</a></li>'\
            .format(repo["links"]["clone"][0]["href"], repo["full_name"])
    html += "</div></div>"

    return html

def allCommitsByProjectNameAndWorkspace(pname, workspace):
    r = requests.get("https://api.bitbucket.org/2.0/repositories/{}/{}/commits".format(workspace, pname), \
        auth=('atharvaveer', 'einstien@123'))
    data = r.json()

    html = '''
        <div class='container p-4'><h2>Commits in {}/{}</h2>
    '''.format(workspace, pname)

    for commit in data["values"]:
        html += '''<div class="card p-4 mt-4" style="width: 30rem; box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
                <div style="font-size: 1.25rem;">{}</div>
                <hr>
                <div><b>Author:</b> {}</div>
                <div><b>Repo:</b> {}</div>
                <div><b>Hash: </b> <a href="{}">{}</a></div>
                <div><b>Created: </b> {}</div>
            </div>
        '''.format(commit["rendered"]["message"]["html"], commit["author"]["raw"], \
            commit["repository"]["full_name"], commit["links"]["html"]["href"], commit["hash"], \
                commit["date"])
    
    html += "</div>"
    return html

def allIssuesByProjectNameAndWorkspace(pname, workspace):
    r = requests.get("https://api.bitbucket.org/2.0/repositories/{}/{}/issues".format(workspace, pname), \
        auth=('atharvaveer', 'einstien@123'))
    data = r.json()

    html = '''
        <div class='container p-4'><h2>Issues in {}/{}</h2>
    '''.format(workspace, pname)

    for issue in data["values"]:
        html += '''<div class="card p-4 mt-4" style="width: 30rem; box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
                <div style="font-size: 1.25rem;">{}</div>
                <hr>
                <div><b>Reporter: </b> {}</div>
                <div><b>Repo: </b> <a href="{}"> {}</a></div>
                <div><b>Priority: </b> {}</div>
                <div><b>Kind: </b> <a href="{}">{}</a></div>
                <div><b>Watches: </b> {}</div>
                <div><b>Created: </b> {}</div>
            </div>
        '''.format(issue["title"], issue["reporter"]["display_name"], \
            issue["repository"]["links"]["html"]["href"], issue["repository"]["full_name"], \
            issue["priority"], issue["links"]["html"]["href"], issue["kind"], \
            issue["watches"], issue["created_on"][:10])
    
    html += "</div>"
    print(html)
    return html

def allPullRequestByProjectNameAndWorkspace(pname, workspace):
    r = requests.get("https://api.bitbucket.org/2.0/repositories/{}/{}/pullrequests".format(workspace, pname), \
        auth=('atharvaveer', 'einstien@123'))
    data = r.json()

    html = "<div class='container p-4'><h2>Pull Requests in {}/{}</h2>".format(workspace, pname)
    for pr in data["values"]:
        html += '''
                <div class="card p-4 mt-4" style="width: 30rem; box-shadow: 0 1px 6px 0 rgba(32,33,36,0.28);">
                    <div style="font-size: 1.25rem;">{}</div>
                    <hr>
                    <div><b>Author:</b> {}</div>
                    <div><b>Repo:</b> {}</div>
                    <div><b>Branch: </b> {}</div>
                    <div><b>State: </b> {}</div>
                    <div><b>Created: </b> {}</div>
                    <hr>
                    <div><b>Descrption</b><br> {}</div>
                </div>
            </div>
        '''.format(pr["title"], pr["author"]["display_name"], \
            pr["destination"]["repository"]["full_name"], pr["destination"]["branch"]["name"], \
            pr["state"], pr["created_on"][:10], pr["description"])

    return html
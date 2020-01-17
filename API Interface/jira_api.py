# from jira import JIRA
# def jira_auth():
#     user = "hkchheda_b17@it.vjti.ac.in"
#     apikey = "NDOzGw8BLJDCj8FGZL3x574E"
#     server = "https://kernel-panic.atlassian.net/"
#     options = {
#         'server': server
#     }
#     return JIRA(options, basic_auth=(user, apikey))

# # ATTRIBUTES WHICH WE DISPLAY FOR ISSUE
# * Watches
# * Comments
# * Description
# * Attachments
# * Reporter
# * Assignee
# * Labels
# * Created
# * Updated
# * Linked Issues

import requests
from pprint import pprint

def allIssuesByProject(p_name):
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/search?jql=project={}'.format(p_name), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    data = r.json()
    html = "<div class='container p-4'><h1>Issues for Project: {}</h1>".format(p_name)
    for issue in data["issues"]:
        html += '''
            <div class="card p-4 mt-4" style="display: block; width: 25rem;">
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
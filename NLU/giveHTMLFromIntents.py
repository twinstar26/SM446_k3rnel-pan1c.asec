from API_Interface.jira_api import *
from API_Interface.confluence_api import *
from API_Interface.stackoverflow_api import *
from API_Interface.bitbucket_api import *
from API_Interface.mom_api import *

def giveHTMLFromIntents(jsonResponse):
    try:
        print(jsonResponse)

        # JIRA
        if jsonResponse['intent']["intentName"] == "allIssuesByProject":
            return allIssuesByProject(jsonResponse["slots"][0]["rawValue"])
        elif jsonResponse['intent']["intentName"] == "allIssuesByProjectAndIssueType":
            return allIssuesByProjectAndIssueType(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"])
        elif jsonResponse['intent']["intentName"] == "allIssuesByAssigneeAndIssueType":
            return allIssuesByAssigneeAndIssueType(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"])
        elif jsonResponse['intent']["intentName"] == "allIssuesByAssigneeAndProjectName":
            return allIssuesByAssigneeAndProjectName(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"])
        elif jsonResponse['intent']["intentName"] == "allIssuesByAssigneeProjectNameAndIssueType":
            return allIssuesByAssigneeProjectNameAndIssueType(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"], jsonResponse["slots"][2]["rawValue"])
        elif jsonResponse['intent']["intentName"] == "issueByIssueKey":
            return issueByIssueKey(jsonResponse["slots"][0]["rawValue"])
        elif jsonResponse['intent']["intentName"] == "allProjects":
            return allProjects()
        elif jsonResponse['intent']['intentName'] == "allRecentlyUpdateIssues":
            return allRecentlyUpdateIssues()

        # STACKOVERFLOW
        elif jsonResponse['intent']["intentName"] == "topPostAnswer":
            return topPostAnswer(jsonResponse["input"])

        # MOM
        elif jsonResponse['intent']['intentName'] == "momDetails":
            return momDetails(jsonResponse["slots"][0]["rawValue"])
        elif jsonResponse['intent']['intentName'] == "summarizeMeeting":
            return summarizeMeeting()


        # BITBUCKET
        elif jsonResponse['intent']['intentName'] == "allPullRequests":
            return allPullRequests()
        elif jsonResponse['intent']["intentName"] == "allPullRequestByUserName":
            return allPullRequestByUserName(jsonResponse["slots"][0]["rawValue"])
        elif jsonResponse['intent']['intentName'] == "allUsers":
            return allUsers()
        elif jsonResponse['intent']['intentName'] == "allRepositoriesByProjectKey":
            return allRepositoriesByProjectKey(jsonResponse["slots"][0]["rawValue"])

        # CONFLUENCE
        elif jsonResponse['intent']["intentName"] == "allPages":
            return allPages()
        elif jsonResponse['intent']["intentName"] == "pageByTitle":
            return pageByTitle(jsonResponse["slots"][0]["rawValue"])
        elif jsonResponse['intent']["intentName"] == "allBlogPost":
            return allBlogPost()

    except Exception as e:
        print(e)
        return "Insufficient information...."

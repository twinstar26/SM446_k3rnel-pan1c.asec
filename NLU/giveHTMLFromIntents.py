from API_Interface.jira_api import *

def giveHTMLFromIntents(jsonResponse):
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
    elif jsonResponse['intent']["intentName"] == "allEpicsByProject":
        return allEpicsByProject(jsonResponse["slots"][0]["rawValue"])
    elif jsonResponse['intent']["intentName"] == "allEpicsByProjectAndIssueType":
        return allEpicsByProjectAndIssueType(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"])
    elif jsonResponse['intent']["intentName"] == "allEpicsByAssigneeAndIssueType":
        return allEpicsByAssigneeAndIssueType(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"])
    elif jsonResponse['intent']["intentName"] == "allEpicsByAssigneeAndProjectName":
        return allEpicsByAssigneeAndProjectName(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"])
    elif jsonResponse['intent']["intentName"] == "allEpicsByAssigneeProjectNameAndIssueType":
        return allEpicsByAssigneeProjectNameAndIssueType(jsonResponse["slots"][0]["rawValue"], jsonResponse["slots"][1]["rawValue"], jsonResponse["slots"][2]["rawValue"])
    elif jsonResponse['intent']["intentName"] == "epicByIssueKey":
        return epicByIssueKey(jsonResponse["slots"][0]["rawValue"])
    
    
    
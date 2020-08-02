# PROJECTS

* All projects  
https://kernel-panic.atlassian.net/rest/api/2/project

# ISSUES
* fields.issuetype.name = "Task"

## BASED ON PROJECT

* All issues by Project Name: ProjectName    
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

* All Todo issues: ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

* All In progress issues: ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

* All Done issues: ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

## BASED ON USERNAME

* All issues by a user: UserName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Todo issues: UserName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All In progress issues: UserName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Done issues: UserName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

## BASED ON BOTH

* All issues by a user: UserName, ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Todo issues: UserName, ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All In progress issues: UserName, ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Done issues: UserName, ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* Get issue by keyname: IssueKEY
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY

## COMMENTS
* Get comments for a given issue: IssueKEY  
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY/comment

## ATTACHMENT
* Get attachments for a given issue: IssueKEY  
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY?fields=attachment

## DESCRIPTION
* Get descrption for a given issue: IssueKEY  
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY?fields=description

# ATTRIBUTES WHICH WE DISPLAY FOR ISSUE
* Watches
* Comments
* Description
* Attachments
* Reporter
* Assignee
* Labels
* Created
* Updated
* Linked Issues

## REST API QUERIES
* Creating a new issue
/rest/api/2/issue [POST]

* Getting a issue
/rest/api/2/issue/{issueIdOrKey}

* Deleting a issue
/rest/api/2/issue/{issueIdOrKey}

* Getting all projects
/rest/api/2/project

* Creating a project
/rest/api/2/project

* Delete a Project
/rest/api/2/project/{projectIdOrKey}

# EPICS: ALMOST SAME AS ISSUES
* fields.issuetype.name = "Epic"

## BASED ON PROJECT
x
* All epics by Project Name: ProjectName
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

* All Todo epics: ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

* All In progress epics: ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

* All Done epics: ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=project=ProjectName

## BASED ON USERNAME

* All epics by a user: UserName
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Todo epics: UserName
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All In progress epics: UserName
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Done epics: UserName
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

## BASED ON BOTH

* All epics by a user: UserName, ProjectName
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Todo epics: UserName, ProjectName
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All In progress epics: UserName, ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* All Done epics: UserName, ProjectName  
https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee=UserName

* Get epic by keyname: IssueKEY
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY

## COMMENTS
* Get comments for a given epic: IssueKEY  
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY/comment

## ATTACHMENT
* Get attachments for a given epic: IssueKEY  
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY?fields=attachment

## DESCRIPTION
* Get description for a given epic: IssueKEY  
https://kernel-panic.atlassian.net/rest/api/2/issue/IssueKEY?fields=description
# bitbucket

## pull request
- Returns all pull requests authored by the specified user by {selected_user}
https://api.bitbucket.org/2.0/pullrequests/{selected_user}

## Repository
- Returns a paginated list of all public repositories of {workspace}
https://api.bitbucket.org/2.0/repositories/{workspace}

- commits {workspace}, {repo_slug}
https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/commits

- forks test remain {workspace}, {repo_slug}
https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/forks

- issues {workspace}, {repo_slug}
https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/issues

- pull reqquest {workspace}, {repo_slug}
https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pullrequests

- version {workspace}, {repo_slug}
https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/versions

## Bitbucket new REST APIS
* Creating a new project
/rest/api/1.0/projects

* Deleting a new project
/rest/api/1.0/projects/{projectKey}

* Getting a project by project key
/rest/api/1.0/projects/{projectKey}

* Create a new repository
/rest/api/1.0/projects/{projectKey}/repos

* Getting repos with project key
/rest/api/1.0/projects/{projectKey}/repos

* Getting all pull requests from repos
/rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-request

* Creating a pull request 
/rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-requests
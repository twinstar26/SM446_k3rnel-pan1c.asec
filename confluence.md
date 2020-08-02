## BLOGPOSTS
* Get all the blogposts
https://kernel-panic.atlassian.net/wiki/rest/api/content?type=blogpost&expand=space,body.view,version,container

* Get blogpost by id: ID
https://kernel-panic.atlassian.net/wiki/rest/api/content/{ID}?expand=space,body.view,version,container

* Get blogpost by title: Title
https://kernel-panic.atlassian.net/wiki/rest/api/content?type=blogpost&title={Title}&expand=space,body.view,version,container

## PAGES
* Get all the pages
https://kernel-panic.atlassian.net/wiki/rest/api/content?expand=space,body.view,version,container

* Get page by id: ID
https://kernel-panic.atlassian.net/wiki/rest/api/content/{ID}?expand=space,body.view,version,container

* Get page by title: Title
https://kernel-panic.atlassian.net/wiki/rest/api/content?title={Title}&expand=space,body.view,version,container

## COMMENTS
* Get comment by ID: ID
https://kernel-panic.atlassian.net/wiki/rest/api/content/{ID}/child/comment

# FEATURES WE PROVIDE IN BLOGPOST / PAGES
* Author
* Title
* Type: (page / blogpost)
* Content
* Comments
* status
* friendlyWhen

## Confluence REST APIS
* Finding blogpost
http://localhost:8080/confluence/rest/api/content?type=blogpost&start=0&limit=10&expand=space,history,body.view,metadata.labels"

* Find a page by title and space key
"http://localhost:8080/confluence/rest/api/content?title={myPage%20Title}&expand=history"

* By ID
"http://localhost:8080/confluence/rest/api/content?expand=space,body.view,version,container&os_authType=basic"

* Creating a new page
curl -u admin:admin -X POST -H 'Content-Type: application/json' -d '{"type":"page","title":"new page",
"space":{"key":"TST"},"body":{"storage":{"value":"<p>This is <br/> a new page</p>","representation":
"storage"}}}' 
http://localhost:8080/confluence/rest/api/content/

* Delete a page
http://localhost:8080/confluence/rest/api/content/3604482
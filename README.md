# flask-tutorial
python flask tutorial 

This is a flask tutorial based on flask web page.
This application is for blog management.

When I wirte a code, there is some issues. The issues is g.
When user logon the system, set g.user from user table in database.
I think g.user could be applied all the requsts once it was created.
But it was not applied.
So I set the user information to session.
It was perfectly worked.

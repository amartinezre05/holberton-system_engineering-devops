
# Postmortem
![gif](https://media.giphy.com/media/3orieLeZL5kyNqiLfO/giphy.gif)
## Issue Summary
When the users try to login to web application receives a terrific answer 401 Error, this affects all the users. The authentication process is through Gmail an is the only way so nobody can access.


100% of the users can't entry

Lapse of time [Colombia time zone (GMT-5)]
08:00 - 09:00

## Timeline

- 08:00 The first occurrence of the problem
- 08:10 Firefighter developer start to read about the 401 error for Gmail authentication
- 08:20 Info refers to the keys in the console of google API
- 08:35 Validate that the keys on the console are ok
- 08:40 Compare the keys in the credentials file
- 08:55 Find the problem with a change in the file credentials
- 09:00 Problem was resolved

## Root Cause

When the search for the keys in the credentials file encounter that keys inside the file were different from the keys on the google console. The origin of the problem was because differents devs overwrote the file and make inconsistencies after the last merge.
![unauthorized](https://github.com/amartinezre05/holberton-system_engineering-devops/blob/master/0x18-webstack_monitoring/Screenshot%20from%202020-05-31%2013-49-28.png)

## Corrective and preventative measures

- Make an alert if the credentials file was modified
- Validate every file to load was in rebase with the master files
- Read the readme to understand how is the flow of the web application

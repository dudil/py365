# py365
## What is it?
Python Library for App Development over MS Graph365

The concept is simple - look at the API docs and "copy" same structure.   
While not very "pythonic" (I would guess - what does it mean anyway?),   
it is easy to follow and go along:
Just open the [official API reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)

## What is it good for?
If you are using any of MS services you are getting to the point that automating things via code is the best way to unleash it true massive power.

While you can use .net core and other services, scripting with python is still very convenient if all you need is just small or serveless scripts.

### Target Python - 3.6
Since this is the version used by Azure serverless engines.

## How to use it?
```bash
$ pip install py365
```

```python
# Graph365 is the main access point to the MS Graph
# rsc is the graph resources we use to feed the graph API
from py365 import Graph365, rsc

#Connect to the tenant
g365 = Graph365(appId=config['app_id'],
                appSecret=config['app_secret'],
                tenantId=config['tenant_id']) 

# Create new user 
# API doc: https://docs.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0
user = rsc.User(displayName="Steve J", userPrincipalName="steve.j@consotco.com")
g365.users.createUser(newUser=user)

```

## API implemented (Basic)
-[x] Create User
-[x] Get User
-[x] Update user
-[X] Send email
-[X] Guest Invite

## What is next? (ATM)
-[ ] Online excel API
-[ ] Get Planner tasks
-[ ] Add unit testings
-[ ] Replace [ADAL](https://github.com/AzureAD/azure-activedirectory-library-for-python)
 with [MSAL](https://github.com/AzureAD/microsoft-authentication-library-for-python) for authentication
-[ ] Check for version with APIs
-[ ] Check for sufficient authority (permissions) before calling an API
-[ ] Check response type and handle errors




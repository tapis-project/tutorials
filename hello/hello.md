# Hello, Tapis
In this first tutorial, we learn to authenticate with Tapis using our TACC username 
and password and make our first API request.

As discussed in the introduction, we will use the official Tapis Python SDK for all of our 
interactions with the APIs. The Python SDK provides Python-native methods and objects for 
making HTTP requests and parsing HTTP responses to and from the Tapis API. In order to do 
just about anything with Tapis, we will need to authenticate.

Tapis authentication is based on tokens (specifically, [JSON Web Tokens](jwt.io)). To
make an API request to Tapis, you first need to generate a token. Tapis can be configured
to support the requirements of different projects and institutions, including different
mechanisms for generating tokens. For this tutorial, we will generate a token using our
TACC username and password. (If you do not have a TACC account, check the 
[prerequisites](https://tapis-project.github.io/tutorials/intro/intro/#prerequisites)
and sign up for an account [here](https://portal.tacc.utexas.edu/account-request).)

In your Jupyter notebook copy the blocks below and run them.
```
# Enter your TACC username and password
import getpass

username = input("Username: ")
password = getpass.getpass(prompt="Password: ", stream=None)
```

All of our interactions with Tapis will go through the `Tapis` python object.
In particular, we can use it to generate a token. 

In your Jupyter notebook copy the blocks below and run them.
You will get a Tapis v3 token to interact with the Tapis services.

```
from tapipy.tapis import Tapis
base_url = "https://tacc.tapis.io"

# Create python Tapis client for user
client = Tapis(base_url= base_url, username=username, password=password)

# *** Tapis v3: Call to Tokens API
client.get_tokens()

# Print Tapis v3 token
client.access_token
```

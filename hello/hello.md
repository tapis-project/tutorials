# Hello, Tapis
In this first tutorial, we learn to authenticate with Tapis using our TACC username 
and password and make our first API request.

As discussed in the introduction, we will use the official Tapis Python SDK for all of our 
interactions with the APIs. The Python SDK provides Python-native methods and objects for 
making HTTP requests and parsing HTTP responses to and from the Tapis API. In order to do 
just about anything with Tapis, we will need to authenticate.

Tapis authentication is based on tokens (specifically, [JSON Web Tokens](jwt.io)), and 
different projects can 

In your Jupyter notebook copy the blocks below and run them.
You will get a Tapis v3 token to interact with the Tapis services.
```
username = input('Username: ')
password = getpass.getpass(prompt='Password: ', stream=None)
```
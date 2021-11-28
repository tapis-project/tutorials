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

In your Jupyter notebook copy the block below and run it.
You will get a Tapis v3 token to interact with the Tapis services.

```
from tapipy.tapis import Tapis
base_url = "https://tacc.tapis.io"

# Create python Tapis client for user
t = Tapis(base_url= base_url, username=username, password=password)

# *** Tapis v3: Call to Tokens API
t.get_tokens()

# Print Tapis v3 token
t.access_token
```
The output should look something similar to the following:

```

access_token: eyJ0eXAiOiJKV1...
claims: {'jti': 'dfada014-66ca-4f6e-a57a-48b618a79678', 'iss': 'https://tacc.tapis.io/v3/tokens', 
'sub': 'jstubbs@tacc', 'tapis/tenant_id': 'tacc', 'tapis/token_type': 'access', 
'tapis/delegation': False, 'tapis/delegation_sub': None, 'tapis/username': 'jstubbs', 
'tapis/account_type': 'user', 'exp': 1638153035, 'tapis/client_id': None, 
'tapis/grant_type': 'password'}
expires_at: 2021-11-29 02:30:35+00:00
expires_in: <function Tapis.add_claims_to_token.<locals>._expires_in at 0x7f110806a8b0>
jti: dfada014-66ca-4f6e-a57a-48b618a79678
original_ttl: 14400
```

The actual access token is the string labeled `access_token` beginning with `eyJ..` in 
the output above. The library dervived the other fields from the token itself, including 
the set of `claims`. When you make an API request to Tapis passing the token, the API uses
the claims to determine who you are and what accesses you have.

Now that we have an access token, we are ready to make our first authenticated API 
request to Tapis. For this "Hello, Tapis" tutorial, we'll make a call to the Profiles 
service to see that Tapis knows who we are.

Copy the following block into your notebook and run it.

```
t.authenticator.get_userinfo()

```
You should see your user information in output similar to the following:

```
create_time: None
dn: cn=jstubbs,ou=People,dc=tacc,dc=utexas,dc=edu
email: jstubbs@tacc.utexas.edu
given_name: Joe
last_name: Stubbs
mobile_phone: None
phone: None
uid: 811324
username: jstubbs
```
The API request syntax `t.authenticator.get_userinfo()` follows a common 
pattern: `t.<service>.<endpoint>(<parameters>)`. Here, the Tapis service we
are using is `authenticator` and the specific endpoint we are invoking is the
`get_userinfo()` endpoint. The `authenticator` service has many other endpoints which
you can read about in the Tapis reference 
[documentation](https://tapis.readthedocs.io/en/latest/technical/authentication.html) 
or in API [specification](https://tapis-project.github.io/live-docs/?service=Authenticator).


## Additional Resources
See the following links for more information about the above topics.

* _Authentication in Tapis_ - Reference [documentation](https://tapis.readthedocs.io/en/latest/technical/authentication.html)
* _Details on Tapis JWT_ - Reference [documentation](https://tapis.readthedocs.io/en/latest/technical/authentication.html#using-a-token)
* _Create a Token API Request_ - API [specification](https://tapis-project.github.io/live-docs/?service=Authenticator#operation/create_token)
* _User Info API Request_ - API [specification](https://tapis-project.github.io/live-docs/?service=Authenticator#operation/get_userinfo).
# Registering Credentials for a System
Now that you have registered a system you will need to register credentials to allow 
Tapis to access the host. Various authentication methods can be used to access a system, 
such as PASSWORD and PKI_KEYS. Here we will cover registering keys first (this was the
default authentication method we used when registering our Stampede2 system) and then 
registering a password.

## Registering SSH Keys
Copy and paste the following code into your notebook.

``` python
t.systems.createUserCredential(systemId='<system_id>', 
                               userName='<system_user>', 
                               privateKey='<private_key>',
                               publicKey='<publicKey>'))
```
Replace:
* `<system_id>` with the id of the system you registered in the previous tutorial.
* ``<system_user>`` with the POSIX user name on the host that Tapis is using on the system
  (i.e., the effective user).
* `<private_key>` with the private key for the host.
* `<public_key>` with the public key for the host.


## Registering a Password
Copy and paste the following code into your notebook.

``` python
t.systems.createUserCredential(systemId='tapisv3-exec-<userid>', 
                               userName='<userid>', 
                               password='<password>'))
```
Replace:
* ``<userid>`` with your username
* ``<password>`` with your password for the host.

## Next Steps
With our system registered with credentials, we can now use the Files API to manage 
data on the system.

 [Next-> Managing Data on a System](../files/data.md)

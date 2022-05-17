# Registering Credentials for a System
Now that you have registered a system you will need to register one or more credentials 
for it to allow Tapis to access the host. Various authentication methods can be used to access a system, 
such as PASSWORD and PKI_KEYS. Here we will cover registering keys first (this was the
default authentication method we used when registering our Stampede2 system) and then 
registering a password.


Please make sure to generate a SSH Key pair on Stampede2. Create a .ssh directory in your home directory and run the command below:

```
ssh-keygen -m PEM -f id_rsa

```
Do not ennter passphrase. Once the keys are created copy the public key to authorized keys file on Stampede2. <br/>
Keep the public key and private key handy, these are required for creating user credentials. For private key, it is recommended to get a one liner private key using the command below. 

```
awk -v ORS='\\n' '1' private_key_name

```


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

This should add a credential for the system. Tapis will use this credential any time
it tries to access the system as the `<system_user>` user. Note that this might be 
different from your Tapis user name.

## Registering a Password
Copy and paste the following code into your notebook.

``` python
t.systems.createUserCredential(systemId='<system_id>',
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

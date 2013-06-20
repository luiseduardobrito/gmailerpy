gmailerpy
=========

gmailer.py - easy gmail bulk send in python


###Getting Started


Send email to a lot of recipients easily using python, json and gmail.

First, clone the repo and extract somewhere. Then, import in your python script:

 ```python
  from google import gmailer
      
  u = gmailer.User("user@gmail.com", "password")
  g = gmailer.Gmailer(u)
      
  g.add_recipients("joaochencci@gmail.com")
  g.set_subject("testando o script")
  g.set_body("ola joao")
      
  g.send()
  ```

For bulk sending, just call `add_recipients` method, from `Gmailer` class.

  ```python
  for email in list("joao@gmail.com", "chencci@gmail.com"):
    g.add_recipients(email)
  ```

Or even:

  ```python
    g.add_recipients("joao@gmail.com", "chencci@gmail.com", [...])
  ```

That's it! Now you got started.

###Templating

This script support email templating. For that, first you need to map the template with the desired params.

  ```python
  body = "<p>Hello <b>{{name}}</b>!</p><p>How are you doing?</p>"
  ```

Then you need to set the body type to be html, for the example showed above. Use the `set_body` method.

  ```python
  g.set_body(body, True)
  ```
  
###Documentation

This shall be reserved for a beatifully complete documentation that I might never write, so don't be lazy and go read the code, it's not so long!

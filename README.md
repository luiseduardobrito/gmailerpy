gmailerpy
=========

Simple script for bulk sending using [Gmail](http://gmail.com).

More info at my [personal page](http://about.me/luiseduardobrito) or at my [github page](http://luiseduardobrito.github.io)


###Getting Started


Send email to a lot of recipients easily using python, json and gmail.

First, clone the repo or download the zip and extract somewhere. Then, import it in your python as an external script:

 ```python
  import gmailer
      
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

For replacing values, just map them using `{{key}}` inside your subject and/or body content.

Example:

  ```python
  t = gmailer.Template("Metting at {{time}}") # specify email subject
  t.content("Hello {{name}}! How are you doing? Don't forget our metting tomowwor at {time}.")
  
  g.add_recipients(gmailer.Recipient("john@gmail.com", {
      'time': 'noon'
    }))
  
  g.add_recipients(gmailer.Recipient("clit@gmail.com", {
      'time': '14h'
    }))
  ```

Then you need to set the body type to be html, for the example showed above. Use the `set_body` method.

  ```python
  g.content(body)
  ```
###Roadmap

1. Create a method for importing all config and recipients from json file
2. HTML body messages deep tests (not tested even superficially)


###Documentation

You can read the methods and class references in the [docs folder](https://github.com/luiseduardobrito/gmailerpy/tree/master/docs) inside the repo, in a [text-file](https://github.com/luiseduardobrito/gmailerpy/blob/master/docs/docs.out) way or in a [html-file](https://github.com/luiseduardobrito/gmailerpy/blob/master/docs/gmailer.html) way.

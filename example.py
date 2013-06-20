#!/usr/bin/python
import gmailer

# say who you are
s = gmailer.Sender("email@gmail.com", "password")
g = gmailer.Gmailer(s)

# create a new template
t = gmailer.Template("Metting today at {{time}}")
t.content("Hello {{name}}, we'll meet at {{time}} in {{location}}.")
g.set_template(t)

# add a recipient
g.add_recipient(gmailer.Recipient("joao@gmail.com", {
		"name": "Joao",
		"time": "noon",
		"location": "FE-02"
	}))

# send and that's it
#g.send()
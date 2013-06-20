#!/usr/bin/python

import gmailer

# say who you are
s = Sender("email@gmail.com", "password")
g = Gmailer(s)

# create a new template
s.set_subject("Metting Today at {{time}}")
t = Template("Hello {{name}}, we'll meet at {{time}} in {{location}}.")
g.set_template(t)

# add a recipient
g.add_recipient(Recipient("joao@gmail.com", {
		"name": "Joao",
		"time": "noon",
		"location": "FE-02"
	}))

# send and that's it
g.send()
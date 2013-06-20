#!/usr/bin/python
import gmailer

# say who you are
s = gmailer.Sender("email@gmail.com", "password")
g = gmailer.Gmailer(s)

# create a new template
t = gmailer.Template("Meeting today at {{time}}")
t.content("Hello {{name}}, we'll meet at {{time}} in {{location}}.")
g.set_template(t)

# add a recipient
g.add_recipient(gmailer.Recipient("pereira@gmail.com", {
		"name": "Pereira",
		"time": "noon",
		"location": "FE-02"
	}))

g.add_recipient(gmailer.Recipient("clit@gmail.com", {
		"name": "Clit",
		"time": "19pm",
		"location": "FE-01"
	}))

# send and that's it
g.send()
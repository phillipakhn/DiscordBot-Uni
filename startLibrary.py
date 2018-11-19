import alastair as a

def modules(message):
    a.removeDuplicates()
    msg = ""
    #msg = msg + str(a.pyStart(message))
    msg = msg + str(a.human(message))
	msg = msg + str(a.ignore(message))
    
    with open("greetings.txt",'rb') as rfp:
		greetings = pickle.load(rfp)
	for i in greetings:	
		if message.content.startswith(i):
	        msg = str(a.greetings(greetings))
            
    if message.content.startswith('!URL'):
		with open("url.txt",'rb') as rfp:
			url = pickle.load(rfp)
	    msg = str(a.url(url))
        
    if message.content.startswith('!Test'):
	    msg = str(a.test())
        
    if message.content.startswith('!Update'):
	    a.update()
        
    if message.content.startswith('!Exit'):
	    a.exitBot()
        
    
	msg = msg + str(a.code(message))
	msg = msg + str(a.gitHelp(message))
	msg = msg + str(a.temperature(message))
	msg = msg + str(a.fQuestion(message.content))
	msg = msg + str(a.fResponse(message.content))
	msg = msg + str(a.add(oldmsg, message))
	msg = msg + str(a.remove(message))
    
    if message.content.startswith('!Display'):
	    msg = str(a.display())
        
	msg = msg + str(a.displayCommands(message))
	msg = msg + str(a.webcam(message))

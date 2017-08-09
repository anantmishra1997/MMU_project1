print 'Let\'s get started'
spy_salutation=raw_input('What should we call you(Mr or Mrs) ?:')
spy_name=raw_input('What is your name ?:')

if (len(spy_name)==0):
    print "A spy needs a Proper Name"
else:
    print 'Welcome '+spy_salutation+' '+spy_name+' glad to meet you'
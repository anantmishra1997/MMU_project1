
print 'Let\'s get started.....!'
spy_salutation=raw_input('What should we call you(Mr or Mrs) ?:')
spy_name=raw_input('What is your name ?:')

if (len(spy_name)==0):
    print 'A spy needs a Proper Name'
else:
    print 'Welcome '+spy_salutation+' '+spy_name+' glad to meet you'
spy_age=0
spy_rating=0.0
spy_online=False
spy_age=int(raw_input("Enter the age"))
if (spy_age > 17 & spy_age < 50):
    print"Entered"
else:
    print"Age error"
spy_rating=float(raw_input("Enter the rating"))
if spy_rating > 4.5:
    print" Great Ace..!"
    spy_online = True
    print "Authentication Complete..Welcome" +" "+ spy_salutation + " " +spy_name + " age: " + str(spy_age) + " rating: " + str(spy_rating)
elif spy_rating >=2.5 and spy_rating <=4.5:
    print"You're the one"
    spy_online = True
    print "Authentication Complete..Welcome "+ spy_salutation + " " + spy_name + " age: " + str(spy_age) + " rating: " + str(spy_rating)
else:
    print"Sorry"

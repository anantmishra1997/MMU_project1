from spy_details import spy
status_message=["Why so serious..son!!","Never say Never","I'm in love with the shape of you"]
friends_name=[]
friends_age=[]
friends_rating=[]
friends_is_online=[]
print "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)? "
question=raw_input("Do you want to continue .......(Y/N)")
def start_chat(spy_name,spy_age,spy_rating):
    current_staus=None
    spy_name = spy_salutation + " " + spy_name
    if spy_age > 12 and spy_age < 50:
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating)
        show_menu=True
        while show_menu:
            menu_choice="What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n""
            menu_choice = raw_input(menu_choice)
            if len(menu_choice>0):
                menu_choice=int(menu_choice)
            if menu_choice==1:
                print("So,the spy wants to add a status....")
            elif menu_choice==2:
                print("So,the spy wants to add a friend....")
            elif menu_choice==3:
                print("Sshh...spy wants to send a secret message")
            elif menu_choice==4:
                print("You want to read the secret message")
            elif menu_choice==5:
                print("You want to read the chats")
            elif menu_choice==6:
                print("Bye spy")
            else:
                print("Wrong choice")
if question.upper()=="Y":
    start_chat()
elif question.upper()=="N":
    spy_salutation = raw_input('What should we call you(Mr or Mrs) ?:')
    spy_name = raw_input('What is your name ?:')
    if (len(spy_name) == 0):
        print 'A spy needs a Proper Name'
    else:
        print 'Welcome ' + spy_salutation + ' ' + spy_name + ' glad to meet you'
    spy_age = 0
    spy_rating = 0.0
    spy_online = False
    spy_age = int(raw_input("Enter the age"))
    if (spy_age > 17 & spy_age < 50):
        print"Entered"
    else:
        print"Age error"
    spy_rating = float(raw_input("Enter the rating"))
    if spy_rating > 4.5:
        print" Great Ace..!"
        spy_online = True
        print "Authentication Complete..Welcome" + " " + spy_salutation + " " + spy_name + " age: " + str(
            spy_age) + " rating: " + str(spy_rating)
    elif spy_rating >= 2.5 and spy_rating <= 4.5:
        print"You're the one"
        spy_online = True
        print "Authentication Complete..Welcome " + spy_salutation + " " + spy_name + " age: " + str(
            spy_age) + " rating: " + str(spy_rating)
    else:
        print"Sorry"
else:
    print("Wrong choice")
def add_friend():
    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = raw_input("Age?")
    new_age = int(new_age)

    new_rating = raw_input("Spy rating?")
    new_rating = float(new_rating)

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)



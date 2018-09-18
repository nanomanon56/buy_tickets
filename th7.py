import sys
Ticket_price = 10

tickets_remaining = 100
SERVICE_CHARGE = 2
def calculate_price(number_of_tickets):
    return number_of_tickets * Ticket_price
# output how many ticets are remaing using the ticekts remaing va
while tickets_remaining > 0:
#run the code until we are out of tickets
    print("Hello would you like a ticket?")
    print("there are {} tickets_remaining".format(tickets_remaining))

    name = raw_input('What is your name? ')

    ticket_number = raw_input('{} How many tickets would you like? '.format(name))
    try:
        ticket_number = int(ticket_number)
        if ticket_number > tickets_remaining:
            raise ValueError('There are only {} tickets remaining'.format(tickets_remaining))
    except ValueError as err:
        print('Oh no we have an issue, please try again'.format(err))
    else:
        total = calculate_price(ticket_number)
        total += SERVICE_CHARGE
        print('your total price is ${}'.format(total))

        # i am confiming my order to confim how many
        purchase = raw_input(" do you want to continue your order? (y/n) ")
        if purchase.lower() == 'y' :
        #If they want to confim,
        #get credit card number and process
            print('SOLD!!')
            print('you have ordered {} tickets'.format(ticket_number))
            tickets_remaining -= ticket_number
        #if sold, show how many tickets are left by tickets puchesed
        else:
            print('Thank you for your time {}!'.format(name))
            break

else:
    print('Thank you so much but we are all out of tickets :(')
#notig=fy the user that the tickets are sold out

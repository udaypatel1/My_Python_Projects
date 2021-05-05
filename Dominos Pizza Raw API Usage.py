## Dominos API raw code == no GUI application

import pizzapi as pp

customer = pp.Customer('FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER',
                    'SAME AS pp.Address BUT IN ONE STRING')
address = pp.Address('ADDRESS','STATE_FULL','STATE_INITIALS','ZIP_CODE')

store = address.closest_store()
menu = store.get_menu()
menu.search(Name='Cheesy')

order = pp.Order(store, customer, address)
order.add_item('12SCDELUX') # hand tossed medium duluxe pizza $15.99
order.add_item('B8PCSCB') # stuffed cheesy bread $6.99

card = pp.PaymentObject('CARD NUMBER','DATE OF EXP','SEC NUMBER','ZIPCODE')
order.pay_with(card) # will not actually order the items

### The following command in asterisks ***order.place(card)*** will complete the transaction and start the order at your nearest dominos


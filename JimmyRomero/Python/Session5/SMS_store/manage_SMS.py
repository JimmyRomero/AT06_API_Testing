from Python.Session5.SMS_store.SMS_store import SMSStore

my_inbox = SMSStore()

my_inbox.add_new_arrival("70731014", "2018-06-23", "SMS text 1")
my_inbox.add_new_arrival("70731011", "2018-06-30", "SMS text 2")
my_inbox.add_new_arrival("70731015", "2018-07-02", "SMS text 3")
my_inbox.add_new_arrival("70731017", "2018-07-02", "SMS text 4")

print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(1))
print(my_inbox.get_unread_indexes())
my_inbox.delete(0)
print(my_inbox.get_unread_indexes())
my_inbox.clear()
print(my_inbox.get_unread_indexes())

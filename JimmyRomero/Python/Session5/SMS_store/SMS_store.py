class SMSStore:

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        has_been_viewed = False
        self.inbox.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return int(len(self.inbox))

    def get_unread_indexes(self):
        unread_indexes = []
        for i in self.inbox:
            if not i[0]:
                unread_indexes.append(i)
        return unread_indexes

    def get_message(self, i):
        if i < self.message_count():
            sms = self.inbox[i]
            sms = (True,) + sms[1:]
            self.inbox[i] = sms
            return self.inbox[i][1:]
        return "None"

    def delete(self, i):
        self.inbox.pop(i)

    def clear(self):
        self.inbox.clear()

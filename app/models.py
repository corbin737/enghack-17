from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(64), index=True)
    message = db.Column(db.Text())
    delivered = db.Column(db.Boolean(), index=True, default=False)

    def __repr__(self):
        return 'Message to ' + self.recipient + ': ' + self.message[:10]

class Broadcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text())

    def __repr__(self):
        return self.message

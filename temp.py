from app import db
db.create_all()
from app import Item
item1 = Item(name="IPhone 10", price=500, barcode="123456789123", description="a phone")
item2 = Item(name="Laptop", price=600, barcode="123456789125", description="a laptop")
db.session.add(item1)
db.session.commit()
Item.query.all()
db.session.add(item2)
Item.query.all()
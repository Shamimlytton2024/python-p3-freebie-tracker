# #!/usr/bin/env python3

# from sqlalchemy import create_engine

# from models import Company, Dev

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///freebies.db')
#     import ipdb; ipdb.set_trace()

# debug.py
from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Test retrieving a dev and viewing their companies
dev = session.query(Dev).filter_by(name='Dev 1').first()
print(dev.companies)

# Test giving a freebie
company = session.query(Company).filter_by(name='Company A').first()
new_freebie = company.give_freebie(dev, 'Sticker', 5)
session.add(new_freebie)
session.commit()

# Test printing freebie details
print(new_freebie.print_details())

# Test oldest company
oldest = Company.oldest_company()
print(oldest)

# Test received_one method
print(dev.received_one('Laptop'))

# Test give_away method
dev2 = session.query(Dev).filter_by(name='Dev 2').first()
dev.give_away(dev2, new_freebie)
session.commit()
print(new_freebie.dev.name)
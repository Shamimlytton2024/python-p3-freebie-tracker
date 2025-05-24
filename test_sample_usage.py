from lib.models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup in-memory SQLite database for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create sample companies
company1 = Company(name="TechCorp", founding_year=1990)
company2 = Company(name="InnovateLLC", founding_year=1985)
session.add_all([company1, company2])
session.commit()

# Create sample devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
session.add_all([dev1, dev2])
session.commit()

# Company gives freebies to devs
freebie1 = company1.give_freebie(dev1, "Sticker", 5)
freebie2 = company1.give_freebie(dev2, "T-Shirt", 20)
freebie3 = company2.give_freebie(dev1, "Mug", 10)

session.add_all([freebie1, freebie2, freebie3])
session.commit()

# Test Freebie.print_details()
print(freebie1.print_details())  # Alice owns a Sticker from TechCorp
print(freebie2.print_details())  # Bob owns a T-Shirt from TechCorp
print(freebie3.print_details())  # Alice owns a Mug from InnovateLLC

# Test Company.oldest_company()
oldest = Company.oldest_company(session)
print(f"Oldest company: {oldest.name}")  # InnovateLLC

# Test Dev.received_one()
print(dev1.received_one("Sticker"))  # True
print(dev2.received_one("Mug"))      # False

# Test Dev.give_away()
print(f"Before give_away: {freebie1.dev.name}")  # Alice
dev1.give_away(dev2, freebie1)
session.commit()
print(f"After give_away: {freebie1.dev.name}")   # Bob

# Test relationships
print(f"Company1 freebies: {[f.item_name for f in company1.freebies]}")  # ['Sticker', 'T-Shirt']
print(f"Dev1 companies: {[c.name for c in dev1.companies]}")              # ['TechCorp', 'InnovateLLC']
print(f"Company1 devs: {[d.name for d in company1.devs]}")                # ['Alice', 'Bob']

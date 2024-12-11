import random
import pandas as pd
from faker import Faker

fake = Faker()

rows = [13,83,9,171,8,5,250,175,40,69,240,36,None,110,256,2,241,142,115,314,243,147,71,1,10,89,7,15,28,12,20,3,6,4,14,74,11]

#images
def generate_photo():
    gender = random.choice(['men', 'women'])
    image_id = random.randint(1,100)
    return f"https://randomuser.me/api/portraits/{gender}/{image_id}.jpg"

#phone numbers
def generate_phone_no():
    return f"+91{random.randint(50000000,99999999)}"

data = []
for i in rows:
    name = fake.name()
    phone = generate_phone_no()
    image = generate_photo()
    data.append([i, name, phone, image])

df = pd.DataFrame(data, columns=['Owner ID', 'Owner Name', 'Owner Phone', 'Owner Image'])

df.to_csv('owner.csv', index=False)
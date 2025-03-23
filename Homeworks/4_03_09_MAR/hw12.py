# Ստեղծել ծրագիր, որը կներառի օգտատերերի տվյալների ներմուծումը, պահպանումը բառարանում և ցուցակում,
# ապա ցույց կտա օգտատերերին ըստ ներմուծված անվան(“Not found”, եթե այդպիսի օգտատեր գոյություն չունի)։
# Յուրաքանչյուր օգտատեր պետք է ունենա հետևյալ դաշտերը՝ ID, անուն, ազգանուն, Էլ. փոստ, գաղտնաբառ և հեռախոսահամար:

data_ls = ("ID", "Name", "Surname", "e-mail", "password", "phone-number")
people_ls = []
data_dict = {}
count = 0

while count < 3:
  for i in data_ls:
    di[i] = input(f"Enter {count + 1} {i} data: ")
  people_ls.append(di)
  di = {}
  count += 1

target = input("Enter name you want to find: ")
for item in people_ls:
  if item["Name"] == target:
    print(item)
    break
  else:
    print("Not found")
    break
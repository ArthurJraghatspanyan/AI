import os

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ]

def setup_month(month: str) -> None:
  global months
  try:
    if month not in months:
      print(f"Error while setting up a month: Month {month} doesn't exist.")
    else:
      os.makedirs(month)
  except FileExistsError:
    print(f"Error while setting up a month: Month {month} already exists. Choose another month.")

def add_note(month: str, day: int, note: str) -> None:
  global months
  try:
    if month not in months:
      print(f"Error while setting up a month: Month {month} doesn't exist.")
    elif not 1 <= day <= 30:
      print(f"Error while adding a note: Day {day} of month doesn't exist.")
    else:
      fd = open(f"{month}/{str(day)}.txt", mode='x')
      fd.write(note)
      print(f"Note of the day: {day} successfully added")
  except FileNotFoundError:
    print(f"Error while adding a note: Month or day doesn't exist.")
  except FileExistsError:
    print(f"Error while adding a note: Note on day {day} already exists.")

def read_note(month: str, day: int) -> str:
  global months
  try:
    if month not in months:
      print(f"Error while setting up a month: Month {month} doesn't exist.")
    elif not 1 <= day <= 30:
      print(f"Error while reading the note of day: {day}: Day of month doesn't exist.")
    else:
      fd = open(f"{month}/{str(day)}.txt", mode='r')
      note = fd.read()
      return f"Note of day {day} is: {note}"
  except FileNotFoundError:
    print("Error while reading the note: File doesn't exist. Please create it.")

def list_notes(month: str) -> dict[str, str]:
  global months
  try:
    if month not in months:
      print(f"Error while setting up a month: Month {month} doesn't exist.")
    di = {}
    ls = os.listdir(f"{month}")
    ls.sort(key=lambda x: int(x.split('.')[0]))
    for day in ls:
      fd = open(f"{month}/{day}", mode='r')
      day = day.removesuffix('.txt')
      di[f"Day {day}"] = fd.read()
    return di
  except FileNotFoundError:
    print("Error while listing notes: File or folder doesn't exist. Please create it.")

def delete_note(month: str, day: int) -> None:
  global months
  try:
    if month not in months:
      print(f"Error while setting up a month: Month {month} doesn't exist.")
    if not 1 <= day <= 30:
      print(f"Error while deleting the note of day: {day}: Day of month doesn't exist.")
    else:
      os.remove(f"{month}/{str(day)}.txt")
      print(f"Note of the day: {day} successfully deleted")
  except FileNotFoundError:
    print("Error while deleting file: File doesn't exist.")
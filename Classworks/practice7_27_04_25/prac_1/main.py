import calendar_manager

if __name__ == '__main__':
  calendar_manager.setup_month("March")

  calendar_manager.add_note("March", 5, "Doctor appointment at 10 AM")
  calendar_manager.add_note("March", 12, "Meeting with the team")

  print(calendar_manager.read_note("March", 5))
  print(calendar_manager.read_note("March", 12))

  print(calendar_manager.list_notes("March"))

  calendar_manager.delete_note("March", 12)
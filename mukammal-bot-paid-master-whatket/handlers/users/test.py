from loader import dp, db, bot


users = db.select_all_users()
print(type(users))
print(users)


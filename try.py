def get_user_email(users, user_id):
    user = users.get(user_id)
    return user.email  # will crash if user_id isn't in users — no None check

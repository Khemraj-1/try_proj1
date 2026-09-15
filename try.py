def get_user_email(users: dict, user_id: str) -> str | None:
    """Return the email for a given user_id, or None if not found."""
    if not users:
        return None

    user = users.get(user_id)
    if user is None:
        return None

    return getattr(user, "email", None)

def is_valid_account_number(account_name):
    """
    Checks if the given account number is valid
    """

    if len(str(account_name)) != 64:
        return False

    try:
        bytes.fromhex(account_name)
    except Exception:
        return False

    return True

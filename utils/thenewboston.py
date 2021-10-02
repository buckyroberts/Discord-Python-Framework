def is_valid_account_number(account_number):
    """
    Checks if the given account number is valid
    """

    if len(str(account_number)) != 64:
        return False

    try:
        bytes.fromhex(account_number)
    except Exception:
        return False

    return True

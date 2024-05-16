def user_role():
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (VENDOR, "Vendor"),
        (CUSTOMER, "Customer"),
    )
    return ROLE_CHOICES
from enum import Enum

class UserRole(str, Enum):
    DEVELOPER = "developer"
    COMPANY = "company"
    ADMIN = "admin"
from enum import Enum

class UserRole(str, Enum):
    DEVELOPER = "developer"
    COMPANY = "company"
    ADMIN = "admin"

class EmploymentType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    INTERNSHIP = "internship"
    CONTRACT = "contract"
    REMOTE = "remote"
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"
    TECHNICIAN = "TECHNICIAN"

class DiscountType(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"
    OFF_PEAK = "off_peak"

class CartStatus(str, Enum):
    ACTIVE = "active"
    CHECKED_OUT = "checked_out"
    ABANDONED = "abandoned"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class ServiceType(str, Enum):
    AC_REPAIR = "ac_repair"
    TV_REPAIR = "tv_repair"
    OVEN_REPAIR = "oven_repair"
    IPS_REPAIR = "ips_repair"
    HOME_CLEANING = "home_cleaning"
    REFRIGERATOR_REPAIR = "refrigerator_repair"
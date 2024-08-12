from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class Person2:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
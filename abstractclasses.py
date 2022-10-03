from abc import ABC, abstractmethod
from collections import UserDict


class AbstractFields(ABC):
    @abstractmethod
    def __init__(self, value):
        pass

    @abstractmethod
    @property
    def value(self):
        pass

    @abstractmethod
    @value.setter
    def value(self, value):
        pass


class AbstractNotebook(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def make_note(self) -> str:
        pass

    @abstractmethod
    def change_note(self, *args: str) -> str:
        pass


class AbstractAddressBook(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def add_contact(self):
        pass

    @abstractmethod
    def change_contact(self, *args: str) -> str:
        pass

    @abstractmethod
    def check_birthdays(self, period: str) -> str:
        pass


class AbstractRecordContainer(UserDict, ABC):
    @abstractmethod
    def load_data(cls, filepath: str) -> None | dict:
        pass

    @abstractmethod
    def backup_data(handler) -> None:
        pass

    @abstractmethod
    def add_record(self, record) -> None:
        pass

    @abstractmethod
    def remove_record(self, *args: str) -> str:
        pass

    @abstractmethod
    def record_exists(self, record_name: str) -> bool:
        pass

    @abstractmethod
    def show_records(self) -> str:
        pass

    @abstractmethod
    def search_records(self, needle: str) -> str:
        pass


class AbstractNoteRecord(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def change_title(self, new_title: str):
        pass

    @abstractmethod
    def change_tags(self, *args: str):
        pass

    @abstractmethod
    def change_text(self, new_text: str):
        pass


class AbstractAddressBookRecord(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_phone(self, phone: str):
        pass

    @abstractmethod
    def count_days_to_birthday(self) -> str:
        pass

    @abstractmethod
    def add_birthday(self, birthday: str) -> None:
        pass

    @abstractmethod
    def add_email(self, email: str) -> None:
        pass

    @abstractmethod
    def add_address(self, *args: str) -> None:
        pass


if __name__ == '__main__':
    pass

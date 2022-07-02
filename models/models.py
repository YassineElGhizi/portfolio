from typing import List


class Me:
    first_name: str
    last_name: str
    description: str
    profession: str
    birthday: str
    email: str
    city: str
    country: str
    language: List[str]
    freelance: bool

    def __init__(self, first_name: str, last_name: str, description: str, profession: str, phone: str,
                 email: str, city: str, country: str, language: List[str], freelance) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.profession = profession
        self.phone = phone
        self.email = email
        self.city = city
        self.country = country
        self.language = language
        self.freelance = freelance

    @property
    def full_addr(self) -> str:
        return f'{self.city} {self.country}'

    @property
    def langs(self) -> str:
        return ",".join(self.language)

    @property
    def freelance_avaible(self) -> str:
        if self.freelance:
            return 'Available'
        else:
            return 'Not Available'
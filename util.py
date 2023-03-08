from dataclasses import dataclass

@dataclass
class Article:
    url: str
    year: str

@dataclass
class TopViews:
    month: str
    year: str
    numarticles: int

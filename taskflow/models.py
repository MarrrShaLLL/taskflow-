class Task:
    def __init__(self, title, done=False):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Վերնագիրը պետք է լինի ոչ դատարկ տող։")
        if not isinstance(done, bool):
            raise ValueError("Վիճակը պետք է լինի bool։")
        self.title = title.strip()
        self.done = done

    def complete(self):
        self.done = True

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise ValueError("Առաջադրանքը պետք է լինի dictionary։")
        if "title" not in data or "done" not in data:
            raise ValueError("Առաջադրանքի դաշտերը բացակայում են։")
        return cls(data["title"], data["done"])

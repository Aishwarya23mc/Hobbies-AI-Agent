from personas import personas


def get_linkedin(name):
    person = personas.get(name.lower())
    if person:
        return person.get("linkedin", "")
    return ""


def get_instagram(name):
    person = personas.get(name.lower())
    if person:
        return person.get("instagram", "")
    return ""


def get_resume(name):
    person = personas.get(name.lower())
    if person:
        return person.get("resume", "")
    return ""
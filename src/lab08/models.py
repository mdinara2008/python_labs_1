from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def make_student(fio, birthdate, group, gpa):
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError("fio must be a non-empty string")
    if not isinstance(group, str) or not group.strip():
        raise ValueError("group must be a non-empty string")

    if not isinstance(birthdate, str) or len(birthdate)!=10:
        raise ValueError("birthdate must be in YYYY-MM-DD format")
    b_date = date.fromisoformat(birthdate)
    if b_date > date.today():
        raise ValueError("birthdate cannot be in the future")

    if not isinstance(gpa, (int, float)) or isinstance(gpa, bool):
        raise ValueError("gpa must be a number")
    if not (0 <= gpa <= 5):
        raise ValueError("gpa must be between 0 and 5")

    return {"fio": fio, "birthdate": birthdate, "group": group, "gpa": float(gpa)}


def validate_student(rec):
    if not isinstance(rec, dict) or set(rec) != set(STUDENT_FIELDS):
        raise ValueError("invalid keys or not a dict")
    
    if not isinstance(rec["fio"], str) or not rec["fio"].strip():
        raise ValueError("fio must be a non-empty string")
    if not isinstance(rec["group"], str) or not rec["group"].strip():
        raise ValueError("group must be a non-empty string")

    if not isinstance(rec["birthdate"], str) or len(rec["birthdate"])!=10:
        raise ValueError("birthdate must be in YYYY-MM-DD format")
    b_str = date.fromisoformat(rec["birthdate"])
    if b_str > date.today():
        raise ValueError("birthdate cannot be in the future")

    if not isinstance(rec["gpa"], (int, float)) or isinstance(rec["gpa"], bool):
            raise ValueError("gpa must be a number")
    if not (0 <= rec["gpa"] <= 5):
        raise ValueError("gpa must be between 0 and 5")
    

def student_age(rec, today=None):
    validate_student(rec)
    b = date.fromisoformat(rec["birthdate"])
    if today is None: 
        today = date.today()
    elif isinstance(today, str):
      if len(today) != 10:
        raise ValueError("today must be in YYYY-MM-DD format")
      today = date.fromisoformat(today)
    elif not isinstance(today, date):
      raise ValueError("today must be a date or YYYY-MM-DD string")

    return today.year - b.year - ((today.month, today.day) < (b.month, b.day))


def student_to_dict(rec):
    validate_student(rec)
    return {
        "fio": rec["fio"],
        "birthdate": rec["birthdate"],
        "group": rec["group"],
        "gpa": float(rec["gpa"])
    }


def student_from_dict(d):
    if not isinstance(d, dict) or set(d) != set(STUDENT_FIELDS):
        raise ValueError("not a dict or invalid keys")
    return make_student(d["fio"], d["birthdate"], d["group"], d["gpa"])


def format_student(rec):
    validate_student(rec)

    parts = rec["fio"].split()
    short_fio = f"{parts[0]} {''.join(p[0].upper() + '.' for p in parts[1:])}".strip()

    age = student_age(rec)
    if 11 <= age%100 <= 14: word = "лет"
    elif age%10==1: word = "год"
    elif 2 <= age%10 <= 4: word = "года"
    else: word = "лет"

    return f"{short_fio} ({rec['group'].strip()}), {age} {word}, GPA {rec['gpa']:.2f}"
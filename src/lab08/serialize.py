import json
from pathlib import Path
from src.lab08.models import student_from_dict, student_to_dict

def students_to_json(students, path):
    data = [student_to_dict(s) for s in students]
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with Path(path).open("r", encoding="utf-8") as f:
        raw = json.load(f)

    if not isinstance(raw, list):
        raise ValueError("JSON должен содержать массив объектов")

    result = []
    for i, item in enumerate(raw, start=1):
        try:
            result.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError(f"Ошибка в записи #{i}: {e}")
    return result


if __name__ == "__main__":
  import sys
  from src.lab08.models import format_student

  if len(sys.argv)>1: cmd = sys.argv[1]
  else: cmd = "ok"

  if cmd == "ok":
    students = students_from_json("data/lab08/students_input.json")
    for s in students:
        print(format_student(s))
    students_to_json(students, "data/lab08/students_output.json")
  elif cmd=="bad":
    students_from_json("data/lab08/students_bad.json")

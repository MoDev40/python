ca2112_class = (
    {
        "name": "Alia",
        "id": "S101",
        "subjects": {"math": 78, "science": 85, "english": 92},
    },
    {
        "name": "Bilal",
        "id": "S102",
        "subjects": {"math": 88, "science": 79, "english": 90},
    },
    {
        "name": "Celine",
        "id": "S103",
        "subjects": {"math": 95, "science": 92, "english": 89},
    },
    {
        "name": "Dawid",
        "id": "S104",
        "subjects": {"math": 67, "science": 73, "english": 80},
    },
    {
        "name": "Elina",
        "id": "S105",
        "subjects": {"math": 82, "science": 88, "english": 84},
    },
)


def calculate_gradebook(class_data: tuple) -> dict:
    student_stats = dict()
    for students in class_data:
        if len(students) > 0:
            subjects = students.get("subjects")
            st_id = students.get("id")
            scores = list(subjects.values())
            student_stats.update(
                {
                    st_id: {
                        "scores": scores,
                        "lowest": min(scores),
                        "highest": max(scores),
                        "sum": sum(scores),
                        "average": round(sum(scores) / len(subjects), 2),
                    }
                }
            )
        else:
            print("This class doesn't have any students")

    class_stats = {
        "students": len(student_stats),
        "averages": [],
        "scores": [],
        "sum": 0,
        "average": 0.0,
    }

    for stats in student_stats.values():
        class_stats["sum"] += stats["sum"]
        class_stats["averages"].append(stats["average"])
        class_stats["scores"].extend(stats["scores"])

    class_stats["lowest"] = min(class_stats["scores"])
    class_stats["highest"] = max(class_stats["scores"])
    class_stats["average"] = round(
        sum(class_stats["scores"]) / len(class_stats["scores"]), 2
    )

    return {"students": student_stats, "class": class_stats}


print(calculate_gradebook(class_data=ca2112_class))

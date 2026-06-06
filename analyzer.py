print("===== AI Resume Skill Gap Analyzer ===== ")

with open("required_skills.txt", "r") as file:
    required_skills = file.read().splitlines()

user_input = input("\nEnter your skills (comma separated): ")

user_skills = [skill.strip() for skill in user_input.split(",")]

matched_skills = []
missing_skills = []

for skill in required_skills:

    if skill.lower() in [s.lower() for s in user_skills]:
        matched_skills.append(skill)

    else:
        missing_skills.append(skill)

match_percentage = (len(matched_skills) / len(required_skills)) * 100

if match_percentage >= 80:
    level = "Job Ready 🚀"

elif match_percentage >= 50:
    level = "Learning Stage 📚"

else:
    level = "Beginner 🌱"

print("\n===== ANALYSIS REPORT =====")

print("\nMatched Skills:")
for skill in matched_skills:
    print("✓", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✗", skill)

print(f"\nMatch Percentage: {match_percentage:.0f}%")

print(f"\nLevel: {level}")

with open("report.txt", "w", encoding="utf-8") as report:

    report.write("===== AI Resume Skill Gap Analysis =====\n\n")

    report.write("Matched Skills:\n")
    for skill in matched_skills:
        report.write(f"[FOUND] {skill}\n")

    report.write("\nMissing Skills:\n")
    for skill in missing_skills:
        report.write(f"[MISSING] {skill}\n")

    report.write(f"\nMatch Percentage: {match_percentage:.0f}%\n")
    report.write(f"Level: {level}\n")

print("\nReport saved successfully in report.txt")
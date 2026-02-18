# Languages good for Web Development
languages_web = {
    "JavaScript",
    "TypeScript",
    "Python",
    "PHP",
    "Ruby",
    "Go",
    "Java",
    "C#"
}
# Languages good for Data Science/Machine Learning
languages_data_science = {
    "Python",
    "R",
    "Julia",
    "Scala",
    "MATLAB",
    "Java",
    "SQL"
}
# Languages good for System Programming
languages_systems = {
    "C",
    "C++",
    "Rust",
    "Go",
    "Zig",
    "Assembly"
}
# Languages good for Mobile Development
languages_mobile = {
    "Swift",
    "Kotlin",
    "Java",
    "Dart",
    "JavaScript",
    "C#"
}
print("\n🌐 Languages for Web Development: ")
print(sorted(languages_web))
print("\n📊 Languages for Data Science:")
print(sorted(languages_data_science))
print("\n⚙️  Languages for System Programming:")
print(sorted(languages_systems))
print("\n📱 Languages for Mobile Development:")
print(sorted(languages_mobile))


print(f"\n❓ Which languages are good for BOTH Web AND Data Science?{languages_web & languages_data_science}")

print(f"\n❓ Languages that can do Web, Mobile, OR Data Science?{languages_mobile | languages_data_science | languages_mobile}")

print(f"\n❓ Languages ONLY for System Programming (not web/mobile/data)?{languages_systems - languages_data_science - languages_mobile - languages_web}")

print(f"\n❓ Which languages work for Web but NOT Mobile?{languages_web - languages_mobile}")

print(f"\n❓ Is 'Python' in the web development set?{"Python" in languages_web}")

print(f"\n❓ The ultimate polyglot language (in ALL four categories)?{languages_web & languages_data_science & languages_mobile & languages_systems}")

modern_web = {"JavaScript", "TypeScript", "Python"}
print(f"\n❓ Is modern_web a PROPER subset of web languages (PROPER = smaller, not equal)?{modern_web < languages_web}")

from pyscript import display, document
grade_7 = {"Ladis", "Washerum", "Allison"}
grade_8 = {"Burgers", "Emplois", "Muswushhans"}
grade_9 = {"Max", "Imum", "Occupanci 120"}
grade_10 = {"Romanes", "eunt", "domus"}
initial_members = grade_7 | grade_8 | grade_9 | grade_10
initial_list = "<br>".join(sorted(initial_members))
document.getElementById("output-content").innerHTML = f"<h1>All members:</h1>{initial_list}<br><h2>Total members:</h2> {len(initial_members)}"
def add_member(event):
    fname = document.getElementById("first-name").value
    lname = document.getElementById("last-name").value
    new_member = {fname + " " + lname}
    all_members = initial_members | new_member
    member_list = "<br>".join(sorted(all_members))
    document.getElementById("output-content").innerHTML = f"<h1>All members:</h1>{member_list}<br><h2>Total members:</h2> {len(all_members)}"
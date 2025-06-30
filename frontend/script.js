const form = document.getElementById("studentForm");
const list = document.getElementById("studentList");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;

    await fetch("/api/students", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
    });

    loadStudents();
    form.reset();
});

async function loadStudents() {
    const res = await fetch("/api/students");
    const students = await res.json();

    list.innerHTML = "";
    students.forEach((s) => {
        const li = document.createElement("li");
        li.textContent = s.name;
        list.appendChild(li);
    });
}

loadStudents();

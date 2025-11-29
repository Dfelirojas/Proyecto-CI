const tableroDiv = document.getElementById("tablero");
const puntajeP = document.getElementById("puntaje");

async function cargarTablero() {
    const res = await fetch("/api/tablero");
    const data = await res.json();
    tableroDiv.innerHTML = "";

    data.forEach((fila, i) => {
        const filaDiv = document.createElement("div");
        filaDiv.className = "fila";

        fila.forEach((celda, j) => {
            const btn = document.createElement("button");
            btn.innerText = celda.pintado ? "✔" : "❓";
            btn.onclick = () => responder(i, j);
            filaDiv.appendChild(btn);
        });

        tableroDiv.appendChild(filaDiv);
    });
}

async function responder(i, j) {
    const respuesta = prompt("Resuelve la operación:");
    if (!respuesta) return;

    const res = await fetch("/api/responder", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ i, j, respuesta })
    });

    const data = await res.json();
    alert(`Operación: ${data.operacion}\n${data.correcta ? "✅ Correcto!" : "❌ Incorrecto!"}`);
    puntajeP.innerText = `Puntaje: ${data.puntaje}`;
    cargarTablero();
}

cargarTablero();

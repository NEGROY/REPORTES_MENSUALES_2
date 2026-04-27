function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
    return "";
}

async function buscarDatos_api() {
    console.clear();

    const tk = (document.getElementById("falla")?.value || "").trim();
    const areaSlct = (document.getElementById("areaSlct")?.value || "").trim();
    const tbCalcu = document.getElementById("TB_calcu");

    if (!tk) {
        console.warn("⚠️ No se ingresó falla");
        tbCalcu.innerHTML = `
            <div class="alert alert-warning mb-0">
                Debe ingresar una falla/ticket.
            </div>
        `;
        return;
    }

    if (!areaSlct) {
        console.warn("⚠️ No se seleccionó área");
        tbCalcu.innerHTML = `
            <div class="alert alert-warning mb-0">
                Debe seleccionar un área de escalación.
            </div>
        `;
        return;
    }

    tbCalcu.innerHTML = `
        <div class="text-center py-4 text-muted">
            <div class="spinner-border spinner-border-sm me-2" role="status"></div>
            Generando tabla de escalación...
        </div>
    `;

    try {
        const url = `/api/masivas/${encodeURIComponent(tk)}/`;
        const resp = await fetch(url, {
            method: "GET",
            headers: { "Accept": "application/json" }
        });

        const payload = await resp.json();

        if (!resp.ok || payload?.ok === false) {
            console.error("❌ Error backend:", payload);
            tbCalcu.innerHTML = `
                <div class="alert alert-danger mb-0">
                    No fue posible consultar la falla ingresada.
                </div>
            `;
            return;
        }

        const rows = getData(payload);
        const row = rows?.[0] || {};

        const body = {
            hrActual: row.hrActual || new Date().toISOString().slice(0, 19).replace("T", " "),
            tmpAcumu: row.tmpAcumu || "",
            areaSlct: parseInt(areaSlct, 10),
            fallaID: row.fallaID || tk,
            titulo: row.titulo || "",
            dashboard: row.dashboard || "",
            txtarea: row.txtarea || "",
            nivel: parseInt(row.nivel || 0, 10),
            falla_dire: row.falla_dire || "",
            company: row.company || ""
        };

        const htmlResp = await fetch("/api/tabla-html/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "text/html",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify(body)
        });

        const html = await htmlResp.text();

        if (!htmlResp.ok) {
            console.error("❌ Error generando tabla html");
            tbCalcu.innerHTML = html;
            return;
        }

        tbCalcu.innerHTML = html;

    } catch (error) {
        console.error("❌ Error general:", error);
        tbCalcu.innerHTML = `
            <div class="alert alert-danger mb-0">
                Ocurrió un error al generar la tabla.
            </div>
        `;
    }
}

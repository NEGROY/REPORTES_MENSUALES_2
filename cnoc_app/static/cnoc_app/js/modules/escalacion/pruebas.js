// cnoc_app/js/modules/escalacion/escalacion.js
function setValue(id, value) {
  const el = document.getElementById(id);
  if (!el) return;
  el.value = (value === null || value === undefined) ? "" : String(value);
}

function setText(id, value) {
  const el = document.getElementById(id);
  if (!el) return;
  el.innerText = (value === null || value === undefined) ? "-" : String(value);
}

// Devuelve data[0] si existe, si no devuelve un objeto vacío
function getRow(payload) {
  if (!payload) return {};
  const data = payload.data;
  if (Array.isArray(data) && data.length > 0) return data[0];
  if (typeof data === "object" && data !== null) return data;
  return {};
}

// Helpers: obtén primer valor existente de una lista de candidatos
function pick(row, candidates) {
  for (const c of candidates) {
    let v;
    if (typeof c === "function") v = c(row);
    else v = row?.[c];
    if (v !== undefined && v !== null && String(v).trim() !== "") return v;
  }
  return "";
}

function fillFromMasivasDetail(payload) {
  const row = getRow(payload);

  // 🔥 Mapeo basado en tu JSON real
  // Respuesta 1 (externa) trae: OPEN_TIME, CLOSE_TIME, TITULO, COMPANY, HH_MM_SS, TIEMPO_VIDA_TK, etc.
  // Respuesta 2 (tu /api/masivas/<tk>/) trae: F_UPDATE, SYSDATE, "GRUPO ASIGNADO", VARIABLE3, UPDATE_ACTION, etc.

  // Inputs superiores
  setValue("cierre", pick(row, ["CLOSE_TIME", "cierre", "close_time"]));

  // "Dirección": no viene explícita como "direccion", así que usamos fallback:
  // 1) TITULO (trae ubicación)  // 2) FALLA   // 3) UPDATE_ACTION (si no hay título)
  setValue("falla_direccion", pick(row, ["TITULO", "FALLA", "falla", "UPDATE_ACTION"]));

  // Inputs panel principal
  setValue("open_time", pick(row, ["OPEN_TIME", "open_time", "F_UPDATE"]));
  setValue("current_time", pick(row, ["SYSDATE", "SYSMODTIME"]));

  // “Tiempo acumulado”: preferimos formato ya preparado
  setValue("elapsed_time", pick(row, [ "HH_MM_SS", "TIEMPO_VIDA_TK", "SIN_ACTUALIZAR_TK_TXT", "TIEMPO_SIN_SEGUIMIENTO_F"  ]));

  // “Nivel”: si no existe nivel, tomamos el grupo asignado / assignment
  setValue("nivel", pick(row, [
    "ASSIGNMENT",
    (r) => r["GRUPO ASIGNADO"],  // clave con espacio
    "GRUPO_ASIGNADO",
    "grupo_asignado"
  ]));

  // hidden (company)
  setValue("company", pick(row, ["COMPANY", "company"]));

  // Títulos UI
  setText("titulo", pick(row, ["TITULO", "FALLA", "TG_ENLACE"]));

  const tituloPrincipal = document.getElementById("titulo_principal");
  if (tituloPrincipal) {
    const v = pick(row, ["TITULO", "FALLA"]);
    tituloPrincipal.hidden = !v;
    tituloPrincipal.innerText = v || "-";
  }

  // Si quieres mostrar algo en resultado:
  const res = document.getElementById("resultado");
  if (res) {
    res.innerHTML = ""; // limpia
  }

  // Si quieres debug en TB_calcu:
  const div = document.getElementById("TB_calcu");
  if (div) {
    div.innerHTML = `<pre style="margin:0">${JSON.stringify(payload, null, 2)}</pre>`;
  }
}

async function buscarDatos_api() {
  // Usa tus helpers existentes si existen en layout/base
  if (typeof limpiarTextAreas === "function") limpiarTextAreas();
  if (typeof toggleLoader === "function") toggleLoader(1);

  const tk = (document.getElementById("falla")?.value || "").trim();
  if (!tk) {
    if (typeof toggleLoader === "function") toggleLoader(0);
    return;
  }

  const url = `/api/masivas/${encodeURIComponent(tk)}/`;

  try {
    const resp = await fetch(url, {
      method: "GET",
      headers: { "Accept": "application/json" }
    });

    const payload = await resp.json().catch(() => ({}));

    if (!resp.ok || payload?.ok === false) {
      const msg = payload?.message || "Error consultando MASIVAS";
      const res = document.getElementById("resultado");
      if (res) res.innerHTML = `<div class="alert alert-danger">${msg}</div>`;
      return;
    }

    // ✅ llenado de inputs
    fillFromMasivasDetail(payload);

  } catch (err) {
    const res = document.getElementById("resultado");
    if (res) res.innerHTML = `<div class="alert alert-danger">Error de red: ${String(err)}</div>`;
  } finally {
    if (typeof toggleLoader === "function") toggleLoader(0);
  }
}

// ✅ IMPORTANTE: exponer función global para que funcione onclick=""
window.buscarDatos_api = buscarDatos_api;
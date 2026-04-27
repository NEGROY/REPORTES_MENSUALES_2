/* **************************************************************************************************************************** */
/** 
 *  * Helper genérico para poblar <select> desde arrays de objetos.
 *  #UTILIZARE ESTA PARTE SI UTILIZO MAS ADELANTE EL SEELCT #
 * - Recursividad: soporta items con childrenKey para generar optgroups o nested options.
 */
function resolveSelect(selectOrId) {
  if (!selectOrId) return null;
  if (typeof selectOrId === "string") return document.getElementById(selectOrId);
  return selectOrId; // asume que ya es un HTMLSelectElement
}

// LIMIAPAA EL SELECT 
function clearSelect(selectEl) {
  while (selectEl.firstChild) selectEl.removeChild(selectEl.firstChild);
}

// CREA LAS OPCIONES DEL SELECT 
function createOption(value, text, { disabled = false } = {}) {
  const opt = document.createElement("option");
  opt.value = value ?? "";
  opt.textContent = text ?? "";
  opt.disabled = disabled;
  return opt;
}

/**
 * Recursivo: renderiza opciones y soporta children para optgroups.
 * Si un item tiene childrenKey (array), crea optgroup.
 */
function renderOptionsRecursive({
  parentEl,
  items,
  valueKey,
  textKey,
  childrenKey,
  transformer,
}) {
  items.forEach((item) => {
    const normalized = transformer ? transformer(item) : item;

    const children = childrenKey ? normalized?.[childrenKey] : null;

    // Si hay children -> optgroup
    if (Array.isArray(children) && children.length > 0) {
      const group = document.createElement("optgroup");
      group.label = normalized?.[textKey] ?? "Grupo";
      parentEl.appendChild(group);

      // Recursividad
      renderOptionsRecursive({
        parentEl: group,
        items: children,
        valueKey,
        textKey,
        childrenKey,
        transformer,
      });
      return;
    }

    // Option normal
    const value = normalized?.[valueKey];
    const text = normalized?.[textKey];
    parentEl.appendChild(createOption(value, text));
  });
}

/**
 * fillSelect: API pública del helper
 */
export function fillSelect({
  select,                 // string id o HTMLSelectElement
  items = [],             // array de objetos
  valueKey = "id",        // campo para option.value
  textKey = "nombre",     // campo para option.textContent
  placeholder = null,     // texto del primer option (ej: "---Seleccione---")
  placeholderValue = "",  // value del placeholder
  keepValue = true,       // mantener selección actual si existe en las nuevas opciones
  selectedValue = null,   // forzar una selección
  childrenKey = null,     // si usas jerarquía (recursivo)
  transformer = null,     // función que normaliza estructura (polimorfismo)
} = {}) {
  const selectEl = resolveSelect(select);
  if (!selectEl) return;

  const previous = selectEl.value;

  clearSelect(selectEl);

  if (placeholder !== null) {
    selectEl.appendChild(
      createOption(placeholderValue, placeholder, { disabled: false })
    );
  }

  renderOptionsRecursive({
    parentEl: selectEl,
    items,
    valueKey,
    textKey,
    childrenKey,
    transformer,
  });

  // Selección final
  if (selectedValue !== null && selectedValue !== undefined) {
    selectEl.value = String(selectedValue);
    return;
  }

  if (keepValue && previous) {
    // restaura si existe dentro de las opciones actuales
    const exists = Array.from(selectEl.options).some(o => o.value === previous);
    if (exists) selectEl.value = previous;
  }
}
/* **************************************************************************************************************************** */
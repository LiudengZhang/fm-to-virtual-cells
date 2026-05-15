// Tools matrix on the bioinfo-tools/tools/ index page.
// Different columns from the posters table → its own init.

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".tools-table").forEach(initToolsTable);
});

async function initToolsTable(container) {
  const src = container.dataset.src;
  if (!src) return;
  try {
    const resp = await fetch(src);
    if (!resp.ok) throw new Error(`Fetch failed: ${resp.status}`);
    const rows = await resp.json();
    new Tabulator(container, {
      data: rows,
      layout: "fitColumns",
      pagination: false,
      initialSort: [{ column: "n_posters", dir: "desc" }],
      columns: [
        {
          title: "Tool", field: "tool", widthGrow: 2,
          formatter: (cell) => {
            const r = cell.getRow().getData();
            return `<a href="${r.slug}/">${r.tool}</a>`;
          },
        },
        { title: "Family", field: "family", headerFilter: "list",
          headerFilterParams: { values: true, clearable: true } },
        { title: "Modality", field: "modality" },
        { title: "Released", field: "released", width: 100 },
        { title: "Posters", field: "n_posters", width: 100, sorter: "number" },
        { title: "Sessions", field: "n_sessions", width: 100, sorter: "number" },
        { title: "License", field: "license" },
        {
          title: "Also in", field: "also_in", widthGrow: 2,
          formatter: (cell) => (cell.getValue() || []).join(", "),
        },
      ],
    });
  } catch (e) {
    container.innerHTML = `<p><strong>Error loading tools matrix:</strong> ${e.message}</p>`;
  }
}

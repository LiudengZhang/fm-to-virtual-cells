// Poster table initialization.
// Each topic page includes a <div class="poster-table" data-src="<url>"></div>.
// We fetch the JSON, render a Tabulator table, and wire up filters.

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".poster-table").forEach(initPosterTable);
});

async function initPosterTable(container) {
  const src = container.dataset.src;
  if (!src) return;
  const statsEl = container.parentElement.querySelector(".poster-stats");
  try {
    const resp = await fetch(src);
    if (!resp.ok) throw new Error(`Fetch failed: ${resp.status}`);
    const data = await resp.json();
    const filtersHost = container.parentElement.querySelector(".poster-filters");
    renderTable(container, data, filtersHost, statsEl);
  } catch (e) {
    container.innerHTML = `<p><strong>Error loading posters:</strong> ${e.message}</p>`;
  }
}

function renderTable(container, rows, filtersHost, statsEl) {
  // Distinct values for filter dropdowns
  const sessions = [...new Set(rows.map(r => r.session))].sort();
  const activities = [...new Set(rows.map(r => r.activity))].sort();

  if (filtersHost) {
    filtersHost.innerHTML = `
      <input type="text" id="poster-search" placeholder="Search title/abstract/authors…" style="min-width:16rem;flex:1">
      <select id="poster-session">
        <option value="">All sessions</option>
        ${sessions.map(s => `<option value="${escapeAttr(s)}">${escapeHtml(s)}</option>`).join("")}
      </select>
      <select id="poster-activity">
        <option value="">All activities</option>
        ${activities.map(a => `<option value="${escapeAttr(a)}">${escapeHtml(a)}</option>`).join("")}
      </select>
    `;
  }

  const table = new Tabulator(container, {
    data: rows,
    layout: "fitColumns",
    pagination: "local",
    paginationSize: 25,
    paginationSizeSelector: [10, 25, 50, 100],
    movableColumns: true,
    placeholder: "No posters match filters",
    initialSort: [{column: "num", dir: "asc"}],
    rowFormatter: (row) => {
      // Allow click-to-expand for full abstract
      const data = row.getData();
      if (!data._expanded) return;
      const existing = row.getElement().querySelector(".poster-detail");
      if (existing) return;
      const el = document.createElement("div");
      el.className = "poster-detail";
      el.innerHTML = `
        <strong>Authors:</strong> ${escapeHtml(data.authors || "")}<br>
        <strong>Date:</strong> ${escapeHtml(data.start || "")}<br>
        <strong>Activity:</strong> ${escapeHtml(data.activity || "")}<br>
        ${data.player_url ? `<strong>PDF:</strong> <a href="${escapeAttr(data.player_url)}" target="_blank">poster viewer</a><br>` : ""}
        <br>
        <strong>Abstract:</strong><br>
        ${escapeHtml(data.abstract || "(no abstract)").replace(/\n/g, "<br>")}
      `;
      row.getElement().appendChild(el);
    },
    columns: [
      {title: "#", field: "num", width: 80, headerSort: true},
      {title: "Title", field: "title", headerFilter: "input", formatter: "plaintext",
        minWidth: 300, widthGrow: 3,
        cellClick: (_, cell) => {
          const row = cell.getRow();
          const data = row.getData();
          data._expanded = !data._expanded;
          row.reformat();
          // Remove the appended detail if now collapsed
          if (!data._expanded) {
            const el = row.getElement().querySelector(".poster-detail");
            if (el) el.remove();
          }
        }
      },
      {title: "Session", field: "session", headerFilter: "input",
        minWidth: 180, widthGrow: 2},
      {title: "Day", field: "day", width: 100, headerFilter: "input"},
      {title: "Presenter", field: "presenter", headerFilter: "input",
        minWidth: 150, widthGrow: 1}
    ]
  });

  if (statsEl) updateStats(statsEl, rows.length, rows.length);

  // Wire up global search + filter dropdowns
  const search = document.getElementById("poster-search");
  const sessSel = document.getElementById("poster-session");
  const actSel = document.getElementById("poster-activity");
  const applyFilters = () => {
    const q = (search?.value || "").trim().toLowerCase();
    const sess = sessSel?.value || "";
    const act = actSel?.value || "";
    table.setFilter((row) => {
      if (sess && row.session !== sess) return false;
      if (act && row.activity !== act) return false;
      if (q) {
        const hay = `${row.title} ${row.abstract} ${row.authors} ${row.num}`.toLowerCase();
        if (!hay.includes(q)) return false;
      }
      return true;
    });
    const visible = table.getDataCount("active");
    if (statsEl) updateStats(statsEl, visible, rows.length);
  };
  [search, sessSel, actSel].forEach(el => el?.addEventListener("input", applyFilters));
  [search, sessSel, actSel].forEach(el => el?.addEventListener("change", applyFilters));
}

function updateStats(el, visible, total) {
  el.textContent = visible === total
    ? `${total} posters. Click any title to expand the full abstract.`
    : `${visible} of ${total} posters match. Click any title to expand the full abstract.`;
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}
function escapeAttr(s) {
  return escapeHtml(s);
}

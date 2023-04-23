const d = document,
  NodelistRecords = document.querySelectorAll(".data-payment");

const loadDataInTable = () => {
  const listRecord = Array.from(NodelistRecords);
  //console.log(listRecord);
  listRecord.map((el) => {
    //console.log(el.textContent.trim());
    //console.log(el.dataset);
    if (el.textContent.trim() === "SIN PAGAR") {
      const dataUrlUnpain = el.dataset.urlUnpain;
      el.parentNode.classList.add("unpain");
      const link = document.createElement("a");
      link.href = dataUrlUnpain;
      link.classList.add("btn", "btn-primary");
      link.textContent = "Registrar pago";
      const td = document.createElement("td");
      td.appendChild(link);
      el.parentNode.appendChild(td);
    } else if (el.textContent.trim() === "PENDIENTE") {
      const dataUrlPending = el.dataset.urlPending;
      el.parentNode.classList.add("pending");
      const td = document.createElement("td");
      if (dataUrlPending=== "") {
        const parrafo = document.createElement("p");
        parrafo.textContent = "Sin comprobante";
        td.appendChild(parrafo);
      }else{
        const link = document.createElement("a");
        link.href = dataUrlPending;
        link.target = "_blank";
        link.classList.add("btn", "btn-primary");
        link.textContent = "Ver pago";
        td.appendChild(link);
      }
      el.parentNode.appendChild(td);
    } else {
      const dataUrl = el.dataset.url;
      const td = document.createElement("td");
      if (dataUrl === "") {
        const parrafo = document.createElement("p");
        parrafo.textContent = "Sin comprobante";
        td.appendChild(parrafo);
      }else{
        const link = document.createElement("a");
        link.href = dataUrl;
        link.target = "_blank";
        link.classList.add("btn", "btn-primary");
        link.textContent = "Ver pago";
        td.appendChild(link);
      }
      el.parentNode.appendChild(td);
    }
  });
};




loadDataInTable();

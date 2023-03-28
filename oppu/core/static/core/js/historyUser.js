const d = document,
NodelistRecords = document.querySelectorAll(".data-payment");

const loadDataInTable = ()=>{
    const listRecord = Array.from(NodelistRecords);
     
    listRecord.map(el=>{
        console.log(el.textContent.trim());
        if (el.textContent.trim() === "SIN PAGAR") {
            const dataUrlUnpain = el.dataset.urlUnpain;
            el.parentNode.classList.add("unpain");
            el.parentNode.lastChild.innerHTML = `<a href="${dataUrlUnpain}" class="btn btn-primary" >Registrar pago</a>`;

        }else if(el.textContent.trim() === "PENDIENTE"){
            const dataUrlPending = el.dataset.urlPending;
            console.log(el.dataset);
            el.parentNode.classList.add("pending");         
            el.parentNode.lastChild.innerHTML = `<a href="${dataUrlPending}" target="_blank" class="btn btn-primary">Ver pago</a>`;
        }else{
            const dataUrl = el.dataset.url;
            el.parentNode.lastChild.innerHTML = `<a href="${dataUrl}" target="_blank" class="btn btn-primary">Ver pago</a>`;
        }
    });
};

loadDataInTable();

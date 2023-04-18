const d = document;
const $btn = d.createElement("a");//Button Global

const getURLForBtn = ()=>{
    const urlParams = new URLSearchParams(window.location.search);
    let domain = window.location.origin;

    const paramsObj = {};
    for (const [key, value] of urlParams.entries()) {
        if (key !== "q" || key !== "p") {
          paramsObj[key] = value;
        };
    };

    console.log(paramsObj);
    console.log(urlParams);

    

    const hasParams = Object.keys(paramsObj).length > 0;

    const paramsString = hasParams ? new URLSearchParams(paramsObj).toString() : "";

    const url = `${domain}/report${hasParams ? `?${paramsString}` : ""}`;

    
    /* CREATE URL */
    console.log(url);
    $btn.target = "_blank"; 
    $btn.href= url;

    if (hasParams && (!paramsObj.hasOwnProperty("p") || (!paramsObj.hasOwnProperty("q") || paramsObj.q === ""))) {
        createButton();
    }else{
        return false;
    }
    
};

/* DESIGN IN TABLE */
const printPaymentForState = ()=>{
    const elemts = Array.from(d.querySelectorAll(".field-state"));

    elemts.map(el=>{
        if (el.firstElementChild.textContent==="SIN PAGAR") {
            el.parentElement.classList.add("unpain");
        }else if(el.firstElementChild.textContent==="PENDIENTE"){
            el.parentElement.classList.add("pending");   
        }
        //console.log(el.firstChild.textContent);
    });
}

/* BOTON PARA PDF */
const createButton = ()=>{
    const $divButton = document.createElement("div");
    const $tableResults = document.querySelector(".results");
    $btn.textContent= "IMPRIMIR RESULTADOS";
    $btn.classList.add("button-customate");
    $divButton.classList.add("div-button");
    $divButton.appendChild($btn);
    $tableResults.insertAdjacentElement("afterend", $divButton);   
}

document.addEventListener("DOMContentLoaded", function() {
    // Aquí puedes agregar código para manipular el DOM una vez que se ha cargado completamente
    printPaymentForState();
    getURLForBtn();
});

//Cambia url

const d = document;

const LoadMonths = () => {
    let today = new Date();
    let currentMonth = today.getMonth() + 1; // Sumamos 1 porque los meses empiezan en 0
    let select = document.getElementById("user-month-payment");

    for (let i = 1; i <= currentMonth; i++) {
      let option = document.createElement("option");
      option.value = i;
      option.text = getMonthName(i);
      
      select.add(option);
    }

    select.value = currentMonth; 
}

const getMonthName = (month)  => {
  let months = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
  ];

  return months[month - 1];
}

LoadMonths();

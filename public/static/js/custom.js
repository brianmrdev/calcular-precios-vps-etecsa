function calcularPrecio() {
  let dataString = {
    CPU: $("#cpu").val(),
    RAM: $("#ram").val(),
    HDD: $("#hdd").val(),
  };
  if (dataString.CPU == "" || dataString.RAM == "" || dataString.HDD == "") {
    document.querySelector("#resultado-diario").textContent = "";
    document.querySelector("#resultado-mensual").textContent = "";
  } else {
    $.ajax({
      type: "POST",
      url: "/calcular_precio/",
      data: dataString,
      dataType: "json",
      success: function (result) {
        if (result.status == false || result.status == "false") {
          console.log(result.msg);
        } else if (result.status == true || result.status == "true") {
          document.querySelector("#resultado-diario").textContent =
            "Total a pagar diario: " + result.diario + " CUP";
          document.querySelector("#resultado-mensual").textContent =
            "Promedio a pagar mensual: " + result.mensual + " CUP";
        }
      },
    });
  }
}

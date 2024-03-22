const xValues = ["co2", "So2", "no2", "co"];
const yValues = [55, 49, 44, 24];
const barColors = ["red", "green","blue","orange"];

new Chart("myChart", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Air pollution particles"
    }
  }
});
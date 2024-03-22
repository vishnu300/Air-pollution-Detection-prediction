const qValues = ["co2", "so2", "no"];
const wValues = [55, 49, 44 ];
const barColors_1 = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart("PieGraph", {
  type: "doughnut",
  data: {
    fontSize: 1,
    labels: qValues,
    datasets: [{
      backgroundColor: barColors_1,
      data: wValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Air pollution paricle in past"
    }
  }
});

const aValues = [10,20,40,80,120,160,200,240,280,320];

new Chart("lineChart", {
  type: "line",
  data: {
    labels: aValues,
    datasets: [{ 
      label: 'CO2', // Label for CO2 dataset
      data: [73,400,500,600,100,200,300,600,200,100],
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(255, 0, 0, 1.0)", // Red color for CO2
      borderColor: "rgba(255, 0, 0, 1.0)", // Red color for CO2
    }, { 
      label: 'NO2', // Label for NO2 dataset
      data: [16,17,70,190,20,45,40,75,60,70],
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(0, 0, 255, 0.1)", // Light blue color for NO2
      borderColor: "rgba(0, 0, 255, 1.0)", // Blue color for NO2
      
    }, { 
      label: 'SO2', // Label for SO2 dataset
      data: [30,7,20,25,36,40,23,10,27,18],
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(173, 216, 230, 1.0)", // Custom light blue color for SO2
      borderColor: "yellow", // Blue color for SO2

    }]
  },
  options: {
    legend: {
      display: true,
      labels: {
        fontColor: 'black', // Adjust font color if needed
        fontSize: 14 // Adjust font size if needed
      }
    }
  }
});

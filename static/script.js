function predictImage() {
  const formData = new FormData(document.getElementById("uploadForm"));

  const predictionResultElement = document.getElementById("predictionResult");

  fetch("/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if ("prediction" in data) {
        // Prediction successful
        predictionResultElement.innerText = `Prediksi Tingkat Fokus: ${
          data.prediction === 0
            ? "Konsentrasi"
            : data.prediction === 1
            ? "Netral"
            : "Rileks"
        }`;
      } else if ("error" in data) {
        // Error occurred
        predictionResultElement.innerText = `Error: ${data.error}`;
      } else {
        // Unexpected response format
        predictionResultElement.innerText = "Unexpected response from server";
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      predictionResultElement.innerText = "Error occurred during prediction";
    });
}

let loadFile = function (event) {
  var image = document.getElementById("imageDisplay");
  image.src = URL.createObjectURL(event.target.files[0]);
};

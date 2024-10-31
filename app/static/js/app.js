document.getElementById("uploadForm").onsubmit = async function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById("fileInput");
    const textInput = document.getElementById("textInput");
    const formData = new FormData();
    
    if (fileInput.files.length > 0) {
        formData.append("file", fileInput.files[0]);
    } else {
        formData.append("text", textInput.value);
    }

    // Submit the form and handle progress
    const response = await fetch('/upload', { method: 'POST', body: formData });
    const data = await response.json();

    if (data.processing_time) {
        alert(`Processing Time: ${data.processing_time} seconds`);
    }
    
    // Display dataset in the output area
    document.getElementById("output").innerText = JSON.stringify(data.dataset, null, 2);
}

document.addEventListener("DOMContentLoaded", function () {
    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("fileInput");
    const fileList = document.getElementById("fileList");
    const deleteButton = document.getElementById("deleteButton");

    dropArea.addEventListener("dragover", function (e) {
        e.preventDefault();
        dropArea.classList.add("highlight");
    });

    dropArea.addEventListener("dragleave", function () {
        dropArea.classList.remove("highlight");
    });

    dropArea.addEventListener("drop", function (e) {
        e.preventDefault();
        dropArea.classList.remove("highlight");

        const files = e.dataTransfer.files;
        displayFileNames(files);

        // You can perform further actions with the dropped files here.
    });

    dropArea.addEventListener("click", function () {
        fileInput.click();
    });

    fileInput.addEventListener("change", function () {
        const files = fileInput.files;
        displayFileNames(files);

        // You can perform further actions with the selected files here.
    });

    /*Delete button*/
    deleteButton.addEventListener("click", function () {
        // Clear the selected file(s) in the file input
        fileInput.value = null;
        // Clear the displayed file names
        fileList.innerHTML = "";
    });

    function displayFileNames(files) {
        fileList.innerHTML = ""; // Clear previous file names
        for (let i = 0; i < files.length; i++) {
            const fileName = files[i].name;
            const listItem = document.createElement("p");
            listItem.textContent = fileName;
            fileList.appendChild(listItem);
        }
    }
});

const editButton = document.getElementById("editButton");

editButton.addEventListener("click", function () {
    const fileName = fileList.querySelector("p"); // Get the first displayed file name (you can customize this logic)
    
    if (fileName) {
        const newName = prompt("Enter a new name for the file:", fileName.textContent);
        
        if (newName !== null) {
            // Update the displayed file name with the new name
            fileName.textContent = newName;
        }
    }
});
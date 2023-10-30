document.addEventListener("DOMContentLoaded", function () {
    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("fileInput");
    const fileList = document.getElementById("fileList");

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

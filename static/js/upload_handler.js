/**
 * Upload Handler Script
 * Manages file selection events and visual feedback on the upload dropzone.
 */
function onFileSelected(input) {
    const file = input.files[0];
    const titleEl = document.getElementById('uploadTitle');
    const descEl = document.getElementById('uploadDesc');
    const statusEl = document.getElementById('fileStatus');

    if (file) {
        if (titleEl) titleEl.textContent = file.name;
        if (descEl) descEl.textContent = "Format: " + file.name.split('.').pop().toUpperCase() + " | Ready for audit";
        if (statusEl) {
            statusEl.style.display = "block";
            statusEl.textContent = "Selected File: " + file.name + " (" + (file.size / 1024).toFixed(1) + " KB)";
        }
    }
}

/**
 * PDF Export Script
 * Generates an A4 vector PDF using html2pdf.js with automatic fallback to native print.
 */
function downloadReportPDF(filename) {
    const btn = document.querySelector('.btn-download');
    const originalText = btn ? btn.textContent : "Download Analysis PDF";
    
    if (btn) {
        btn.textContent = "Generating PDF...";
        btn.disabled = true;
    }

    const element = document.getElementById('reportContainer');
    const reportName = filename ? filename.replace(/\.[^/.]+$/, "") : "Resume";

    const opt = {
        margin: [8, 8, 8, 8],
        filename: `ATS_Analysis_Report_${reportName}.pdf`,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true, logging: false },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    if (typeof html2pdf !== 'undefined') {
        html2pdf().set(opt).from(element).save().then(() => {
            if (btn) {
                btn.textContent = originalText;
                btn.disabled = false;
            }
        }).catch(err => {
            console.error("html2pdf export failed, falling back to window.print():", err);
            window.print();
            if (btn) {
                btn.textContent = originalText;
                btn.disabled = false;
            }
        });
    } else {
        window.print();
        if (btn) {
            btn.textContent = originalText;
            btn.disabled = false;
        }
    }
}

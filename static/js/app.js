// Main app utilities
document.addEventListener('DOMContentLoaded', () => {
    // Update range input values
    document.querySelectorAll('input[type="range"]').forEach(range => {
        const valueDisplay = range.nextElementSibling;
        if (valueDisplay && valueDisplay.classList.contains('range-value')) {
            range.addEventListener('input', (e) => {
                valueDisplay.textContent = e.target.value;
            });
        }
    });

    // Active nav link
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.color = 'var(--accent-primary)';
        }
    });
});

// Utility functions
function showLoading(button) {
    const btnText = button.querySelector('.btn-text');
    const btnLoader = button.querySelector('.btn-loader');
    if (btnText) btnText.style.display = 'none';
    if (btnLoader) btnLoader.style.display = 'inline';
    button.disabled = true;
}

function hideLoading(button) {
    const btnText = button.querySelector('.btn-text');
    const btnLoader = button.querySelector('.btn-loader');
    if (btnText) btnText.style.display = 'inline';
    if (btnLoader) btnLoader.style.display = 'none';
    button.disabled = false;
}

function showResult(containerId, content, isMock = false) {
    const container = document.getElementById(containerId);
    container.innerHTML = `
        <div class="result-header">
            <h3>Generated Content ${isMock ? '<span class="mock-badge">DEMO MODE</span>' : ''}</h3>
            <div class="result-actions">
                <button class="icon-btn" onclick="copyToClipboard(this)" title="Copy">📋</button>
            </div>
        </div>
        <div class="result-content">${content}</div>
    `;
    container.style.display = 'block';
}

function copyToClipboard(button) {
    const resultContent = button.closest('.result-container').querySelector('.result-content');
    const text = resultContent.innerText;

    navigator.clipboard.writeText(text).then(() => {
        button.textContent = '✓';
        setTimeout(() => {
            button.textContent = '📋';
        }, 2000);
    });
}

function formatMarkdown(text) {
    // Handle null, undefined, or non-string values
    if (!text || typeof text !== 'string') {
        return '<p style="color: var(--error);">Error: Invalid content received</p>';
    }

    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/\n/g, '<br>');
}

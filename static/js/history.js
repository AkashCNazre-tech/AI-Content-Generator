// History page functionality
document.addEventListener('DOMContentLoaded', () => {
    loadHistory();

    const filterSelect = document.getElementById('filter-type');
    if (filterSelect) {
        filterSelect.addEventListener('change', () => {
            loadHistory(filterSelect.value);
        });
    }
});

async function loadHistory(contentType = '') {
    const historyList = document.getElementById('history-list');
    historyList.innerHTML = '<div class="loading">Loading history...</div>';

    try {
        const url = contentType ? `/api/history?content_type=${contentType}` : '/api/history';
        const response = await fetch(url);
        const items = await response.json();

        if (items.length === 0) {
            historyList.innerHTML = '<div class="loading">No content generated yet.</div>';
            return;
        }

        historyList.innerHTML = items.map(item => createHistoryItem(item)).join('');
    } catch (error) {
        historyList.innerHTML = `<div class="loading" style="color: var(--error);">Error loading history: ${error.message}</div>`;
    }
}

function createHistoryItem(item) {
    const date = new Date(item.created_at).toLocaleString();
    const isImage = item.content_type === 'image';

    const resultContent = isImage
        ? `<img src="${item.result}" alt="Generated image">`
        : `<div class="history-result">${formatHistoryText(item.result)}</div>`;

    return `
        <div class="history-item">
            <div class="history-item-header">
                <span class="history-type">${item.content_type}</span>
                <span class="history-date">${date}</span>
            </div>
            <div class="history-prompt"><strong>Prompt:</strong> ${item.prompt}</div>
            ${resultContent}
            <div style="margin-top: 1rem;">
                <button class="icon-btn" onclick="copyHistoryItem('${item.id}')" title="Copy">📋 Copy</button>
                <button class="icon-btn" onclick="deleteHistoryItem(${item.id})" title="Delete" style="color: var(--error);">🗑️ Delete</button>
            </div>
        </div>
    `;
}

function formatHistoryText(text) {
    if (text.length > 300) {
        return text.substring(0, 300) + '... <a href="#" onclick="event.preventDefault(); this.parentElement.innerHTML = \'' + text.replace(/'/g, "\\'") + '\'">Show more</a>';
    }
    return text;
}

function copyHistoryItem(itemId) {
    const item = document.querySelector(`[data-id="${itemId}"]`);
    if (item) {
        const text = item.querySelector('.history-result').innerText;
        navigator.clipboard.writeText(text);
    }
}

async function deleteHistoryItem(itemId) {
    if (!confirm('Are you sure you want to delete this item?')) return;

    try {
        await fetch(`/api/history/${itemId}`, { method: 'DELETE' });
        loadHistory();
    } catch (error) {
        alert('Error deleting item: ' + error.message);
    }
}

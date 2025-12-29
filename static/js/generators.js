// Tab switching
document.addEventListener('DOMContentLoaded', () => {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabName = btn.dataset.tab;

            // Update buttons
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Update content
            tabContents.forEach(content => {
                content.classList.remove('active');
                if (content.id === `${tabName}-tab`) {
                    content.classList.add('active');
                }
            });
        });
    });

    // Setup form handlers
    setupAdGenerator();
    setupImageGenerator();
    setupBlogGenerator();
    setupSocialGenerator();
});

// Ad Generator
function setupAdGenerator() {
    const form = document.getElementById('ad-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const button = form.querySelector('button[type="submit"]');

        showLoading(button);

        try {
            const response = await fetch('/api/generate-ad', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    product_name: formData.get('product_name'),
                    description: formData.get('description'),
                    target_audience: formData.get('target_audience'),
                    tone: formData.get('tone'),
                    temperature: parseFloat(formData.get('temperature'))
                })
            });

            const data = await response.json();
            showResult('ad-result', formatMarkdown(data.result), data.mock);
        } catch (error) {
            showResult('ad-result', `<p style="color: var(--error);">Error: ${error.message}</p>`);
        } finally {
            hideLoading(button);
        }
    });
}

// Image Generator
function setupImageGenerator() {
    const form = document.getElementById('image-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const button = form.querySelector('button[type="submit"]');

        showLoading(button);

        try {
            const response = await fetch('/api/generate-image', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    prompt: formData.get('prompt'),
                    size: formData.get('size')
                })
            });

            const data = await response.json();
            const content = `
                <p><strong>Prompt:</strong> ${formData.get('prompt')}</p>
                <img src="${data.result}" alt="Generated image" style="max-width: 100%; border-radius: 12px; margin-top: 1rem;">
            `;
            showResult('image-result', content, data.mock);
        } catch (error) {
            showResult('image-result', `<p style="color: var(--error);">Error: ${error.message}</p>`);
        } finally {
            hideLoading(button);
        }
    });
}

// Blog Generator
function setupBlogGenerator() {
    const form = document.getElementById('blog-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const button = form.querySelector('button[type="submit"]');

        showLoading(button);

        try {
            const response = await fetch('/api/generate-blog', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    topic: formData.get('topic'),
                    keywords: formData.get('keywords'),
                    tone: formData.get('tone'),
                    length: formData.get('length'),
                    temperature: 0.7
                })
            });

            const data = await response.json();
            showResult('blog-result', formatMarkdown(data.result), data.mock);
        } catch (error) {
            showResult('blog-result', `<p style="color: var(--error);">Error: ${error.message}</p>`);
        } finally {
            hideLoading(button);
        }
    });
}

// Social Media Generator
function setupSocialGenerator() {
    const form = document.getElementById('social-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const button = form.querySelector('button[type="submit"]');

        showLoading(button);

        try {
            const response = await fetch('/api/generate-social', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    platform: formData.get('platform'),
                    topic: formData.get('topic'),
                    tone: formData.get('tone'),
                    include_hashtags: formData.get('include_hashtags') === 'on',
                    temperature: 0.8
                })
            });

            const data = await response.json();
            showResult('social-result', formatMarkdown(data.result), data.mock);
        } catch (error) {
            showResult('social-result', `<p style="color: var(--error);">Error: ${error.message}</p>`);
        } finally {
            hideLoading(button);
        }
    });
}

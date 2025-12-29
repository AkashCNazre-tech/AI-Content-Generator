document.addEventListener('DOMContentLoaded', () => {
    const generatorForm = document.getElementById('ad-generator-form');
    const generateBtn = document.querySelector('.generate-btn');
    const adResult = document.getElementById('ad-result');
    const imageResult = document.getElementById('image-result');
    const resultsSection = document.getElementById('results');

    if (generatorForm) {
        generatorForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // UI Loading State
            const originalBtnText = generateBtn.innerHTML;
            generateBtn.innerHTML = '<span>Generating Magic...</span>';
            generateBtn.disabled = true;
            resultsSection.hidden = false;
            adResult.innerHTML = '<div class="loading-spinner"></div>';
            imageResult.innerHTML = '<div class="loading-spinner"></div>';

            // Gather Data
            const formData = {
                product_name: document.getElementById('productName').value,
                description: document.getElementById('productDesc').value,
                target_audience: document.getElementById('targetAudience').value,
                tone: document.getElementById('tone').value
            };

            try {
                // 1. Generate Ad Copy
                const adResponse = await fetch('/api/generate-ad', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });

                if (!adResponse.ok) throw new Error('Ad generation failed');
                const adData = await adResponse.json();

                // Render Ad (supporting markdown-ish line breaks)
                adResult.innerHTML = marked(adData.script) || adData.script.replace(/\n/g, '<br>');
                if (adData.mock) {
                    adResult.innerHTML += '<p class="mock-note"><em>(Mock Response: Add API Key for real results)</em></p>'
                }

                // 2. Generate Image (using Product Name + Description as prompt)
                const imagePrompt = `Advertisement for ${formData.product_name}, ${formData.description}, highly detailed, professional photography, ${formData.tone} style`;

                const imgResponse = await fetch('/api/generate-image', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt: imagePrompt })
                });

                if (!imgResponse.ok) throw new Error('Image generation failed');
                const imgData = await imgResponse.json();

                imageResult.innerHTML = `<img src="${imgData.image_url}" alt="Generated Ad Visual" class="fade-in">`;
                if (imgData.mock) {
                    imageResult.innerHTML += '<p class="mock-note"><em>(Placeholder Image)</em></p>'
                }

            } catch (error) {
                console.error(error);
                adResult.innerHTML = `<p class="error">Error: ${error.message}</p>`;
                imageResult.innerHTML = '';
            } finally {
                // Reset Button
                generateBtn.innerHTML = originalBtnText;
                generateBtn.disabled = false;
            }
        });
    }
});

// Simple Markdown parser for bolding/line breaks if needed
function marked(text) {
    if (!text) return '';
    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\n/g, '<br>');
}

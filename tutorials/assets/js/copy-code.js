// Adds a Copy button to code blocks inside accordion panels
// (<details class="accordion" markdown="1">), e.g. the definitions on the Materials page.
(() => {
  document.querySelectorAll('.markdown-body details.accordion div.highlight').forEach((block) => {
    const code = block.querySelector('code');
    if (!code) return;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-code';
    button.textContent = 'Copy';
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(code.textContent);
        button.textContent = 'Copied!';
      } catch {
        // No clipboard access (e.g. plain http): select the code so Ctrl+C works.
        getSelection().selectAllChildren(code);
        button.textContent = 'Press Ctrl+C';
      }
      setTimeout(() => {
        button.textContent = 'Copy';
      }, 2000);
    });
    block.appendChild(button);
  });
})();

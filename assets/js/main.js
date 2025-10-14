
document.addEventListener("DOMContentLoaded", function() {
    const highlights = document.querySelectorAll('div.highlight');
  
    highlights.forEach(function(highlight) {
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = 'Copy';
      
        highlight.appendChild(button);
      
        button.addEventListener('click', function() {
            const code = highlight.querySelector('pre.highlight code');
            const text = code.innerText;
          
            navigator.clipboard.writeText(text).then(function() {
                button.textContent = 'Copied!';
                setTimeout(function() {
                    button.textContent = 'Copy';
                }, 2000); 
            }, function(err) {
                button.textContent = 'Error';
                console.error('Could not copy text: ', err);
            });
        });
    });
});

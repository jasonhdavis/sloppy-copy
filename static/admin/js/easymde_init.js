document.addEventListener('DOMContentLoaded', function() {
    const editors = document.querySelectorAll('.markdown-editor');
    editors.forEach(el => {
        new EasyMDE({ element: el });
    });
});

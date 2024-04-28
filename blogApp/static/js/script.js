tinymce.init({
    selector: 'textarea'
});


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('input[type="search"]');
    var instances = M.Search.init(elems, {});
});

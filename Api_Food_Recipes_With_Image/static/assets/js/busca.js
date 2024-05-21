window.onload = function(){
    var titles = document.querySelectorAll('.recipe h3');

    titles.forEach(function(title){
        title.addEventListener('click', function(){
            var details = this.nextElementSibling;
            details.classList.toggle('hidden');
        });
    });
};


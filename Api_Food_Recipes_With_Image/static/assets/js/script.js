document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault(); 
        
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        
        if (username === 'admin' && password === 'admin123') {
            window.location.href = '../pagina_teste/pages/busca.html';
        } else {
           
            var errorMessage = document.querySelector('span');
            errorMessage.textContent = 'Nome de usuário ou senha incorretos.';
        }
    });
});

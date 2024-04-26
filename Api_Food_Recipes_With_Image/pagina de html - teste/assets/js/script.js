document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Impede o envio padrão do formulário
        
        // Obter os valores dos campos de nome de usuário e senha
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        // Supondo que a validação do login seja bem-sucedida, redirecione para a página 'busca.html'
        if (username === 'admin' && password === 'admin') {
            // Redirecionar para a página 'busca.html'
            window.location.href = '../../pages/busca.html';
        } else {
            // Se o login falhar, exiba uma mensagem de erro (você pode estilizar isso de acordo com sua preferência)
            var errorMessage = document.querySelector('span');
            errorMessage.textContent = 'Nome de usuário ou senha incorretos.';
        }
    });
});

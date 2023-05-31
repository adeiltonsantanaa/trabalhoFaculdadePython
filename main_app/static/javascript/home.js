document.addEventListener('DOMContentLoaded', function() {
    var botao = document.getElementById('botao');
    var divEsconder = document.querySelector('.welcome');
    
    botao.addEventListener('click', function() {
        divEsconder.style.display = 'none';
        console.log('clicado')
    });
});
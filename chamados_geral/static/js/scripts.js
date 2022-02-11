$(document).ready(function(){
    var baseUrl = 'http://localhost:8000/'; //talvez precise alterar quando subir no servidor
    //Evento para o botão excluir, não deletar direto, após isso faremos uma verificação para saber se o user deseja mesmo excluir
    var deleteBtn = $('.delete-btn');
    var filter = $('#filter'); //marcação para scriptar o filtro

    $(deleteBtn).on('click', function(e){
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer mesmo deletar este chamado ?');

        if(result){
            window.location.href = delLink;
        }

    });

    //função/ação do filtro
    $(filter).change(function(){
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    })


  

})

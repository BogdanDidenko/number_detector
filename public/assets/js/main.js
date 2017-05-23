$(function(){
    var dissable = false;
    var text = 'Возможно вы имели ввиду ';
    $('#send').on('click', function() {
        if(dissable) return;
        var imageVectorize = Global.getPaintedCalls();
        $('.answer').hide(300);
        $.ajax({
            url: '/data',
            method: 'POST',
            dataType: 'json',
            data: {data: imageVectorize},
            success: (res)=>{
                console.log(res);
                $('.answer').show(300);
                $('.answer').html(text + res.number);

                dissable = false;
            }
        })
        dissable = true;
        console.log(imageVectorize);
    })
});
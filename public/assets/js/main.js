$(function(){
    var dissable = false;
    $('#send').on('click', function() {
        if(dissable) return;
        var imageVectorize = Global.getPaintedCalls();
        $.ajax({
            url: '/data',
            method: 'POST',
            dataType: 'json',
            data: {data: imageVectorize},
            success: (res)=>{
                console.log(res);
                dissable = false;
            }
        })
        dissable = true;
        console.log(imageVectorize);
    })
});
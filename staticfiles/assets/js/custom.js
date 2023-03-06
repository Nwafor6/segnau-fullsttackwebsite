$(document).ready(function() {
    // sSubscribe user to new letter
    $("#newsletter").submit(function(e){
        e.preventDefault()
        console.log($("#email").val())
        $.ajax({
            type:"POST",
            url:`http://127.0.0.1:8000/subscribe/`,
            data:{
                "email":$("#email").val()
            },
            success:function(resp){
                $("#newsletter_alert").html(`
                <div class="alert alert-success alert-dismissible fade show mt-3" role="alert">
                    <strong>${resp.detail}</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
                `)
                document.getElementById("newsletter").reset()
            },
            error:function(err){
                console.log(err)
            }
        })
    })
    
    









    
})
$(document).ready(function() {
    // sSubscribe user to new letter
    $(".email-form").submit(function(e){
        e.preventDefault()
        console.log($("#email").val())
        $.ajax({
            type:"POST",
            url:`https://segnau.pythonanywhere.com/contact-us/`,
            data:{
                "email":$("#email").val(),
                "name":$("#name").val(),
                "subject":$("#subject").val(),
                "message":$("#message").val()
            },
            success:function(resp){
                $("#sent-message").html(`
                <div class="alert alert-success alert-dismissible fade show mt-3" role="alert">
                    <strong>${resp.detail}</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
                `)
                document.getElementByClassName("email-form").reset()
            },
            error:function(err){
                console.log(err)
            }
        })
    })
    
    









    
})